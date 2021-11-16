from .settings import *

TEST_RUNNER = 'humanscape.test_runner.TestRunner'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'test_db.sqlite3',
    }
}