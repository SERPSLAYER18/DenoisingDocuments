import os
from pathlib import Path
import cv2
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from tqdm.auto import tqdm
import random

from sklearn.model_selection import train_test_split
import tensorflow as tf

from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import (Conv2D,
                                     MaxPooling2D,
                                     UpSampling2D,
                                     Dropout,
                                     Conv2DTranspose,
                                     Input,
                                     BatchNormalization,
                                     UpSampling2D)
from tensorflow.keras.callbacks import EarlyStopping
import imgaug as ia
from imgaug import augmenters as iaa

IMAGE_SIZE = (540, 540)
IMAGE_SHAPE = (*IMAGE_SIZE, 1)


def image_preprocessing(image):
    img = np.asarray(image, dtype="float32")
    old_shape = img.shape
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, IMAGE_SIZE)
    img = np.reshape(img, IMAGE_SHAPE)
    img = img / 255.0
    return img, old_shape


def reverse_process(img, shape):
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    img = cv2.resize(img, shape[0:2])
    img = img * 255
    img = np.asarray(img, dtype="int32")
    return img


class DenoisingAutoencoder(Model):
    def __init__(self):
        super(DenoisingAutoencoder, self).__init__()
        self.encoder = tf.keras.Sequential([
            Input(shape=IMAGE_SHAPE),
            Conv2D(48, (3, 3), activation='relu', padding='same'),
            Conv2D(72, (3, 3), activation='relu', padding='same'),
            Conv2D(144, (3, 3), activation='relu', padding='same'),
            BatchNormalization(),
            MaxPooling2D((2, 2), padding='same'),
            Dropout(0.5),
        ])

        self.decoder = tf.keras.Sequential([
            Conv2D(144, (3, 3), activation='relu', padding='same'),
            Conv2D(72, (3, 3), activation='relu', padding='same'),
            Conv2D(48, (3, 3), activation='relu', padding='same'),
            BatchNormalization(),
            UpSampling2D((2, 2)),
            Conv2D(1, (3, 3), activation='sigmoid', padding='same')
        ])

    def call(self, x, **kwargs):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded
