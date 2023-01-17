import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default': {
    'ENGINE': 'django.db.backends.sqlite',
    'NAME': os.path.join(BASE_DIR,'db/sqlite/db.sqlite3'),
    }
}

MYSQL = {
    
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bd',
        'USER':'user',
        'PASSWORD': 'root',
        'HOST': '192.168.110.47',
        'PORT':'3306'
    }
    
}
