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


def test_add_chapter_title():
    next_line = "Some chapter title"
    bb = get_builder_for_state(BookBuilderState.TITLING_CHAPTER)
    assert bb.classify(next_line) == LineType.CHAPTER_TITLE
    bb.process(next_line)
    assert bb.state == BookBuilderState.TITLING_CHAPTER
    assert bb.current_chapter.title == next_line


def test_add_first_verse_without_chapter_title():
    next_line = "1Some verse. 2The next verse."
    bb = get_builder_for_state(BookBuilderState.TITLING_CHAPTER)
    assert bb.classify(next_line) == LineType.VERSE_CHUNK
    bb.process(next_line)
    assert bb.state == BookBuilderState.COLLECTING_VERSES
    assert len(bb.current_chapter.verses) == 2
    assert bb.current_chapter.get_verse(2).text == 'The next verse.'


def test_collecting_verses():
    bb = get_builder_for_state(BookBuilderState.COLLECTING_VERSES)
    verse_chunk_1 = '3This is a verse. 4Another verse here 5This one ends "with a quote."'
    verse_chunk_2 = '6Another verse over here. 7Can you read this?'
    bb.process(verse_chunk_1)
    bb.process(verse_chunk_2)
    assert len(bb.current_chapter.verses) == 7
    assert bb.current_chapter.get_verse(6).text == 'Another verse over here.'


def test_classify_number_test():
    bb = BookBuilder("Matthew")
    bb.state = BookBuilderState.ENUMERATING_CHAPTER
    assert bb.classify("13") == LineType.CHAPTER_NUMBER


def get_builder_for_state(bb_state):
    bb = BookBuilder("Matthew")
    bb.process("1")
    if bb_state == BookBuilderState.TITLING_CHAPTER:
        return bb
    bb.process('Chapter title')
    bb.process('1First verse. 2Second verse.')
    if bb_state == BookBuilderState.COLLECTING_VERSES:
        return bb
