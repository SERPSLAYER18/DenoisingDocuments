# DenoisingDocuments 📃🧹🔍
Web-app for denoising of text on images

Web application capable of:
*	Denoising scans of documents by removing artifacts such as fold lines and dirt stains.
*	Text recognition on denoised images
*	Register, login, save & view results history

A non-compressing convolutional autoencoder neural network architecture was used for denoising. And pyTesseract package was used for text recognition. Web app powered by Flask framework. SQLAlchemy ORM, Flask Login, PostgreSQL are used to store user data. App was dockerized and deployed or remote machine. 

## Endpoints:

`/signup`  - Sign up endpoint \
`/login`   - Log in endpoint \
`/logout`  - Log out endpoint \
`/profile` - Profile page \
`/history` - History page \
`/denoise` - Denoising page \
`/predict` - Predictions page 

## Tests: 🔬🧫🧪
~~~
pytest .\tests\
~~~

## Installation & deploy: 🧑‍💻👟💻

~~~
docker-compose up 
~~~
