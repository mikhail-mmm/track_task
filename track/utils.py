from file_handling import is_file, read_from_file, write_to_file, create_file
from parser_value import TrackValue, StatValue
from representators import get_format_stat
from settings import STATISTICS_FILE


def add_statistics(track_data: TrackValue) -> None:
    if is_file():
        data = read_from_file()
        if data:
            write_data = statistics_update(data, track_data.project_name, track_data.time)
            write_to_file(write_data)
        else:
            print_response(f'{STATISTICS_FILE}: File read error!')
    else:
        write_data = {}
        write_data[track_data.project_name] = [track_data.time]
        create_file(write_data)


def get_statistics(stat_data: StatValue) -> None:
    if is_file():
        data = read_from_file()
        if data:
            project_statistics = get_format_stat(data, stat_data.project_name, stat_data.days)
            if project_statistics:
                print_response(project_statistics)
            else:
                print_response(f'Project "{stat_data.project_name}" statistics not found!')
        else:
            print_response(f'{STATISTICS_FILE}: File read error!')
    else:
        print_response(f'File {STATISTICS_FILE} not found!')


def statistics_update(
        data: dict[str, list[list[str | int]]],
        project_name: str,
        time: list[list[str | int]],
) -> dict[str, list[list[str | int]]]:
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


def is_required_attributes(subparser: str, project_name: str, days: int | None = None) -> bool:
    if subparser == 'track':
        if project_name is None:
            print_response('Please enter -p/--project=<project_name>')
            return False
    elif subparser == 'stat':
        if project_name is None:
            print_response('Please enter -p/--project=<project_name>')
            return False
        if days is None:
            print_response('Please enter -d/--days=<amount_of_days>')
            return False
    return True


def print_response(response: str) -> None:
    print(response)
