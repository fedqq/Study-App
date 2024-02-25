from topic import Topic
from test import Test

class Subject:
    def __init__(self, name: str) -> None:
        self.name = name
        self.topics: list[Topic] = [Topic('Topic A'), Topic('Topic B')]
        self.done_tests: list[Test] = []
        
    def add_topic(self, topic: Topic):
        self.topics.append(topic)