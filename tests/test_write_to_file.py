import os
import pytest

from conftest import test_data_for_writing, clear_test_file
from track.utils.files import write_to_file
from track.utils.utils import add_statistics


def test_write_to_file(test_data_for_writing):
    test_filepath = 'tests/test_files/test_write_to_file.json'
    size_file_before = os.path.getsize(test_filepath)
    write_to_file(test_data_for_writing, filepath=test_filepath)
    size_file_after = os.path.getsize(test_filepath)
    assert size_file_after > size_file_before
    clear_test_file(test_filepath)
