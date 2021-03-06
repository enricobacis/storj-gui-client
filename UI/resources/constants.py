# -*- coding: utf-8 -*-

SAVE_PASSWORD_HASHED = True
MAX_RETRIES_DOWNLOAD_FROM_SAME_FARMER = 3
MAX_RETRIES_UPLOAD_TO_SAME_FARMER = 3
MAX_RETRIES_NEGOTIATE_CONTRACT = 1000
MAX_RETRIES_GET_FILE_POINTERS = 100

FILE_POINTERS_REQUEST_DELAY = 1
# int: file pointers request delay, in seconds.

MAX_DOWNLOAD_REQUEST_BLOCK_SIZE = 32 * 1024
MAX_UPLOAD_REQUEST_BLOCK_SIZE = 4096
MAX_UPLOAD_CONNECTIONS_AT_SAME_TIME = 4
MAX_DOWNLOAD_CONNECTIONS_AT_SAME_TIME = 4
CONCURRENT_UPLOADING = False

DEFAULT_MAX_BRIDGE_REQUEST_TIMEOUT = 5
DEFAULT_MAX_FARMER_CONNECTION_TIMEOUT = 7
# int: maximum bridge request timeout, in seconds.

DEFAULT_BRIDGE_API_URL = 'api.storj.io'

# DESIGN
DISPLAY_FILE_CREATION_DATE_IN_MAIN = True
FILE_LIST_SORTING_MAIN_ENABLED = True

# PATHS
USE_USER_ENV_PATH_FOR_TEMP = True
