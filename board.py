import requests
import constants
from custom_field import CustomField


class Board:
    all_boards = []

    def __init__(self, board_id):
        self.id = board_id
        self.url = f'https://api.trello.com/1/boards/{board_id}/'
        Board.all_boards.append(self)

    @staticmethod
    def instantiate_from_db_list(db_list: list):
        for row in db_list:
            Board(row[0])

        for brd in Board.all_boards:
            fields_json = brd.get_custom_fields_in_board()
            CustomField.instantiate_from_json(fields_json, brd.id)

    def get_lists_in_board(self):
        url = self.url + 'lists'
        response = requests.request(
            "GET",
            url,
            headers=constants.HEADERS,
            params=constants.PARAMS
        )
        print(response.text)

    def get_custom_fields_in_board(self):
        url = self.url + 'customFields'
        response = requests.request(
            "GET",
            url,
            headers=constants.HEADERS,
            params=constants.PARAMS
        )
        return response.json()

    def get_members_in_board(self):
        url = self.url + 'members'
        response = requests.request(
            "GET",
            url,
            headers=constants.HEADERS,
            params=constants.PARAMS
        )
        return response.json()
