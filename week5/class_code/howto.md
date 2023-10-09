#### Flask api call
```python
# start flask web server
poetry run python 05-test-model.py

# From python
import requests
url = 'http://localhost:5000/predict'
response = requests.post(url, json=customer)
result = response.json()
result 

# Using Curl
curl -X POST -H "Content-Type: application/json" -d @customer.json http://localhost:5000/predict

```

#### Guvicorn
```bash
# start gunicorn wsgi
poetry run gunicorn --bind 0.0.0.0:5000 05-test-model:app

# The other steps are the same
```

#### Docker
```bash
# prepare files before
cp ~/mlzoomcamp/poetry.lock ~/mlzoomcamp/week5/class_code/poetry.lock 
cp ~/mlzoomcamp/pyproject.toml ~/mlzoomcamp/week5/class_code/pyproject.toml

# build docker image
docker build -t churn-app ~/mlzoomcamp/week5/class_code/

# run app
docker run --rm -p 5000:5000 churn-app

# now I can use curl on localhost to make calls to api

# clean up folder
rm ~/mlzoomcamp/week5/class_code/pyproject.toml ~/mlzoomcamp/week5/class_code/poetry.lock 
```

#### AWS Elastic Beanstalk
```bash
# prepare files before
cp ~/mlzoomcamp/poetry.lock ~/mlzoomcamp/week5/class_code/poetry.lock 
cp ~/mlzoomcamp/pyproject.toml ~/mlzoomcamp/week5/class_code/pyproject.toml

# aws elastic beanstalk
eb init -p docker -r us-east-1 churn-serving
eb create churn-serving-env

# test it
curl -X POST -H "Content-Type: application/json" -d @customer.json http://{ebhost}/predict

# terminate
eb terminate churn-serving-env

# clean up folder
rm ~/mlzoomcamp/week5/class_code/pyproject.toml ~/mlzoomcamp/week5/class_code/poetry.lock 
```