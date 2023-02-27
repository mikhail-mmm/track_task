import os
import json

from settings import STATISTICS_FILE


def write_to_file(write_data: dict[str, list[list[str | int]]]) -> None:
    with open(STATISTICS_FILE, 'w') as file_json:
        json.dump(write_data, file_json)


def read_from_file() -> dict[str, list[list[str | int]]] | None:
    try:
        with open(STATISTICS_FILE, 'r') as file_json:
            data = json.load(file_json)
        return data
    except ValueError:
        return None


def create_file(write_data: dict[str, list[list[str | int]]]) -> None:
    with open(STATISTICS_FILE, 'w') as file_json:
        json.dump(write_data, file_json)


def is_file() -> bool:
    return True if os.path.isfile(STATISTICS_FILE) else False
