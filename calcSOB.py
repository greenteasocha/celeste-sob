from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List

INPUT_FILE = "chapters.csv"
OUTPUT_FILE = "SOB.txt"


@dataclass
class Chapter:
    name: str
    record: str


def read_file(filename: str) -> List[Chapter]:
    ret = []
    with open(filename, "r") as f:
        chapters = f.readlines()
        for chapter in chapters:
            name, record = chapter.strip().split(",")
            ret.append(Chapter(name, record))

    return ret


def write_file(filename: str, record: str) -> None:
    with open(filename, "w") as f:
        f.write(record)


def calc(chapters: List[Chapter]) -> str:
    base = datetime(1900, 1, 1, 0, 0, 0, 0)
    for chapter in chapters:
        record = datetime.strptime(chapter.record, "%M:%S.%f")
        delta = timedelta(
            hours=record.hour,
            minutes=record.minute,
            seconds=record.second,
            milliseconds=record.microsecond // 1000
        )
        base += delta
    return base.strftime("%H:%M:%S.%f")


def main():
    chapters = read_file(INPUT_FILE)
    sob = calc(chapters)
    write_file(OUTPUT_FILE, sob)


if __name__ == "__main__":
    main()
