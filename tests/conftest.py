import json
import pytest

from datetime import date
from track.settings.parser_value import TrackValue


@pytest.fixture
def test_track_value():
    return TrackValue(
        project_name='test_name',
        time=[date.today().strftime("%d.%m.%y"), 10]
    )

@pytest.fixture
def test_data_for_writing(test_track_value):
    test_data = {}
    test_data[test_track_value.project_name] = test_track_value.time
    return test_data


def clear_test_file(test_filepath):
    with open(test_filepath, 'w') as test_file:
        json.dump({}, test_file)
