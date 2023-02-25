import json
import os

from datetime import date, timedelta
from settings import FILE_NAME
from typing import Any

TimeDate = list[list[str | int]]


def add_statistics(project_name: str, time: list[str | int]) -> str:
    if project_name == 'null':
        return 'Enter project name! (-p/--project=<project_name>)'
    statistics = {}
    statistics[project_name] = [time]
    if os.path.isfile(FILE_NAME):
        write_to_file(project_name, time)
    else:
        create_file(statistics)
    return 'Complete!'


def print_statistics(project_name: str, days: int) -> str:
    if os.path.isfile(FILE_NAME):
        data = read_from_file()
        return get_statistics(data, project_name, days)
    else:
        return f'Project "{project_name}" statistics not found!'


def write_to_file(project_name: str, time: list[str | int]) -> None:
    data = read_from_file()
    is_date = False
    try:
        for el in data[project_name]:
            if el[0] == time[0]:
                el[1] += time[1]
                is_date = True
        if is_date is False:
            data[project_name].append(time)
    except KeyError:
        data[project_name] = [time]
    with open(FILE_NAME, 'w') as f:
        json.dump(data, f)


def read_from_file() -> Any:
    with open(FILE_NAME, 'r') as f:
        data = json.load(f)
    return data


def create_file(statistics: dict[str, TimeDate]) -> None:
    with open(FILE_NAME, 'w') as f:
        json.dump(statistics, f)


def get_statistics(
        data: dict[str, TimeDate],
        project_name: str,
        days: int,
) -> str:
    dates = get_date_list(days)
    project_statistics = ''
    try:
        for stat in data[project_name]:
            if stat[0] in dates:
                project_statistics += f'{stat[0]} {get_format_time(int(stat[1]))}\n'
        if project_statistics:
            return project_statistics
        else:
            return f'Project "{project_name}" statistics not found!'
    except KeyError:
        return f'Project "{project_name}" statistics not found!'


def get_date_list(days: int) -> list[str]:
    dates = []
    for delta in range(0, days):
        date_str = (date.today() - timedelta(days=delta)).strftime("%d.%m.%y")
        dates.append(date_str)
    return dates


def get_format_time(minutes: int) -> str:
    if minutes < 60:
        return f'{minutes}m'
    else:
        hours = minutes // 60
        minutes_remainder = minutes % 60
        return f'{hours}h {minutes_remainder}m'
