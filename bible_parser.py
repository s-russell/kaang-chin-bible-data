from enum import Enum, auto
import re
from models.bible import Bible
from models.book import Book
from models.chapter import Chapter
from models.verse import Verse


def parse_verse_chunk(chunk):
    verse_tuples = re.findall('(\\d+)([\\D0]+)', chunk)
    return [Verse(int(n), t.strip()) for n, t in verse_tuples]


class LineType(Enum):
    number = auto()
    text = auto()
    numbered_text = auto()


class BibleParser:

    def __init__(self, language):
        self.bible = Bible(language)
        self.current_book = None
        self.current_chapter = None
        self.current_verse_title = None

    def classify(self, line_text):
        line_type = None

        if line_text.isnumeric():
            line_type = LineType.number
        elif self.check_pattern_match('^[123]? ?[a-zA-Z0 ]+$', line_text):
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
            next_line, _ = classified_lines[i + 1] if i < (
                len(classified_lines) - 1) else (None, None)

            if line_type == LineType.text and next_line == '1':
                self.begin_new_book(line)
            elif line_type == LineType.text:
                self.current_verse_title = line
            elif line_type == LineType.number:
                self.begin_new_chapter(line)
            elif line_type == LineType.numbered_text:
                verses = parse_verse_chunk(line)
                if(self.current_verse_title):
                    verses[0].title = self.current_verse_title
                    self.current_verse_title = None
                self.current_chapter.add_all_verses(verses)

        self.current_book.add_chapter(self.current_chapter)
        self.bible.books.append(self.current_book)
        return self.bible

    def begin_new_book(self, book_title):
        if(self.current_book):
            self.current_book.add_chapter(self.current_chapter)
            self.bible.books.append(self.current_book)
        self.current_chapter = None
        self.current_book = Book(book_title)

    def begin_new_chapter(self, chapter_number_str):
        chapter_number = int(chapter_number_str)
        if(self.current_chapter):
            self.current_book.add_chapter(self.current_chapter)
        self.current_chapter = Chapter(chapter_number)
