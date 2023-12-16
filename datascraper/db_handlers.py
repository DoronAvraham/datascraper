import os
import psycopg2

__DB_HOST_KEY = "DB_HOST"
__DB_NAME = "my_cocktails_bar"
__DB_PASSWORD_KEY = "DB_PASSWORD"
__DB_USER_KEY = "DB_USER"

def handler_postgresql(database = __DB_NAME, user = None, password = None, host = None):
    return psycopg2.connect(database = database,
                        user = user or os.environ.get(__DB_USER_KEY),
                        password = password or os.environ.get(__DB_PASSWORD_KEY),
                        host = host or os.environ.get(__DB_HOST_KEY))
