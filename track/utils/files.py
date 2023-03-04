import os
import json

from track.settings.parser_value import TrackData, JsonData
from track.settings.settings import STATISTICS_FILEPATH


def write_to_file(write_data: TrackData | JsonData, filepath: str = STATISTICS_FILEPATH) -> None:
    with open(filepath, 'w') as file_json:
        json.dump(write_data, file_json)


def read_from_file(filepath: str = STATISTICS_FILEPATH) -> JsonData | None:
    try:
        with open(filepath, 'r') as file_json:
            data = json.load(file_json)
        return data
    except ValueError:
        return None


def create_file(write_data: JsonData, filepath: str = STATISTICS_FILEPATH) -> None:
    with open(filepath, 'w') as file_json:
        json.dump(write_data, file_json)


def is_file(filepath: str = STATISTICS_FILEPATH) -> bool:
    return os.path.isfile(filepath)
