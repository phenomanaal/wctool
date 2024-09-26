import pytest
from pathlib import Path
from src.wc import FileCounter, StringCounter

@pytest.fixture
def file_counter():
    return FileCounter(Path(__file__).resolve().parent / "test.txt")

@pytest.fixture
def string_counter():
    with open(Path(__file__).resolve().parent / "test.txt", "r") as f:
        return StringCounter(f.read())
    
# FILE COUNTER test functions

def test_file_counter_byte_count(file_counter):
    assert file_counter.byte_count == 335042

def test_file_counter_line_count(file_counter):
    assert file_counter.line_count == 7145

def test_file_counter_word_count(file_counter):
    assert file_counter.word_count == 58164

def test_file_counter_character_count(file_counter):
    assert file_counter.character_count == 332146

# STRING COUNTER test functions

def test_string_counter_byte_count(string_counter):
    assert string_counter.byte_count == 335042

def test_string_counter_line_count(string_counter):
    assert string_counter.line_count == 7145

def test_string_counter_word_count(string_counter):
    assert string_counter.word_count == 58164

def test_file_counter_character_count(string_counter):
    assert string_counter.character_count == 332146

# test errors
def test_file_counter_file_does_not_exist():
    with pytest.raises(FileNotFoundError) as exc_info:
        FileCounter(Path(__file__).resolve().parent / "blah.txt")