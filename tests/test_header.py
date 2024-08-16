import pytest
from unittest import mock
from jsix_format.header import write_header, read_header

def test_write_header():
    mock_file = mock.mock_open()

    with mock.patch('builtins.open', mock_file):
        with open('test_file', 'w') as f:
            write_header(f, "JSIXIMAGEFORMAT", 1024, 768, 3)

    mock_file().write.assert_any_call("JSIXIMAGEFORMAT\n")
    mock_file().write.assert_any_call("00000400\n")  # 1024 in hex
    mock_file().write.assert_any_call("00000300\n")  # 768 in hex
    mock_file().write.assert_any_call("00000003\n")  # 3 in hex

def test_read_header():
    mock_file = mock.mock_open(read_data="JSIXIMAGEFORMAT\n00000400\n00000300\n00000003\n")

    with mock.patch('builtins.open', mock_file):
        with open('test_file', 'r') as f:
            magic_number, width, height, pixel_depth = read_header(f)

    assert magic_number == "JSIXIMAGEFORMAT"
    assert width == 1024
    assert height == 768
    assert pixel_depth == 3
