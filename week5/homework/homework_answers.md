#### Question 1
``` bash
poetry --version
> Poetry (version 1.6.1)
```

#### Question 2
``` bash
poetry add scikit-learn=1.3.1
```
First hash in `poetry.lock` file is: `sha256:1a231cced3ee3fa04756b4a7ab532dc9417acd581a330adff5f2c01ac2831fcf` that corresponds to the file `scikit-learn-1.3.1.tar.gz`

#### Question 3
``` bash
poetry run python model.py
> Credit probability: 0.902
```

#### Question 4
``` bash
poetry add flask gunicorn requests
poetry run gunicorn --bind 0.0.0.0:5000 flask_model:app
```
Now I can make prediction using:
``` python
poetry run python
Python 3.10.13 (main, Oct  7 2023, 21:19:38) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> url = "http://localhost:5000/predict"
>>> client = {"job": "unknown", "duration": 270, "poutcome": "failure"}
>>> requests.post(url, json=client).json()
{'prediction': True, 'probability': 0.14}
```

#### Question 5
``` bash
docker pull svizor/zoomcamp-model:3.10.12-slim
docker images
REPOSITORY              TAG            IMAGE ID       CREATED        SIZE
svizor/zoomcamp-model   3.10.12-slim   08266c8f0c4b   10 hours ago   147MB
```

#### Question 6
``` bash
touch Dockerfile
docker build -t homework-w5 ./
docker run --rm -p 5000:5000 homework-w5
```
Now I can make prediction using:
``` python
poetry run python
Python 3.10.13 (main, Oct  7 2023, 21:19:38) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> url = "http://localhost:5000/predict"
>>> client = {"job": "retired", "duration": 445, "poutcome": "success"}
>>> requests.post(url, json=client).json()
{'prediction': True, 'probability': 0.727}
```