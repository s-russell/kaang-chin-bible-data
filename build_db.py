import docx2txt
from book_builder.book_builder import BookBuilder
import sqlite3
import sys

db_name = 'kc-bible-auto.db'


def get_numbers(number_string):
    return [int(n) for n in number_string.split()]


book_data = [
    {'file': 'Mate', 'name': 'Mate', 'stats': {
        'chapter_count': 28,
        'verses_counts': get_numbers('25	23	17	25	48	34	29	34	38	42	30	50	58	36	39	28	27	35	30	34	46	46	39	51	46	75	66	20')
    }},
    {'file': 'Mark', 'name': 'Mark', 'stats': {
        'chapter_count': 16,
        'verses_counts': get_numbers('45	28	35	41	43	56	37	38	50	52	33	44	37	72	47	20')
    }},
    {'file': 'Luka ei Thuthangni', 'name': 'Luka', 'stats': {
        'chapter_count': 24,
        'verses_counts': get_numbers('80	52	38	44	39	49	50	56	62	42	54	59	35	35	32	31	37	43	48	47	38	71	56	53')
    }},
    {'file': 'Johan', 'name': 'John', 'stats': {
        'chapter_count': 21,
        'verses_counts': get_numbers('51	25	36	54	47	71	53	59	41	42	57	50	38	31	27	33	26	40	42	31	25')
    }},
    {'file': 'THOEITHANAK', 'name': 'Thoeithanak', 'stats': {
        'chapter_count': 28,
        'verses_counts': get_numbers('26	47	26	37	42	15	60	40	43	48	30	25	52	28	41	40	34	28	40	38	40	30	35	27	27	32	44	31')
    }},  # Acts
    {'file': 'ROMEN', 'name': 'Romen', 'stats': {
        'chapter_count': 16,
        'verses_counts': get_numbers('32	29	31	25	21	23	25	39	33	21	36	21	14	23	33	27')
    }},
    {'file': '1Korintu', 'name': '1 Korin', 'stats': {
        'chapter_count': 16,
        'verses_counts': get_numbers('31	16	23	21	13	20	40	13	27	33	34	31	13	40	58	24')
    }},
    {'file': '2Korintu', 'name': '2 Korin', 'stats': {
        'chapter_count': 13,
        'verses_counts': get_numbers('24	17	18	18	21	18	16	24	15	18	33	21	13')
    }},
    {'file': 'Kalati', 'name': 'Kalati', 'stats': {
        'chapter_count': 6,
        'verses_counts': get_numbers('24	21	29	31	26	18')
    }},  # Galations
    {'file': 'Efisa', 'name': 'Efisa', 'stats': {
        'chapter_count': 6,
        'verses_counts': get_numbers('23	22	21	32	33	24')
    }},
    {'file': 'Filipi', 'name': 'Filipi', 'stats': {
        'chapter_count': 4,
        'verses_counts': get_numbers('30	30	21	23')
    }},
    {'file': 'Kolote', 'name': 'Kolote', 'stats': {
        'chapter_count': 4,
        'verses_counts': get_numbers('29	23	25	18')
    }},  # Colosians
    {'file': '1THESALONI', 'name': '1 Thesaloni', 'stats': {
        'chapter_count': 5,
        'verses_counts': get_numbers('10	20	13	18	28')
    }},
    {'file': '2THESALONI', 'name': '2 Thesaloni', 'stats': {
        'chapter_count': 3,
        'verses_counts': get_numbers('12	17	18')
    }},
    {'file': '1TIMOTHY', 'name': '1 Timothy', 'stats': {
        'chapter_count': 6,
        'verses_counts': get_numbers('20	15	16	16	25	21')
    }},
    {'file': '2TIMOTHY', 'name': '2 Timothy', 'stats': {
        'chapter_count': 4,
        'verses_counts': get_numbers('18	26	17	22')
    }},
    {'file': 'TITUS', 'name': 'Titus', 'stats': {
        'chapter_count': 3,
        'verses_counts': get_numbers('16	15	15')
    }},
    {'file': 'FILEMON', 'name': 'Filemon', 'stats': {
        'chapter_count': 1,
        'verses_counts': get_numbers('25')
    }},
    {'file': 'HEBREW', 'name': 'Hebrews', 'stats': {
        'chapter_count': 13,
        'verses_counts': get_numbers('14	18	19	16	14	20	28	13	28	39	40	29	25')
    }},
    {'file': 'JAME', 'name': 'James', 'stats': {
        'chapter_count': 5,
        'verses_counts': get_numbers('27	26	18	17	20')
    }},
    {'file': '1PITER', 'name': '1 Peter', 'stats': {
        'chapter_count': 5,
        'verses_counts': get_numbers('25	25	22	19	14')
    }},
    {'file': '2PETER', 'name': '2 Peter', 'stats': {
        'chapter_count': 3,
        'verses_counts': get_numbers('21	22	18')
    }},
    {'file': '1JOHN', 'name': '1 John', 'stats': {
        'chapter_count': 5,
        'verses_counts': get_numbers('10	29	24	21	21')
    }},
    {'file': '2JOHN', 'name': '2 John', 'stats': {
        'chapter_count': 1,
        'verses_counts': get_numbers('13')
    }},
    {'file': '3 JOHN', 'name': '3 John', 'stats': {
        'chapter_count': 1,
        'verses_counts': get_numbers('15')
    }},
    {'file': 'JUDE', 'name': 'Jude', 'stats': {
        'chapter_count': 1,
        'verses_counts': get_numbers('25')
    }},
    {'file': 'Thuphran', 'name': 'Thuphran', 'stats': {
        'chapter_count': 22,
        'verses_counts': get_numbers('20	29	22	11	14	17	17	13	21	11	19	17	18	20	8	21	18	24	21	15	27	21')
    }},  # Revelations
]


def dupe_verse(c, v): return len(
    [v1 for v1 in c.verses if v1.number == v.number]) > 1


def zero_in_verse(v): return v.number == 0


def validation_errors(b):
    return [f"{c.number}:{v.number} {v.text}" for c in b.chapters for v in c.verses if dupe_verse(c, v) or zero_in_verse(v)]


def parse(bl):
    book_list = []
    for item in bl:
        book_txt = docx2txt.process(f"docx_normalized/{item['file']}.docx")
        lines = [line.strip()
                 for line in book_txt.split('\n\n') if line.strip() != '']
        bb = BookBuilder(lines[0])
        for line in lines[1:]:
            bb.process(line)
        book = bb.build()
        book.name = item['name']
        errors = validation_errors(book)
        if errors:
            print(f"Validation failed for docx_normalized/{item['file']}.docx")
            print('\n'.join(errors))
            sys.exit(1)
        else:
            book_list.append(book)
    return book_list


def create_db(db):
    with open('data/scripts/create_tables.sql', 'r') as sql_file:
        qry = sql_file.read()
        db.executescript(qry)


insert_chapter = """
        insert into chapter(number, title, book_id)
        values(?,?,?)
        """

insert_verse = """
    insert into verse(number, title, text, chapter_id)
    values(?,?,?,?)
    """


def load_book(book, db):
    db.execute('insert into book(name, language) values(?,?)',
               (book.name, 'Kaang Chin'))
    book_id = db.lastrowid

    for c in book.chapters:
        chapter_params = (c.number, c.title if c.title else None, book_id)
        db.execute(insert_chapter, chapter_params)
        chapter_id = db.lastrowid
        verse_params = [(v.number, v.title if v.title else None,
                         v.text, chapter_id) for v in c.verses]
        print(f"loading {book.name} {c.number} -- {len(c.verses)} verses")
        db.executemany(insert_verse, verse_params)


def validate_statistics(bl):
    errors = []
    for book in bl:
        stats = [item['stats']
                 for item in book_data if item['name'] == book.name][0]
        expectd_chapter_count = stats['chapter_count']
        observed_chapter_count = len(book.chapters)
        if expectd_chapter_count != observed_chapter_count:
            errors.append({'book': book.name, 'type': 'chapter count',
                           'expected': expectd_chapter_count, 'observed': observed_chapter_count})
        for i, c in enumerate(book.chapters):
            expected_verse_count = stats['verses_counts'][i]
            observed_verse_count = len(c.verses)
            if expected_verse_count != observed_verse_count:
                errors.append({'book': book.name, 'chapter': c.number, 'type': 'verse count',
                               'expected': expected_verse_count, 'observed': observed_verse_count})
    if errors:
        for e in errors:
            print(
                f"{e['book']} {e['chapter']}\t\texpected: {e['expected']} verses but got {e['observed']}")
        sys.exit(2)


if __name__ == '__main__':
    book_list = parse(book_data)
    print(f"Parsed {len(book_list)} books:")

    validate_statistics(book_list)

    conn = sqlite3.connect(db_name)
    db = conn.cursor()
    print("Creating Database")
    create_db(db)
    for book in book_list:
        load_book(book, db)

    conn.commit()
    conn.close()

    sys.exit(0)
