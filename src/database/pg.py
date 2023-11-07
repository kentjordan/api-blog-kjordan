import os
import psycopg2.extras as pg_extras
import psycopg2 as pg

pg_extras.register_uuid()

__DB_HOST_ADRESS = os.getenv('DB_HOST_ADRESS')
__DB_HOST_PORT = os.getenv('DB_HOST_PORT')
__DB_USER = os.getenv('DB_USER')
__DB_PASSWORD = os.getenv('DB_PASSWORD')
__DB_NAME = os.getenv('DB_NAME')

connection = pg.connect(dsn=f'host={__DB_HOST_ADRESS} port={
    __DB_HOST_PORT} user={__DB_USER} password={__DB_PASSWORD} dbname={__DB_NAME}')
