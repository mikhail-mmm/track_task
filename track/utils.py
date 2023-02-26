import json
import os

from representators import get_format_stat
from settings import STATISTICS_FILE
from typing import NewType

TimeDate = list[list[str | int]]


class UserData:
    project_name: str
    time: list[str | int]


def add_statistics(new_data: UserData) -> bool:
    if new_data.project_name == 'null':
        return False
    if is_file():
        data = read_from_file()
        if data:
            write_data = data_change(data, new_data.project_name, new_data.time)
            write_to_file(write_data)
        else:
            return False
    else:
        write_data = {}
        write_data[new_data.project_name] = [new_data.time]
        create_file(write_data)
    return True


def print_statistics(project_name: str, days: int) -> str:
    if is_file():
        data = read_from_file()
        if data:
            print_data = get_statistics(data, project_name, days)
            if print_data:
                return print_data
            else:
                return f'Project "{project_name}" statistics not found!'
        else:
            return f'{STATISTICS_FILE}: File read error!'
    else:
        return f'File {STATISTICS_FILE} not found!'


def data_change(data: dict[str, TimeDate], project_name: str, time: TimeDate) -> dict[str, TimeDate]:
    is_date = False
    if project_name in data:
        for el in data[project_name]:
            if el[0] == time[0]:
                el[1] += time[1]
                is_date = True
        if is_date is False:
            data[project_name].append(time)
    else:
        data[project_name] = [time]
    return data


def write_to_file(write_data: dict[str, TimeDate]) -> None:
    with open(STATISTICS_FILE, 'w') as file_json:
        json.dump(write_data, file_json)


def read_from_file() -> dict[str, TimeDate] | None:
    try:
        with open(STATISTICS_FILE, 'r') as file_json:
            data = json.load(file_json)
        return data
    except ValueError:
        return None


def create_file(write_data: dict[str, TimeDate]) -> None:
    with open(STATISTICS_FILE, 'w') as file_json:
        json.dump(write_data, file_json)


def get_statistics(
        data: dict[str, TimeDate],
        project_name: str,
        days: int,
) -> str | None:
    project_statistics = get_format_stat(data, project_name, days)
    return project_statistics if project_statistics else None


def is_file() -> bool:
    return True if os.path.isfile(STATISTICS_FILE) else False
