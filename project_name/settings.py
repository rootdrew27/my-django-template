from pathlib import Path
import os
import json
from django.core.exceptions import ImproperlyConfigured

# For Production
# -------------------
# Set DEBUG to False 
# Set database (migrate if necessary
# )
# Adjust the settings at the bottom of this file 
# -------------------
DEBUG = True


with open("ENV_VARS.json") as f:
    secrets = json.loads(f.read())

def getSecret(setting, secrets=secrets):
    """Get the secret variable or return explicit exception."""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = getSecret("SECRET_KEY")

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = '{{ project_name }}.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['{{ project_name }}/templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = '{{ project_name }}.wsgi.application' 

import dj_database_url

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }

    # 'default': {
    #     dj_database_url.config(
    #         default=dj_database_url.parse(os.environ.get("DATABASE_URL")),
    #         conn_max_age=600
    #     )
    # }

    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': '',
    #     'USER': 'root',
    #     'PASSWORD': getSecret('DATABASE_PASSWORD'),
    #     'HOST': '127.0.0.1',
    #     'PORT': '3306',
    # }

    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': '', 
    #     'USER': 'root', 
    #     'PASSWORD': getSecret('DATABASE_PASSWORD),
    #     'HOST': '127.0.0.1', 
    #     'PORT': '5432',
    # }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_DIR = []

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SESSION_ENGINE = "django.contrib.sessions.backends.file"

SESSION_FILE_PATH = os.path.join(BASE_DIR, 'SessionFiles')



# SETTINGS for Production
if (DEBUG == False):

    ALLOWED_HOSTS = []

    STATIC_ROOT = os.path.join( BASE_DIR, 'static_root' )

    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

    CSRF_COOKIE_SECURE = True

    SESSION_COOKIE_SECURE = True

