#!/usr/bin/env python3
from pathlib import Path
import argparse

def byte_count(filepath: str | Path) -> int:   
    
    return Path(filepath).stat().st_size

def line_count(filepath: str | Path) -> int:

    filepath = Path(filepath).resolve()
    
    with open(filepath, 'r') as f:
        return sum(1 for line in f)
    
def word_count(filepath: str | Path) -> int:
    filepath = Path(filepath).resolve()

    with open(filepath, 'r') as f:
        text_file = f.read()

    return len(text_file.split())
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some command-line arguments.")
    parser.add_argument("-l", "--lines", action="store_true", default=False, help="lines flag")
    parser.add_argument("filepath", type=str, help="The first argument")
    args = parser.parse_args()

    if args.lines:
        print(line_count(args.filepath), args.filepath)
    else:
        print(byte_count(args.filepath), args.filepath)
    