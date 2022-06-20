import cv2
import numpy as np
from tensorflow.keras.models import load_model as load_tf_model

IMAGE_SIZE = (540, 540)
IMAGE_SHAPE = (*IMAGE_SIZE, 1)


def load_model():
    autoencoder = load_tf_model('App/static/ConvAutoEncoder')
    return autoencoder


def image_preprocessing(image):
    img = np.asarray(image, dtype="float32")
    old_shape = img.shape
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, IMAGE_SIZE)
    img = np.reshape(img, IMAGE_SHAPE)
    img = img / 255.0
    return img, old_shape


def reverse_process(img, shape):
    img = cv2.cvtColor(np.array(img), cv2.COLOR_GRAY2RGB)
    img = cv2.resize(img, tuple(reversed(shape[0:2])))
    img = img * 255
    img = np.asarray(img, dtype="int32")
    return img
