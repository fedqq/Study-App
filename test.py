from term import Term
from testTypes import TestType

class Test:
    def __init__(self, terms: list[Term], type: TestType) -> None:
        self.terms = terms
        self.type = type