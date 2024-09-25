import pytest
from pathlib import Path
from src.wc import byte_count, line_count, word_count, character_count

@pytest.fixture
def file_path():
    return Path(__file__).resolve().parent / "test.txt"

def test_byte_count(file_path):
    assert byte_count(file_path) == 335042

def test_line_count(file_path):
    assert line_count(file_path) == 7145

def test_word_count(file_path):
    assert word_count(file_path) == 58164

def test_character_count(file_path):
    assert character_count(file_path) == 332146