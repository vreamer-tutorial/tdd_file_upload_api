## TDD file upload API with Flask

### Setup
* Create a virtualenv
```
virtualenv venv

. venv/bin/activate
```
* Install Flask
```
pip install Flask
```
or
```
pip install -r requirements.txt
```
* Create a Flask app

### Run Tests
```
python -m unittest tests.test_file_upload
```

### Run Application
```
python app.py
```

### Upload File
```
http://localhost:5000/file/upload
```
