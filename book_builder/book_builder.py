from enum import Enum, auto
from .models.book import Book
from .models.chapter import Chapter
from .models.verse import Verse
import re


class LineType(Enum):
    BOOK_TITLE = auto()
    CHAPTER_NUMBER = auto()
    CHAPTER_TITLE = auto()
    VERSE_CHUNK = auto()
    VERSE_TITLE = auto()


class BookBuilderState(Enum):
    ENUMERATING_CHAPTER = auto()
    TITLING_CHAPTER = auto()
    COLLECTING_VERSES = auto()


class BookBuilder:

    def __init__(self, title):
        self.book = Book(title)
        self.last_line_type = LineType.BOOK_TITLE
        self.state = BookBuilderState.ENUMERATING_CHAPTER
        self.current_chapter = None

    def classify(self, text):
        classifiers = {
            BookBuilderState.ENUMERATING_CHAPTER: _classify_enumerating_chapter,
            BookBuilderState.TITLING_CHAPTER: _classify_titling_chapter,
            BookBuilderState.COLLECTING_VERSES: _classify_collecting_verses
        }
        classification = classifiers[self.state](text)
        return classification

    def process(self, text):
        line_type = self.classify(text)

        if line_type == LineType.CHAPTER_NUMBER:
            self.current_chapter = Chapter(int(text))
            self.state = BookBuilderState.TITLING_CHAPTER

        elif line_type == LineType.CHAPTER_TITLE:
            self.current_chapter.title = text

        elif line_type == LineType.VERSE_CHUNK:
            verses = parse_verse_chunk(text)
            self.current_chapter.add_all_verses(verses)
            self.state = BookBuilderState.COLLECTING_VERSES


def _classify_enumerating_chapter(next_line):
    if next_line.isnumeric():
        return LineType.CHAPTER_NUMBER
    else:
        raise Exception(f"Chapter number expected. Got {next_line} instead.")


def _classify_titling_chapter(next_line):
    return LineType.VERSE_CHUNK if re.match('^\\d+', next_line) else LineType.CHAPTER_TITLE


def _classify_collecting_verses(next_line):
    if re.match('^\\d+', next_line):
        return LineType.VERSE_CHUNK


def parse_verse_chunk(chunk):
    verse_tuples = re.findall('(\\d+)(\\D+)', chunk)
    return [Verse(int(n), t.strip()) for n, t in verse_tuples]
