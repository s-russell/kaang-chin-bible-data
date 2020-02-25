import docx2txt
import re
from models.verse import Verse


def parse_verse_chunk(chunk):
    verse_tuples = re.findall('(\\d+)(\\D+)', chunk)
    return [Verse(int(n), t.strip()) for n, t in verse_tuples]


def main():
    johan_txt = docx2txt.process('docx/Johan.docx')
    lines = [line.strip() for line in johan_txt.split('\n\n') if line.strip() != '']
    for line in lines: print(line)


if __name__ == '__main__':
    main()
