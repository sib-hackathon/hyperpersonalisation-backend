## Configuration

1. `pip install requirements.txt`
2. `python manage.py makemigrations`
3. `python manage.py migrate`
4. `python manage.py createsuperuser`
5. `python manage.py runserver`


## Available APIs
### JWT Token and Refresh
1. http://127.0.0.1:8000/accounts/api/token/ (POST)
2. http://127.0.0.1:8000/accounts/api/token/refresh (POST)

### User Data
1. http://127.0.0.1:8000/accounts/api/profile (GET)
2. http://127.0.0.1:8000/accounts/api/profile (POST)