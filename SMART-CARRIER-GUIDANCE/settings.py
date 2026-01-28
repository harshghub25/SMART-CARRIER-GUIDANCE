from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------- SECURITY ----------------
SECRET_KEY = 'django-insecure-12345'
DEBUG = True

ALLOWED_HOSTS = []


# ---------------- APPLICATIONS ----------------
INSTALLED_APPS = [
    "jazzmin",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    'accounts',
    'student',
]


# ---------------- MIDDLEWARE ----------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]


# ---------------- URL & TEMPLATES ----------------
ROOT_URLCONF = 'SMART-CARRIER-GUIDANCE.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],   # global templates (home, base)
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


# ---------------- DATABASE ----------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ---------------- PASSWORD VALIDATION ----------------
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


# ---------------- STATIC FILES ----------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]


# ---------------- DEFAULTS ----------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ---------------- AUTH FLOW (VERY IMPORTANT) ----------------
LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'student:onboarding'
LOGOUT_REDIRECT_URL = 'accounts:login'

JAZZMIN_SETTINGS = {
    "site_title": "Smart Career Admin",
    "site_header": "Smart Career Guidance",
    "site_brand": "CareerGuide",
    "welcome_sign": "Welcome to Admin Dashboard",
    "copyright": "CareerGuide",
    "search_model": ["auth.User", "student.StudentProfile"],
    "topmenu_links": [
        {"name": "Home", "url": "/", "permissions": ["auth.view_user"]},
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
}
