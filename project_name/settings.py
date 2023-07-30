#Django

#System
from pathlib import Path
import os
#Third Party
import dj_database_url
#Custom
from EnvVarReader.env_var_reader import Secrets


secrets = Secrets("ENV_VARS.json")

SECRET_KEY = secrets.getSecret("SECRET_KEY")


DEBUG = True 

# FOR PRODUCTION
# -------------------
# Set DEBUG to False 
# Set database (migrate if necessary)
# Adjust the settings at the bottom of this file 
# -------------------

BASE_DIR = Path(__file__).resolve().parent.parent



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
    'whitenoise.middleware.WhiteNoiseMiddleware', #used to serve static files in production
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
        'DIRS': [os.path.join(BASE_DIR, '{{ project_name }}/templates/')],
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
    #     'NAME': secrets.getSecret('DATABASE_NAME'),
    #     'USER': secrets.getSecret('DATABASE_USERNAME'),
    #     'PASSWORD': secrets.getSecret('DATABASE_PASSWORD'),
    #     'HOST': '127.0.0.1',
    #     'PORT': '3306',
    # }

    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': secrets.getSecret('DATABASE_NAME'), 
    #     'USER': secrets.getSecret('DATABASE_USERNAME'), 
    #     'PASSWORD': secrets.getSecret('DATABASE_PASSWORD),
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

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SESSION_ENGINE = "django.contrib.sessions.backends.file"

SESSION_FILE_PATH = os.path.join(BASE_DIR, 'SessionFiles')

#Static AND Media

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'bootstrap'),
]

MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media'


# SETTINGS for Production -----------------------------------------------------------------
if (DEBUG == False):

    ALLOWED_HOSTS = ['*']

    STATIC_ROOT = os.path.join( BASE_DIR, 'static_root' )

    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

    CSRF_COOKIE_SECURE = True

    SESSION_COOKIE_SECURE = True

