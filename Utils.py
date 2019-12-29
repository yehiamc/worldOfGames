import os

ERROR_MESSAGE = "Something went wrong.."
SCORES_FILE_NAME = "/Users/yehiamc/Desktop/Scores.txt"


def error_message():
    return ERROR_MESSAGE


def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')