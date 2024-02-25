import tkinter as tk
from tkinter import ttk
from subject import Subject
from utils import _dialog
from topic import Topic
from topicSelector import TopicSelector

class SubjectWindow:
    def __init__(self, subject: Subject) -> None:
        self.subject = subject
        self.topics = subject.topics
        self.window = tk.Toplevel()
        self.window.title(f'Study {subject.name}')
        self.window.grab_set()
        self.window.geometry('1400x900')
        self.w = 1400
        self.h = 900
        self.window.configure(background = '#1a1a1a')
        
        self.update_topic_list()
        
        ttk.Label(self.window, font = ("Segoe UI Black", 60), text = f'Study {subject.name}', background = '#1a1a1a').place(x = self.w/2, y = 70, anchor = tk.CENTER)
        
        def set_learned(id, learned):
            for topic in self.topics:
                for term in topic.terms:
                    if term.id == id:
                        term.learned = learned
        
        def _flaschards(*_):
            TopicSelector(subject, self.window.grab_set, set_learned)
                    
        ttk.Button(self.window, text = 'flashcards', command = _flaschards).place(x = 200, y = self.h / 2)
        
        self.window.mainloop()
        
    def update_topic_list(self):
        self.topic_var = tk.StringVar()
        self.topic_list = ttk.OptionMenu(self.window, self.topic_var, self.topics[0].name, *[topic.name for topic in self.topics])
        self.topic_list.place(x = 100, y = 100)
    
    def add_topic(self):
        def create(var: tk.StringVar):
            self.subject.topics.append(Topic(var.get()))
        
        _dialog('New Topic Name', 'Create New Topic', create)