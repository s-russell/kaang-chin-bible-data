from .book_builder import *


def test_book_builder_creation():
    bb = BookBuilder("Matthew")
    assert bb.book.title == "Matthew"
    assert bb
    assert bb.state == BookBuilderState.ENUMERATING_CHAPTER
    assert bb.last_line_type == LineType.BOOK_TITLE


def test_book_builder_first_chapter_title():
    bb = BookBuilder("Matthew")
    bb.process("1")
    assert bb.state == BookBuilderState.TITLING_CHAPTER
    assert bb.current_chapter.number == 1
    assert len(bb.book.chapters) == 0


def test_classify_number_test():
    bb = BookBuilder("Matthew")
    bb.state = BookBuilderState.ENUMERATING_CHAPTER
    assert bb.classify("13") == LineType.CHAPTER_NUMBER
