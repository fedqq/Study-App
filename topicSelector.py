import tkinter as tk
from tkinter import ttk
from subject import Subject
from topic import Topic
from flashcards import Flashcards

class TopicSelector:
    def __init__(self, subject: Subject, grab_func, learn_func) -> None:
        self.window = tk.Toplevel()
        self.window.title('Select Topics to Include in Flaschards')
        self.window.resizable(False, False)
        self.subject = subject
        
        ttk.Label(self.window, text = f'Select topics from {subject.name}').pack(padx = 20, pady = 20)
        
        chosen_topics: list[Topic] = []
        
        def add_topic(t: Topic, b: ttk.Button):
            chosen_topics.append(t)
            b.configure(style = 'TButton')
        
        for topic in subject.topics:
            
            btn = ttk.Button(self.window, text = topic.name, style = 'Accent.TButton')
            btn.configure(command = lambda t=topic, b=btn: add_topic(t, b))
            btn.pack(padx = 20, pady = 10)
         
        def confirm():
            if chosen_topics == []:
                return
            terms = []
            for topic in chosen_topics:
                terms += topic.terms
            self.window.destroy()
            Flashcards(terms, subject.name, grab_func, learn_func)
        
        ttk.Button(self.window, text = 'confirm', command = confirm).pack(padx = 20, pady = 20)
        
        self.window.grab_set()
        self.window.mainloop()