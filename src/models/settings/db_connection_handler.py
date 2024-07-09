import sqlite3
from sqlite3 import Connection
import datetime

# Adaptador para converter datetime para string
def adapt_datetime(ts):
    return ts.strftime('%Y-%m-%d %H:%M:%S')

# Conversor para converter string para datetime
def convert_datetime(s):
    return datetime.datetime.strptime(s.decode('utf-8'), '%Y-%m-%d %H:%M:%S')

# Registrar o adaptador e o conversor
sqlite3.register_adapter(datetime.datetime, adapt_datetime)
sqlite3.register_converter('timestamp', convert_datetime)

class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "storage.db"
        self.__conn = None

    def connect(self) -> None:
        # Conectar ao banco de dados SQLite com a detecção de tipos habilitada
        conn = sqlite3.connect(
            self.__connection_string, 
            check_same_thread=False, 
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        self.__conn = conn

    def get_connection(self) -> Connection:
        return self.__conn

# Cria uma instância da classe DBConnectionHandler
db_connection_handler = DBConnectionHandler()
