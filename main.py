from board import Board
from custom_field import CustomField
from custom_field_option import CustomFieldOption
from database import database_connection


def main(data, context):
    Board.instantiate_from_db_list(database_connection.get_boards())

    database_connection.insert_custom_fields(CustomField.convert_all_to_list())
    database_connection.insert_custom_field_options(CustomFieldOption.convert_all_to_list())

    database_connection.connection.close()


if __name__ == '__main__':
    main('', '')
