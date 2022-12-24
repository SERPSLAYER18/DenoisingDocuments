import os
import unittest
from tensorflow.keras.models import load_model as load_tf_model
def load_model(path='./App/static/ConvAutoEncoder'):
    autoencoder = load_tf_model(path)
    return autoencoder



class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_model_existing(self):
        self.assertTrue(os.path.exists('./flask_container/App/static/ConvAutoEncoder/saved_model.pb'))

    def test_model_loading(self):
        model = load_model('./flask_container/App/static/ConvAutoEncoder')


if __name__ == '__main__':
    unittest.main()
