import cv2
import numpy as np
from tensorflow.keras.models import load_model as load_tf_model
from flask import current_app

IMAGE_SIZE = (540, 540)
IMAGE_SHAPE = (*IMAGE_SIZE, 1)


def load_model(path='App/static/ConvAutoEncoder'):
    autoencoder = load_tf_model(path)
    return autoencoder


def image_preprocessing(image):
    img = np.asarray(image, dtype="float32")
    current_app.logger.info(f'Input image shape: {img.shape}')
    old_shape = img.shape
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    current_app.logger.info(f'Image shape before resize: {img.shape}')
    img = cv2.resize(img, IMAGE_SIZE)
    current_app.logger.info(f'Image shape after resize: {img.shape}')
    img = np.reshape(img, IMAGE_SHAPE)
    current_app.logger.info(f'Image shape after reshape: {img.shape}')
    img = img / 255.0
    return img, old_shape


def reverse_process(img, shape):
    img = cv2.cvtColor(np.array(img), cv2.COLOR_GRAY2RGB)
    img = cv2.resize(img, tuple(reversed(shape[0:2])))
    img = img * 255
    img = np.asarray(img).astype(np.uint8)
    return img
