## How to deploy
###1- create virtual environment:
```
# install virtualenv dependency
pip install virtualenv

# create a virtual env
python -m venv virtualEnv 

# activate the virtual env
virtualEnv\Scripts\activate

# install project dependencies from requirement.txt
pip install -r requirements.txt
```

###2- in settings.py :

- **DEBUG** : should be set to False in production. You can set DJANGO_DEBUG environment variable to False and use it.
- **SECRET_KEY** : This is a large random value used for CSRF protection etc. It is important that the key used in production is not in source control or accessible outside the production server. The Django documents suggest that this might best be loaded from DJANGO_SECRET_KEY environment variable or read from a server-only file.


###3- Run prod server :

- unix:
  ``
  gunicorn FATARgmao.wsgi
  ``
- windows:
  ``
  waitress-serve --listen=*:8000 FATARgmao.wsgi:application  
  ``
