class Chapter:
    number = -1
    title = ''
    verses = []

    def __init__(self, number):
        self.number = number

    def add_verse(self, verse):
        self.verses.append(verse)
        self.verses.sort(key=lambda v: v.number)

    def add_all_verses(self, verses):
        self.verses.extend(verses)
        self.verses.sort(key=lambda v: v.number)

    def get_verse(self, number):
        return self.verses[number - 1] if number <= len(self.verses) else None