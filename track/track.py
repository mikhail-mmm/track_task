import argparse

from datetime import date
from track.settings.parser_value import TrackValue, StatValue
from track.utils.utils import add_statistics, get_statistics, is_required_attributes


def track(args: argparse.Namespace) -> None:
    if is_required_attributes('track', args.project_name):
        track_data = TrackValue(
            project_name=args.project_name,
            time=[date.today().strftime("%d.%m.%y"), args.n],
        )
        add_statistics(track_data)


def return_statistics(args: argparse.Namespace) -> None:
    if is_required_attributes('stat', args.project_name, args.days):
        stat_data = StatValue(
            project_name=args.project_name,
            days=args.days,
        )
        get_statistics(stat_data)


def main() -> None:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title='subcommands', help='log time or print statistic')

    track_parser = subparsers.add_parser('track', help='tracking project work time')
    track_parser.add_argument('-p', '--project', dest='project_name', help='project name')
    track_parser.add_argument('n', type=int, default=1, help='work time (default = 1 minute)')
    track_parser.set_defaults(func=track)

    stat_parser = subparsers.add_parser('stat', help='print statistics for amount of days')
    stat_parser.add_argument('-p', '--project', type=str, dest='project_name', help='project name')
    stat_parser.add_argument('-d', '--days', type=int, help='amount of days')
    stat_parser.set_defaults(func=return_statistics)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
