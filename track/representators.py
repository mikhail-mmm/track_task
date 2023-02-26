from datetime import date, timedelta
from utils import TimeDate


def get_format_stat(data: dict[str, TimeDate], project_name: str, days: int) -> str | None:
    dates = get_date_str_list(days)
    project_statistics = ''
    if project_name in data:
        for stat in data[project_name]:
            if stat[0] in dates:
                project_statistics += f'{stat[0]} {get_format_time(int(stat[1]))}\n'
        if project_statistics:
            return project_statistics
        else:
            return None


def get_format_date(days: int) -> list[str]:
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


def get_date_str_list(days: int) -> list[str]:
    date_str_list = get_format_date(days)
    return date_str_list
