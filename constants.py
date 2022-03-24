import os

GOOGLE_DOC_LINK = 'https://docs.google.com/document/d/[DOC_ID]/edit'


API_KEY = os.environ.get("TRELLO_API_KEY")
AUTH_TOKEN = os.environ.get("TRELLO_TOKEN")
PARAMS = {
    "key": API_KEY,
    "token": AUTH_TOKEN,
}
HEADERS = {
    "Accept": "application/json"
}

BOARD_ID_TEAM_ALPHA = '6191c991ee98d37c936d4099'
BOARD_ID_TEAM_BETA = '61eba0d2c21c0c191f4d021e'
BOARD_ID_EDITOR_ALPHA = '619c71771deda242e027685e'
PROOFREADING_LIST_EDITOR_ALPHA = '61e819cda4422b71873dd7f7'
BOARD_ID_EDITOR_BETA = '61ed0fd94bf5051e2602d02c'
PROOFREADING_LIST_EDITOR_BETA = '61ed0fe3d70a94477f001b6e'


# Date Time Related Things
DATE_FORMAT = '%Y-%m-%d'
