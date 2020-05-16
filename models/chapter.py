class Chapter:

    def __init__(self, number):
        self.number = number
        self.title = ''
        self.verses = []

    def add_verse(self, verse):
        self.verses.append(verse)
        self.verses.sort(key=lambda v: v.number)

    def add_all_verses(self, verses):
        self.verses.extend(verses)
        self.verses.sort(key=lambda v: v.number)

    def get_verse(self, number):
        verses = [v for v in self.verses if v.number == number]
        return verses[0] if verses else None
