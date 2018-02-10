# coding: utf-8
import os
from configurations import Configuration
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Base(Configuration):

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'X'  # TODO: to change before deployment

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True
    DEBUG_TOOLBAR_PATCH_SETTINGS = False
    INTERNAL_IPS = ['127.0.0.1']
    ALLOWED_HOSTS = ['*']

    # Application definition
    INSTALLED_APPS = [
        # Default
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        # Requirements
        'pytz',
        'oauth2_provider',
        'social_django',
        'corsheaders',
        'rest_framework',
        'rest_framework.authtoken',
        'common',
        # Applications
        'healthyapp',
        'healthyfood',
        # Debug
        'debug_toolbar',
    ]

    MIDDLEWARE = [
        # CORS Headers
        'corsheaders.middleware.CorsMiddleware',
        # Debug
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        # Default
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        # Social
        'social_django.middleware.SocialAuthExceptionMiddleware',
    ]

    ROOT_URLCONF = 'healthylab.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    # Social
                    'social_django.context_processors.backends',
                    'social_django.context_processors.login_redirect',
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'healthylab.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/2.0/ref/settings/#databases
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

    # Authentication backends
    AUTHENTICATION_BACKENDS = (
        'social_core.backends.open_id.OpenIdAuth',
        'social_core.backends.google.GoogleOpenId',
        'social_core.backends.google.GoogleOAuth2',
        'social_core.backends.google.GoogleOAuth',
        'social_core.backends.facebook.FacebookAppOAuth2',
        'social_core.backends.facebook.FacebookOAuth2',
        'social_core.backends.instagram.InstagramOAuth2',
        'social_core.backends.twitter.TwitterOAuth',
        'django.contrib.auth.backends.ModelBackend',
    )

    # Password validation
    # https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
    AUTH_PASSWORD_VALIDATORS = [
        # {
        #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        # },
        # {
        #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        # },
        # {
        #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        # },
        # {
        #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        # },
    ]

    # Internationalization
    # https://docs.djangoproject.com/en/2.0/topics/i18n/
    LANGUAGE_CODE = 'fr-fr'
    TIME_ZONE = 'Europe/Paris'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    LANGUAGES = (
        ('fr', _('Français')),
        ('en', _('English')),
    )

    LOCALE_PATHS = (
        os.path.join(BASE_DIR, 'locale'),
    )

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.0/howto/static-files/
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'statics'),
    )

    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'django.contrib.staticfiles.finders.FileSystemFinder',
    )

    # Media url and directory
    MEDIA_NAME = 'medias'
    MEDIA_URL = '/medias/'
    MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_NAME)

    # Custom settings
    CELERY_ENABLE = False
    CORS_ORIGIN_ALLOW_ALL = True
    APPEND_SLASH = True

    # Django REST Framework configuration
    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.IsAuthenticated',
        ),
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.TokenAuthentication',
            'rest_framework.authentication.SessionAuthentication',
            'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        ),
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
            'rest_framework.renderers.AdminRenderer',
        ),
        'DEFAULT_PARSER_CLASSES': (
            'rest_framework.parsers.JSONParser',
            'rest_framework.parsers.FormParser',
            'rest_framework.parsers.MultiPartParser',
            'rest_framework.parsers.FileUploadParser',
            'rest_framework_xml.parsers.XMLParser',
        ),
        'DEFAULT_PAGINATION_CLASS': 'common.api.pagination.CustomPageNumberPagination',
        'PAGE_SIZE': 10,
        'TEST_REQUEST_DEFAULT_FORMAT': 'json',
        'COERCE_DECIMAL_TO_STRING': True,
        'HYPERLINKED': True,
    }

    # Login URLs
    LOGIN_URL = '/login/'
    LOGIN_REDIRECT_URL = '/'

    # User substitution
    AUTH_USER_MODEL = 'healthyapp.Profile'

    # Messages
    MESSAGE_TAGS = {
        messages.DEBUG: 'light',
        messages.INFO: 'info',
        messages.SUCCESS: 'success',
        messages.WARNING: 'warning',
        messages.ERROR: 'danger',
    }
    CSS_CLASSES = {
        (1, 1): 'info',
        (1, 0): 'success',
        (0, 0): 'warning',
        (0, 1): 'danger',
    }
