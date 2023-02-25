import argparse

from datetime import date
from utils import add_statistics, print_statistics


def start_track(args: argparse.Namespace) -> None:
    time = [date.today().strftime("%d.%m.%y"), args.n]
    print(add_statistics(args.name_project, time))


def start_stat(args: argparse.Namespace) -> None:
    print(print_statistics(args.name_project, args.days))


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


if __name__ == '__main__':
    args, unknown = parser.parse_known_args()
    args.func(args)
