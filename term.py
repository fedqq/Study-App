class Term:
    def __init__(self, name: str, meaning: str) -> None:
        self.name = name
        self.meaning = meaning
        self.learned = False
        self.id = f'term:{self.name}:means:{self.meaning}'
        
    def learn(self):
        self.learned = True
        
    def unlearn(self):
        self.learned = False