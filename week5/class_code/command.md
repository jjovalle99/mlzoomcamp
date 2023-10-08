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
```python
# start gunicorn wsgi
poetry run gunicorn --bind 0.0.0.0:5000 05-test-model:app

# The other steps are the same
```