"""
Django settings for georiviere project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
import sys
from pathlib import Path

from georiviere import __version__
from geotrek import __version__ as __geotrek_version__

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

PROJECT_DIR = BASE_DIR / "georiviere"
VAR_DIR = BASE_DIR / 'var'

ROOT_URL = ""
TITLE = "Georivière"

VERSION = f"{__version__} based on geotrek {__geotrek_version__}"

SRID = 2154

SPATIAL_EXTENT = (105000, 6150000, 1100000, 7150000)
VIEWPORT_MARGIN = 0.1

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEST = 'test' in sys.argv

ALLOWED_HOSTS = os.getenv('SERVER_NAME').split(',')

# Application definition

INSTALLED_APPS = [
    'dal',
    'dal_select2',
    'dal_queryset_sequence',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'easy_thumbnails',
    'embed_video',
    'djgeojson',
    'django_filters',
    'compressor',
    'mapentity',  # mapentity should be placed after app declaring paperclip models
    'leaflet',
    'paperclip',
    'crispy_forms',
    'rest_framework',
    'modeltranslation',
    'geotrek.altimetry',
    'colorfield',
    'georiviere.main',
    'georiviere.river',
    'georiviere.description',
    'georiviere.knowledge',
    'georiviere.maintenance',
    'georiviere.observations',
    'georiviere.finances_administration',
    'georiviere.studies',
    'georiviere.proceeding',
    'geotrek.zoning',
    'georiviere.watershed',
    'geotrek.authent',
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)


PAPERCLIP_ATTACHMENT_MODEL = 'main.Attachment'
PAPERCLIP_FILETYPE_MODEL = 'main.FileType'

CRISPY_ALLOWED_TEMPLATE_PACKS = ('bootstrap', 'bootstrap3', 'bootstrap4')
CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'mapentity.middleware.AutoLoginMiddleware',
]

ROOT_URLCONF = 'georiviere.urls'

TEMPLATES = [
    {
        'BACKEND': 'djappypod.backend.OdtTemplates',
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            PROJECT_DIR / "templates",
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'mapentity.context_processors.settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'georiviere.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST', 'postgres'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    }
}

DATABASE_SCHEMAS = {}

ALTIMETRIC_PROFILE_PRECISION = 25  # Sampling precision in meters
ALTIMETRIC_PROFILE_AVERAGE = 2  # nb of points for altimetry moving average
ALTIMETRIC_PROFILE_STEP = 1  # Step min precision for positive / negative altimetry gain
ALTIMETRIC_PROFILE_BACKGROUND = 'white'
ALTIMETRIC_PROFILE_COLOR = '#F77E00'
ALTIMETRIC_PROFILE_HEIGHT = 400
ALTIMETRIC_PROFILE_WIDTH = 800
ALTIMETRIC_PROFILE_FONTSIZE = 25
ALTIMETRIC_PROFILE_FONT = 'ubuntu'
ALTIMETRIC_PROFILE_MIN_YSCALE = 1200  # Minimum y scale (in meters)
ALTIMETRIC_AREA_MAX_RESOLUTION = 150  # Maximum number of points (by width/height)
ALTIMETRIC_AREA_MARGIN = 0.15

BASE_INTERSECTION_MARGIN = 250

HIDDEN_FORM_FIELDS = {}
COLUMNS_LISTS = {}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = os.getenv('LANGUAGE_CODE', 'en-us')

TIME_ZONE = os.getenv('TZ', 'UTC')

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = VAR_DIR / "static"
MEDIA_ROOT = VAR_DIR / "media"
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    PROJECT_DIR / "static",
]

LANGUAGES = (
    ('en', 'English'),
    ('fr', 'French'),
)

MAPENTITY_CONFIG = {
    'TITLE': TITLE,
    'ROOT_URL': ROOT_URL,
    'CONVERSION_SERVER': 'http://{}:{}'.format(os.getenv('CONVERSION_HOST', 'convertit'),
                                               os.getenv('CONVERSION_PORT', '6543')),
    'CAPTURE_SERVER': 'http://{}:{}'.format(os.getenv('CAPTURE_HOST', 'screamshotter'),
                                            os.getenv('CAPTURE_PORT', '8000')),
    'SENDFILE_HTTP_HEADER': 'X-Accel-Redirect',
    'GEOJSON_PRECISION': 7,
    'TEMP_DIR': VAR_DIR / "tmp",
    'MAPENTITY_WEASYPRINT': False,
    'GPX_FIELD_NAME': 'geom_3d',
    'GEOJSON_LAYERS_CACHE_BACKEND': 'fat',
    'MAP_STYLES': {
        'city': {'weight': 4, 'color': '#FF9700', 'opacity': 0.3, 'fillOpacity': 0.0},
        'district': {'weight': 6, 'color': '#FF9700', 'opacity': 0.3, 'fillOpacity': 0.0, 'dashArray': '12, 12'},
        'restrictedarea': {'weight': 2, 'color': '#00008B', 'fillColor': '#1E90FF', 'opacity': 0.9, 'fillOpacity': 0.2},
        'watershed': {'weight': 2, 'color': '#aa0000', 'fillColor': '#aa0000', 'opacity': 0.9, 'fillOpacity': 0.2},
        'usage': {'weight': 4, 'color': '#F88017', 'opacity': 0.9},
        'morphology': {'weight': 4, 'color': 'brown', 'opacity': 0.9},
        'status': {'weight': 4, 'color': 'grey', 'opacity': 0.9},
        'land': {'weight': 4, 'color': '#b02a37', 'opacity': 0.9},
        'stream': {'weight': 4, 'color': 'blue', 'opacity': 0.9},
        'knowledge': {'weight': 4, 'color': '#198754', 'opacity': 0.9},
        'followup': {'weight': 4, 'color': '#fd7e14', 'opacity': 0.9},
        'intervention': {'weight': 4, 'color': 'red', 'opacity': 0.9},
        'station': {'weight': 4, 'color': '#FFD801', 'opacity': 0.9},
        'study': {'weight': 4, 'color': '#d63384', 'opacity': 0.9},
        'proceeding': {'weight': 4, 'color': '#3dd5f3', 'opacity': 0.9},
    }
}

LEAFLET_CONFIG = {
    'SRID': 3857,
    'TILES': [
        ('OSM', '//{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', '(c) OpenStreetMap Contributors'),
        ('OSM N&B', '//{s}.tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png', '(c) OpenStreetMap Contributors'),
    ],
    'SPATIAL_EXTENT': (-5, 40, 10, 55),
    'NO_GLOBALS': False,
    'PLUGINS': {
        'georiviere': {'js': ['river/js/source_location.js']},
        'topofields': {'js': ['river/js/georiviere.forms.snap.js',
                              'river/js/cut-topology.js'],
                       'css': ['river/css/cut-topology.css']}
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': os.getenv('MEMCACHED_URL', 'memcached:11211').replace('memcached://', ''),
    },
    'fat': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': VAR_DIR / "cache",
        'TIMEOUT': 28800,  # 8 hours
    }
}

PATHS_LINE_MARKER = 'dotL'
SNAP_DISTANCE = 30

ICON_SIZES = {
    'river_source': 18,
}

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

UPLOAD_DIR = 'upload'

API_SRID = 4326
LAYER_PRECISION_LAND = 4
LAYER_SIMPLIFY_LAND = 6
CACHE_TIMEOUT_LAND_LAYERS = 60 * 60 * 24

LAND_BBOX_CITIES_ENABLED = True
LAND_BBOX_DISTRICTS_ENABLED = True
LAND_BBOX_AREAS_ENABLED = True

AUTHENT_DATABASE = None
AUTHENT_TABLENAME = None
DEFAULT_STRUCTURE_NAME = os.getenv('DEFAULT_STRUCTURE', 'My structure')

#
# MAIL SETTINGS
# ..........................
DEFAULT_FROM_EMAIL = os.getenv('SERVER_EMAIL', 'root@localhost')
# address will be set for sent emails (ex: noreply@yourdomain.net)
SERVER_EMAIL = DEFAULT_FROM_EMAIL

EMAIL_HOST = os.getenv('EMAIL_HOST', 'localhost')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
EMAIL_PORT = os.getenv('EMAIL_HOST_PORT', 25)
EMAIL_USE_TLS = bool(os.getenv('EMAIL_USE_TLS', False))
EMAIL_USE_SSL = bool(os.getenv('EMAIL_USE_SSL', False))

if os.getenv('SSL_ENABLED', default=0):
    # SECURITY
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    CSRF_COOKIE_HTTPONLY = True
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Override with custom settings
custom_settings_file = os.getenv('CUSTOM_SETTINGS_FILE')
if custom_settings_file and os.path.exists(custom_settings_file) and not TEST:
    with open(custom_settings_file, 'r') as f:
        exec(f.read())
