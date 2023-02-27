from datetime import date, timedelta


def get_format_stat(data: dict[str, list[list[str | int]]], project_name: str, days: int) -> str | None:
    dates = get_dates(days)
    project_statistics = ''
    if project_name in data:
        for stat in data[project_name]:
            if stat[0] in dates:
                time = get_format_time(int(stat[1]))
                project_statistics += f'{stat[0]} {time}\n'
        return project_statistics or None


def get_dates(days: int) -> list[str]:
    dates = []
    for delta in range(days):
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
