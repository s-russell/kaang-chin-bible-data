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
    TITLING_VERSE = auto()


class BookBuilder:

    def __init__(self, title):
        self.book = Book(title)
        self.state = BookBuilderState.ENUMERATING_CHAPTER
        self.current_chapter = None
        self.current_verse_title_lines = []

    def classify(self, text):
        classifiers = {
            BookBuilderState.ENUMERATING_CHAPTER: _classify_enumerating_chapter,
            BookBuilderState.TITLING_CHAPTER: _classify_titling_chapter,
            BookBuilderState.COLLECTING_VERSES: _classify_collecting_verses,
            BookBuilderState.TITLING_VERSE: _classify_titling_verse
        }
        classification = classifiers[self.state](text)
        return classification

    def process(self, text):
        line_type = self.classify(text)

        if line_type == LineType.CHAPTER_NUMBER:
            if self.current_chapter is not None:
                self.book.chapters += [self.current_chapter]
            self.current_chapter = Chapter(int(text))
            self.state = BookBuilderState.TITLING_CHAPTER

        elif line_type == LineType.CHAPTER_TITLE:
            self.current_chapter.title = text

        elif line_type == LineType.VERSE_CHUNK:
            verses = parse_verse_chunk(text)
            if len(self.current_verse_title_lines) > 0:
                verses[0].title = '\n'.join(self.current_verse_title_lines)
                self.current_verse_title_lines = []
            self.current_chapter.add_all_verses(verses)
            self.state = BookBuilderState.COLLECTING_VERSES

        elif line_type == LineType.VERSE_TITLE:
            self.current_verse_title_lines += [text]
            self.state = BookBuilderState.TITLING_VERSE

    def build(self):
        self.book.chapters += [self.current_chapter]
        return self.book


def _classify_enumerating_chapter(next_line):
    if next_line.isnumeric():
        return LineType.CHAPTER_NUMBER
    else:
        raise Exception(f"Chapter number expected. Got {next_line} instead.")


def _classify_titling_chapter(next_line):
    return LineType.VERSE_CHUNK if re.match('^\\d+', next_line) else LineType.CHAPTER_TITLE


def _classify_collecting_verses(next_line):
    if next_line.isnumeric():
        classification = LineType.CHAPTER_NUMBER
    elif re.match('^\\d+', next_line):
        classification = LineType.VERSE_CHUNK
    else:
        classification = LineType.VERSE_TITLE
    return classification


def _classify_titling_verse(next_line):
    return _classify_collecting_verses(next_line)


def parse_verse_chunk(chunk):
    verse_tuples = re.findall('(\\d+)(\\D+)', chunk)
    return [Verse(int(n), t.strip()) for n, t in verse_tuples]
