import pytest

from track.utils.utils import is_required_attributes


@pytest.mark.parametrize(
    'subparser,project_name,days,expected',
        [
    ('track', 'project_name', 2, True),
    ('track', 'project_name', None, True),
    ('track', None, 2, False),
    ('track', None, None, False),
    ('stat', 'project_name', 2, True),
    ('stat', 'project_name', None, False),
    ('stat', None, None, False),
        ]
)
def test_is_required_attributes(subparser, project_name, days, expected):
    assert is_required_attributes(subparser, project_name, days) == expected
