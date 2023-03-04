import pytest

from track.utils.files import is_file


@pytest.mark.parametrize(
    'file_path,expected',
        [
    ('tests/test_files/test_is_file.json', True),
    ('tests/test_files/non_exist_file.json', False),
        ]
)
def test_is_file(file_path, expected):
    assert is_file(file_path) == expected
