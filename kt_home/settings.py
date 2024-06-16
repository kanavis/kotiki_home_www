"""
Django settings for kt_home project.
"""
from .system_settings import *

SECRET_KEY = 'django-insecure-i_edcn6c@+hcxmsz!hf8fm@29on0ika)1#p@6h8w***fon&v_r'
DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Berlin'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
