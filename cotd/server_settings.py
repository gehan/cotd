DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'cotd_db',                      # Or path to database file if using sqlite3.
        'USER': 'cotd',                      # Not used with sqlite3.
        'PASSWORD': 'tarynsam',                  # Not used with sqlite3.
        'HOST': 'mysql.captainoftheday.com', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

MEDIA_ROOT = '/home/gehan/captainoftheday.com/public/media'