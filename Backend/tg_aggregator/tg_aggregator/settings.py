# settings.py

import os
from pathlib import Path
# Убедитесь, что вы установили python-dotenv: pip install python-dotenv
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --- ЗАГРУЗКА ПЕРЕМЕННЫХ ОКРУЖЕНИЯ ---
# Ищем файл .env в корневой папке проекта (рядом с manage.py) и загружаем переменные из него
load_dotenv(BASE_DIR / '.env')


# --- КЛЮЧЕВЫЕ НАСТРОЙКИ БЕЗОПАСНОСТИ ---

# Читаем секретный ключ из окружения. ОБЯЗАТЕЛЬНО для продакшена.
# os.environ.get() безопасно вернет None, если переменная не найдена.
SECRET_KEY = os.environ.get('SECRET_KEY')

# Читаем режим отладки. На хостинге эта переменная будет 'False'.
DEBUG = os.environ.get('DEBUG') == 'True'

# Читаем разрешенные хосты из строки, разделенной запятыми.
# Например: "mysite.onrender.com,127.0.0.1"
allowed_hosts_str = os.environ.get('ALLOWED_HOSTS', '')
ALLOWED_HOSTS = [host.strip() for host in allowed_hosts_str.split(',') if host.strip()]


# --- TELEGRAM API КЛЮЧИ ---
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
TELEGRAM_API_ID = os.environ.get('TELEGRAM_API_ID')
TELEGRAM_API_HASH = os.environ.get('TELEGRAM_API_HASH')
TELEGRAM_SESSION_NAME = 'telegram_session'


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'aggregator_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tg_aggregator.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'tg_aggregator.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ... (AUTH_PASSWORD_VALIDATORS остаются без изменений) ...

# Internationalization
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
# Папка, куда Django будет собирать все статические файлы для продакшена
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files (User-uploaded files)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- НАСТРОЙКИ CORS ДЛЯ ПРОДАКШЕНА ---
# Читаем разрешенные домены для CORS из переменной окружения
cors_allowed_origins_str = os.environ.get('CORS_ALLOWED_ORIGINS', '')
CORS_ALLOWED_ORIGINS = [origin.strip() for origin in cors_allowed_origins_str.split(',') if origin.strip()]

# Если мы в режиме отладки, можно разрешить все домены для удобства
if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_CREDENTIALS = True