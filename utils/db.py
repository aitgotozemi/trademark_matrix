import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()

_required = ['DB_HOST', 'DB_PORT', 'DB_NAME', 'DB_USER', 'DB_PASSWORD']
_missing = [k for k in _required if not os.getenv(k)]
if _missing:
    raise EnvironmentError(f'.env に以下のキーが見つかりません: {_missing}')

DB_CONFIG = {
    'host':     os.environ['DB_HOST'],
    'port':     int(os.environ['DB_PORT']),
    'dbname':   os.environ['DB_NAME'],
    'user':     os.environ['DB_USER'],
    'password': os.environ['DB_PASSWORD'],
}


def get_conn() -> psycopg2.extensions.connection:
    return psycopg2.connect(**DB_CONFIG)
