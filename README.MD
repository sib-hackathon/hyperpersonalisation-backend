## Configuration

1. `pip install requirements.txt`
1. `python setup.py`
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

### Option Saving
1. http://127.0.0.1:8000/suggestions/option-suggestions (GET)  
Sample Get Data
```
[
  {
    "button_id": 2,
    "button_name": "Test 2",
    "count": 1
  }
]
```
2. http://127.0.0.1:8000/suggestions/option-suggestions (POST)  
Sample Post Data
```
{
    "button_id": 2
}
```

### Option Suggesting
1. http://127.0.0.1:8000/suggestions/option-saving (GET)  
Sample Get Data
```
[
  {
    "button_id": 2,
    "button_name": "Test 2",
    "count": 1
  }
]
```
2. http://127.0.0.1:8000/suggestions/option-saving (POST)
Sample Post Data
```
{
    "button_id": 2
}
```

### Notification
1. http://127.0.0.1:8000/notification (GET)  
Sample Get Data
```
{
  "id": int,
  "user": "uuid",
  "title": "E-Lock Enabled",
  "message": "You have enabled the E-Lock for a while and has not been disabled. Please disable it if you are done using it.",
  "date_created": "2023-11-01T04:59:35.225349Z",
  "date_updated": "2023-11-01T05:23:02.872374Z"
}
```
2. http://127.0.0.1:8000/notification/<int:id>  
Sample Post Data
```
{
  "read": true
}
```