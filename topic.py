from term import Term

class Topic: 
    def __init__(self, topic_name: str) -> None:
        self.terms: list[Term] = []
        self.name = topic_name
        
    def add_term(self, term: Term):
        self.terms.append(term)