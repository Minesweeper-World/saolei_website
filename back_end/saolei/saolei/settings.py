# -*- coding: utf-8 -*-
"""
Django settings for saolei project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-3_(yjnup(rsxz&pd@stz25*meq10bn3m3$lt!n_1+s723#k=ay"

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
# ALLOWED_HOSTS = ["*"]
DEBUG = True
ALLOWED_HOSTS = ["*"]

# 自定义404、500错误页面
# handler404 = 'fault_page.views.page_not_found'
# handler500 = 'fault_page.views.server_error'

# Application definition

INSTALLED_APPS = [
    "captcha",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django_apscheduler',
    'corsheaders',
    'userprofile',
    'videomanager',
    'msuser',
    'django_cleanup.apps.CleanupConfig', # 必须放在最后(文档所言)
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.csrf.CsrfViewMiddleware",
    'corsheaders.middleware.CorsMiddleware',   # 允许跨域请求
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'django_ratelimit.middleware.RatelimitMiddleware',
]

ROOT_URLCONF = "saolei.urls"

RATELIMIT_VIEW = "utils.ratelimited"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [BASE_DIR / 'dist', BASE_DIR / 'templates'],

        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "dist/"), # ????dist?都一样
]

WSGI_APPLICATION = "saolei.wsgi.application"

SECURE_CONTENT_TYPE_NOSNIFF = False

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "saolei",
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "127.0.0.1",
        #'HOST': 'mysql',   # docker-compose 中的服务名称
        "PORT": "3306",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# STATIC_URL = "static/"
STATIC_URL = "/static/"
# STATIC_URL = "/"
STATIC_ROOT = os.path.join(BASE_DIR, '/root/saolei/static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '/root/saolei/media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"



# 格式
CAPTCHA_OUTPUT_FORMAT = u'%(text_field)s %(hidden_field)s %(image)s'
# 噪点样式
CAPTCHA_NOISE_FUNCTIONS = (
    # 'captcha.helpers.noise_null',       # 没有样式
    # 'captcha.helpers.noise_arcs',     # 线
    'captcha.helpers.noise_dots',       # 点
)
# 图片大小
CAPTCHA_IMAGE_SIZE = (100, 30)
# 字符个数
CAPTCHA_LENGTH = 4
# 超时(minutes)
CAPTCHA_TIMEOUT = 15
# 文字倾斜
CAPTCHA_LETTER_ROTATION = (-10,10)
# 背景颜色
CAPTCHA_BACKGROUND_COLOR = '#FFFFFF'
# 文字颜色
CAPTCHA_FOREGROUND_COLOR = '#0A12E5'
# 验证码类型
# 图片中的文字为随机英文字母，如 mdsh
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'
# 图片中的文字为数字表达式，如 1+2=
# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'


CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_HEADERS = ('*')
CSRF_TRUSTED_ORIGINS = ['http://localhost:8080']

# 开发时
SESSION_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SECURE = True  # https时候改成True
CSRF_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_SECURE = True     # https时候改成True
# 部署时
# SESSION_COOKIE_SAMESITE = 'Lax'
# SESSION_COOKIE_SECURE = False  # https时候改成True
# CSRF_COOKIE_SAMESITE = 'Lax'
# CSRF_COOKIE_SECURE = False     # https时候改成True

# 发送邮箱验证码
EMAIL_HOST = "smtp.88.com"     # 服务器
EMAIL_PORT = 25                 # 一般情况下都为25
EMAIL_HOST_USER = "wangjianing@88.com"     # 账号
EMAIL_HOST_PASSWORD = "TdS2ZPt2izAkY25b"   # 密码 (注意：这里的密码指的是授权码)
# EMAIL_USE_SSL = True
# EMAIL_FROM = "wangjianing@88.com"      # 邮箱来自

SESSION_COOKIE_NAME = "session_id"        # Session的cookie保存在浏览器上时的key
SESSION_COOKIE_PATH = "/"                # Session的cookie保存的路径(默认)
SESSION_COOKIE_DOMAIN = None             # Session的cookie保存的域名(默认)
# SESSION_COOKIE_SECURE = False            # 是否Https传输cookie
SESSION_COOKIE_HTTPONLY = True           # 是否Session的cookie只支持http传输(默认)
SESSION_COOKIE_AGE = 1209600*2           # Session的cookie失效日期(默认2周)
SESSION_SAVE_EVERY_REQUEST = False       # 是否设置关闭浏览器使得Session过期
SESSION_COOKIE_AT_BROWSER_CLOSE = False  # 是否每次请求都保存Session，默认修改之后才能保存

AUTH_USER_MODEL='userprofile.UserProfile'

CACHES = {
    "saolei_website": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "SOCKET_CONNECT_TIMEOUT": 5,  # 连接redis超时时间，单位为秒
            "SOCKET_TIMEOUT": 5,  # redis读写操作超时时间，单位为秒
            # "CONNECTION_POOL_KWARGS": {"decode_responses": True,"encoding": "utf-8"},
        }
    },
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "SOCKET_CONNECT_TIMEOUT": 5,  # 连接redis超时时间，单位为秒
            "SOCKET_TIMEOUT": 5,  # redis读写操作超时时间，单位为秒
        }
    }
}
# 会话存储方式二选一
# SESSION_ENGINE = "django.contrib.sessions.backends.db"
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "saolei_website"


APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a" # 定时任务格式
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # 定时任务最大执行时间，秒

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
        "default": {
            "format": '%(asctime)s %(name)s  %(pathname)s:%(lineno)d %(module)s:%(funcName)s '
                      '%(levelname)s- %(message)s',
            "datefmt": "%Y-%m-%d %H:%M:%S"
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/debug.log'),
            'when': "D",
            'interval': 1,
            'formatter': 'default'
        },
        "request": {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/request.log'),
            'formatter': 'default'
        },
        "server": {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/server.log'),
            'formatter': 'default'
        },
        "root": {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/root.log'),
            'formatter': 'default'
        }
    },
    'loggers': {
        # 应用中自定义日志记录器
        'videomanager': {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
            'propagate': True,
        }
    },
    'root': {
        "level": "DEBUG",
        "handlers": ["root"],
    }
}

SETTINGS_PATH = os.path.normpath(os.path.dirname(__file__))
TEMPLATE_DIRS = (
os.path.join(SETTINGS_PATH, 'templates'),
)




