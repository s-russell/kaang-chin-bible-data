class Verse:
    number = -1
    title = None
    text = None

    def __init__(self, number, text, title=None):
        self.number = number
        self.text = text
        self.title = title
