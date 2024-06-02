# Define connection parameters
DB_USER = 'root'
DB_PASSWORD = 'kiwiapple'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'books'
MYSQL_URL = f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}'
DB_URL = f'{MYSQL_URL}/{DB_NAME}'
