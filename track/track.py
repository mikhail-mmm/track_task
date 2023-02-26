import argparse

from dataclasses import dataclass
from datetime import date
from utils import add_statistics, print_statistics


@dataclass(frozen=True, kw_only=True)
class UserData:
    project_name: str
    time: list[str | int]


def start_track(args: argparse.Namespace) -> None:
    new_data = UserData(
        project_name=args.name_project,
        time=[date.today().strftime("%d.%m.%y"), args.n],
    )
    if add_statistics(new_data):
        print('Complete!')
    else:
        print('Enter project name! (-p/--project=<project_name>)')


def start_stat(args: argparse.Namespace) -> None:
    print(print_statistics(args.name_project, args.days))


def parsing() -> tuple(argparse.Namespace, list[str]):
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title='subcommands', help='log time or print statistic')

    track_parser = subparsers.add_parser('track', help='tracking project work time')
    track_parser.add_argument('-p', '--project', dest='name_project', help='project name')
    track_parser.add_argument('n', type=int, default=1, help='work time (default = 1 minute)')
    track_parser.set_defaults(func=start_track)

    stat_parser = subparsers.add_parser('stat', help='print statistics for amount of days')
    stat_parser.add_argument('-p', '--project', type=str, dest='name_project', help='project name')
    stat_parser.add_argument('-d', '--days', type=int, help='amount of days')
    stat_parser.set_defaults(func=start_stat)
    args, unknown = parser.parse_known_args()
    args.func(args)
    return args, unknown


if __name__ == '__main__':
    parsing()
