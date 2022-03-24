import os
import mysql.connector
from mysql.connector.constants import ClientFlag

# Instance name - flash-hour-338103:asia-south1:test-sql-server

config = {
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASSWORD'),
    'host': '35.200.140.194',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': os.environ.get('SSL_CA'),
    'ssl_cert': os.environ.get('SSL_CERT'),
    'ssl_key': os.environ.get('SSL_KEY'),
    'database': os.environ.get('DB_NAME'),
}

GET_BOARDS = 'SELECT Id FROM Boards'

INSERT_CUSTOM_FIELD = 'INSERT INTO CustomFields (' \
                      'Id, BoardId, Name, Type) ' \
                      'VALUES (%s, %s, %s, %s) ' \
                      'ON DUPLICATE KEY UPDATE ' \
                      'BoardId = VALUES(BoardId),' \
                      'Name = VALUES(Name),' \
                      'Type = VALUES(Type);'

INSERT_CUSTOM_FIELD_OPTION = 'INSERT INTO CustomFieldOptions (' \
                             'Id, IdCustomField, CustomFieldValue) ' \
                             'VALUES (%s, %s, %s) ' \
                             'ON DUPLICATE KEY UPDATE ' \
                             'IdCustomField = VALUES(IdCustomField),' \
                             'CustomFieldValue = VALUES(CustomFieldValue);'


class DatabaseConnector:
    def __init__(self):
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def get_boards(self):
        self.cursor.execute(GET_BOARDS)
        return self.cursor.fetchall()

    def insert_custom_fields(self, values: list):
        self.cursor.executemany(INSERT_CUSTOM_FIELD, values)
        self.connection.commit()

    def insert_custom_field_options(self, values: list):
        self.cursor.executemany(INSERT_CUSTOM_FIELD_OPTION, values)
        self.connection.commit()


database_connection = DatabaseConnector()
