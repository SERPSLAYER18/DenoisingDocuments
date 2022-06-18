docker build -t flaskapp:latest .

docker run --link postgres -p 5000:5000 flaskapp
