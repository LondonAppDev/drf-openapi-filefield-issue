# Django REST Framework Swagger FileField OpenAPI Issue

When generating an OpenAPI schema, fields that use FileField are set as strings.


## Steps to re-produce

 1. Create virtualenv: `python -m venv env`
 2. Source virtual env: `source env/bin/activate`
 3. Install dependencies: `pip install -r requirements.txt`
 4. Run server: `python manage.py runserver`
 5. Navigate to [http://127.0.0.1:8000/api/docs](http://127.0.0.1:8000/api/docs)

You will find that the input field is `string` and there is no file upload option.
