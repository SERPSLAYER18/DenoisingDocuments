if __name__ == '__main__':
    from tensorflow.keras.models import load_model
    import tensorflow

    print(tensorflow.__version__)

    autoencoder = load_model('static/ConvAutoEncoder')
