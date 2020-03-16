from enum import Enum, auto
from .models.book import Book
from .models.chapter import Chapter


class LineType(Enum):
    BOOK_TITLE = auto()
    CHAPTER_NUMBER = auto()
    CHAPTER_TITLE = auto()
    VERSE_CHUNK = auto()
    VERSE_TITLE = auto()


class BookBuilderState(Enum):
    ENUMERATING_CHAPTER = auto()
    TITLING_CHAPTER = auto()


class BookBuilder:

    def __init__(self, title):
        self.book = Book(title)
        self.last_line_type = LineType.BOOK_TITLE
        self.state = BookBuilderState.ENUMERATING_CHAPTER
        self.current_chapter = None

    def classify(self, text):
        classifiers = {
            BookBuilderState.ENUMERATING_CHAPTER: _classify_enumerating_chapter
        }
        classification = classifiers[self.state](text)
        return classification

    def process(self, text):
        line_type = self.classify(text)
        if line_type == LineType.CHAPTER_NUMBER:
            self.current_chapter = Chapter(int(text))
            self.state = BookBuilderState.TITLING_CHAPTER


def _classify_enumerating_chapter(next_line):
    if next_line.isnumeric():
        return LineType.CHAPTER_NUMBER
    else:
        raise Exception(f"Chapter number expected. Got {next_line} instead.")
