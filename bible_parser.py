from enum import Enum, auto
import re
from models.bible import Bible
from models.book import Book


class LineType(Enum):
    number = auto()
    text = auto()
    numbered_text = auto()


class BibleParser:

    def __init__(self, language):
        self.bible = Bible(language)
        self.last_line_type = None
        self.last_line = None
        self.current_book = None

    def classify(self, line_text):
        line_type = None

        if line_text.isnumeric():
            line_type = LineType.number
        elif self.check_pattern_match('^[123]? ?[a-zA-Z ]+$', line_text):
            line_type = LineType.text
        elif self.check_pattern_match('^(\\d{1,3}[\\S ]+)+$', line_text):
            line_type = LineType.numbered_text

        return line_type

    def check_pattern_match(self, match_pattern, text):
        pattern = re.compile(match_pattern)
        match = pattern.match(text)
        return True if match else False

    def process(self, line):
        line_type = self.classify(line)

        if line_type == LineType.numbered:

    def build(self):
        if self.current_book:
            self.bible.add_book(self.current_book)
        return self.bible
