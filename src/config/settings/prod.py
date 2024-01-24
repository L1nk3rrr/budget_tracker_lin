from config.settings.base import *  # NOQA

SECRET_KEY = "django-insecure-k4r%kk1z2pmmeh1+ov$p^)3mchk^4ybb9(!$*(%(j+^anol)ca"

DEBUG = False

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
