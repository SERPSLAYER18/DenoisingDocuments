import numpy as np
import pytesseract
from flask import Blueprint, render_template, request, jsonify, current_app
from flask_login import login_required, current_user

from . import model, db
from .NN import image_preprocessing, reverse_process
from .entities import Computation
from .util import base64_to_pil, np_to_base64

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    computations_count = Computation.query.filter_by(user_id=current_user.id).count()
    return render_template('profile.html',
                           name=current_user.name,
                           computations_count=computations_count)


@main.route('/history')
@login_required
def history():
    query = Computation.query.filter_by(user_id=current_user.id)
    return render_template('history.html', query=query)


@main.route('/denoise')
@login_required
def denoise():
    return render_template('denoise.html', name=current_user.name)


@login_required
@main.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        img = base64_to_pil(request.json)
        #print(f'Input image shape: {img.shape}')
        #current_app.logger.info(f'Input image shape: {img.shape}')
        img, old_shape = image_preprocessing(img)
        #print(f'After preprocessing: {img.shape}')
        img = model(img[np.newaxis, :])[0]
        #print(f'Image shape after encoder: {img.shape}')
        img = reverse_process(img, old_shape)
        recognized_text = pytesseract.image_to_string(img)
        base64_image = np_to_base64(img)

        # ADD COMPUTATION TO DB
        try:
            computation = Computation(user_id=current_user.id,
                                      input_image=request.json,
                                      denoised_image=base64_image,
                                      extracted_text=recognized_text
                                      )
            db.session.add(computation)
            db.session.commit()
        except:
            current_app.logger.error(f'Size of image is too large {img.shape}')

        return jsonify(denoised_img=base64_image, recognized_text=recognized_text)
    return None
