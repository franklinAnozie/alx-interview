#!/usr/bin/python3
""" Script to read line by line for stdin """

import sys
import re


def println():
    """ Prints a line """
    print(f"File size: {Expected_Line.get_total_file_size()}")
    stat_code_dict = Expected_Line.get_status_code_count()
    for key in stat_code_dict:
        if stat_code_dict[key] > 0:
            print(f"{key}: {stat_code_dict[key]}")


def readln():
    """ Reads content of stdin and prints out after 10 lines """
    count = 0
    try:
        for line in sys.stdin:
            new_line = Expected_Line(line)
            if new_line.match_status():
                new_line.set_total_file_size(int(new_line.size))
                try:
                    new_line.set_status_code_count(int(new_line.status))
                except Exception as e:
                    pass
                count += 1
                if count == 10:
                    println()
                    count = 0
                    sys.stdout.flush()
            else:
                pass
        println()
    except KeyboardInterrupt:
        println()
        sys.exit(0)


class Expected_Line():
    """
    Class to construct the data structure and save their info
    """
    __total_file_size = 0
    __status_code_count = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }

    def __init__(self, line_read: str) -> None:
        """ init method """
        log_pattern = re.compile(r"""
            (?P<ip>.*?)
            \[(?P<date>.+?)\]                    # Date
            \s"GET\s/projects/260\sHTTP/1\.1"\s  # HTTP Request
            (?P<status>.*)                    # Status Code
            \s
            (?P<size>\d+)                        # File Size
        """, re.VERBOSE)
        self.match = log_pattern.match(line_read)
        if self.match:
            self.IP = f"{self.match.group('ip')}"
            self.date = f"{self.match.group('date')}"
            self.status = f"{self.match.group('status')}"
            self.size = f"{self.match.group('size')}"

    def match_status(self) -> bool:
        """ returns true or false depending on if there
        was a successful match or not in the init fxn
        """
        return bool(self.match)

    @classmethod
    def get_total_file_size(cls) -> int:
        """ class method to retrieve the file size data """
        return cls.__total_file_size

    @classmethod
    def set_total_file_size(cls, value: int) -> None:
        """ Class method to set the value of the file size """
        cls.__total_file_size += value

    @classmethod
    def get_status_code_count(cls) -> dict:
        """ class method to retrieve the status codes data """
        return cls.__status_code_count

    @classmethod
    def set_status_code_count(cls, status_code: int) -> None:
        """ class method to set the value of the status codes """
        if status_code in cls.__status_code_count:
            cls.__status_code_count[status_code] += 1


if __name__ == "__main__":
    readln()
