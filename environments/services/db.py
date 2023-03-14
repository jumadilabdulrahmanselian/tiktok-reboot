import psycopg2, requests
import configparser
from psycopg2.extras import DictCursor
from colorama import Fore, Style

class DB:
    host: None
    user: None
    password: None
    database: None
    schema: None
    port: 5432
    connect = None
    pgPath = None

    def __init__(self) -> None:
        config = configparser.ConfigParser()
        config_path = 'config.ini'
        config.read(config_path, encoding='utf-8')
        self.host = config.get('Database', 'host')
        self.user = config.get('Database', 'user')
        self.password = config.get('Database', 'pass')
        self.database = config.get('Database', 'database')
        self.schema = config.get('Database', 'schema')
        self.port = config.get('Database', 'port')
        self.pgPath = config.get('Database', 'path')

    def Connect(self):
        try:
            self.connect = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port,
                options="-c search_path=dbo,"+self.schema
            )
            return self.connect
        except (Exception) as error:
            print("Failed to connect to Database", error)

    def Cursor(self, ):
        # cursor_factory=NamedTupleCursor
        return self.Connect().cursor(cursor_factory=DictCursor)