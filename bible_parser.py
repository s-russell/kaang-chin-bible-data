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
        self.current_book = None
        self.current_chapter = None

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

    def parse(self, lines):
        classified_lines = [(line, self.classify(line)) for line in lines]

        for i in range(len(classified_lines)):
            line, line_type = classified_lines[i]
            next_line, next_line_type = classified_lines[i + 1] if i < (
                len(classified_lines) - 1) else (None, None)

            if line_type == LineType.text and next_line_type == LineType.numbered_text:
                self.begin_new_book(line)

        return self.bible

    def begin_new_book(self, book_title):
        if(self.current_book):
            self.bible.books.append(self.current_book)
        self.current_book = Book(book_title)
