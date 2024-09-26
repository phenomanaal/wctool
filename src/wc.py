#!/usr/bin/env python3
from pathlib import Path
import sys
import argparse

class FileCounter:
    def __init__(self, filepath: str | Path):
        self.filepath = Path(filepath).resolve()
        if not self.filepath.exists():
            raise FileNotFoundError(f"The file {self.filepath} does not exist.")
        with open(self.filepath, "r", encoding="utf-8") as f:
            self.file_text = f.read()
        super().__init__()

    @property
    def byte_count(self):
        return self.filepath.stat().st_size
    
    @property
    def line_count(self):
        with open(self.filepath, 'r', encoding='utf-8') as f:
            return sum(1 for line in f)

    @property
    def word_count(self):
        return len(self.file_text.split())
    
    @property
    def character_count(self) -> int:
        return len(self.file_text.replace('\r\n', '\n'))
    
class StringCounter:
    def __init__(self, content: str):
        self.content = content

    @property
    def byte_count(self):
        return len(self.content.encode('utf-8'))
    
    @property
    def line_count(self):
        return len(self.content.splitlines())
    
    @property
    def word_count(self):
        return len(self.content.split())
    
    @property
    def character_count(self) -> int:
        return len(self.content)

def main():
    parser = argparse.ArgumentParser(description="Process some command-line arguments.")
    parser.add_argument("-l", "--lines", action="store_true", help="lines flag")
    parser.add_argument("-w", "--words", action="store_true", help="word flag")
    parser.add_argument("-m", "--multibyte", action="store_true", help="character flag")
    parser.add_argument("-c", "--count", action="store_true", help="byte flag")
    parser.add_argument("filepath", nargs='?', type=str, help="The first argument (optional filepath)")
   
    args = parser.parse_args()

    display_file: str
    display_num: str

    if args.filepath:
        display_file = args.filepath
        try:
            counter = FileCounter(args.filepath)
        except FileNotFoundError as e:
            print(e)
            sys.exit(1)
    else:
        display_file = ""
        counter = StringCounter(sys.stdin.read())   
        

    if args.lines:
        display_num = str(counter.line_count)
    elif args.words:
        display_num = str(counter.word_count)
    elif args.multibyte:
        display_num = str(counter.character_count)
    elif args.count:
        display_num = str(counter.byte_count)
    else:
        display_num = f"{counter.line_count} {counter.word_count} {counter.byte_count}"

    print(display_num, display_file)


if __name__ == "__main__":
    main()