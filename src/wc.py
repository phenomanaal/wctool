#!/usr/bin/env python3
from pathlib import Path
import sys
import argparse

def byte_count(filepath: str | Path = None, content: str = None) -> int:   
    
    if filepath:
        return Path(filepath).stat().st_size
    else:
        return len(content.encode('utf-8'))

def line_count(filepath: str | Path = None, content: str = None) -> int:

    if filepath:
        filepath = Path(filepath).resolve()
        
        with open(filepath, 'r', encoding='utf-8') as f:
            return sum(1 for line in f)
    else:
        return len(content.splitlines())
    
def word_count(filepath: str | Path = None, content: str = None) -> int:

    if filepath:
        filepath = Path(filepath).resolve()

        with open(filepath, 'r', encoding='utf-8') as f:
            text_file = f.read()

        return len(text_file.split())
    else:
        return len(content.split())

def character_count(filepath: str | Path = None, content: str = None) -> int:
    if filepath:
        filepath = Path(filepath).resolve()

        with open(filepath, 'r', encoding='utf-8') as f:
            text_file = f.read()
        text_file = text_file.replace('\r\n', '\n')

        return len(text_file)
    else:
        return len(content)
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some command-line arguments.")
    parser.add_argument("-l", "--lines", action="store_true", help="lines flag")
    parser.add_argument("-w", "--words", action="store_true", help="word flag")
    parser.add_argument("-c", "--characters", action="store_true", help="character flag")
    parser.add_argument("-f", "--filepath", type=str, required=False, help="The first argument")
   
    args = parser.parse_args()
    if args.filepath:
        inputs = { "filepath": Path(args.filepath) }
    else:
        inputs = { "content": sys.stdin.read() }

    display_num: str
    display_file: str
    if args.filepath:
        display_file = args.filepath
    else:
        display_file = ""

    if args.lines:
        display_num = str(line_count(**inputs))
    elif args.words:
        display_num = str(word_count(**inputs))
    elif args.characters:
        display_num = str(character_count(**inputs))
    else:
        display_num = f"{line_count(**inputs)} {word_count(**inputs)} {byte_count(**inputs)}"

    print(display_num, display_file)
    