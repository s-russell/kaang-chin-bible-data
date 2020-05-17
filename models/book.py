class Book:

    def __init__(self, name):
        self.name = name
        self.chapters = []

    def get_chapter(self, chap_number):
        chapters = [c for c in self.chapters if c.number == chap_number]
        return chapters[0] if chapters else None

    def add_chapter(self, chapter):
        self.chapters.append(chapter)
        self.chapters.sort(key=lambda c: c.number)
