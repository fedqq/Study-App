import tkinter as tk
from subject import Subject
from tasks import Tasks
import shelve
import sv_ttk
from tkinter import ttk
import datetime
from PIL import ImageTk, Image  
from subjectWindow import SubjectWindow
from utils import _dialog
from topic import Topic
from term import Term

class main:
    def __init__(self) -> None:
        self.subjects: list[Subject]
        self.root = tk.Tk()
        self.root.title("Study Help Application")
        self.root.configure(background = 'black')
        self.root.wm_attributes("-transparent", 'green')
        self.root.geometry(f'{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}')
        self.w = self.root.winfo_screenwidth()
        self.h = self.root.winfo_screenheight()
        self.root.attributes('-fullscreen', True)
        self.root.resizable(False, False)
        sv_ttk.use_dark_theme()
        style = ttk.Style()
        style.theme_use('sun-valley-dark')
        style.configure('TFrame', background = 'black')
        style.configure('Card.Accent.TButton', font = ('Segoe UI', 40))
        style.configure('Card.TButton', font = ('Segoe UI', 40))
        
        self.add_main_widgets()
        
        self.root.after(0, self.load_data)
        
        time_to_min = datetime.datetime.now().second % 60
        self.root.after(time_to_min*1000, self.update_time)
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.mainloop()
        
    def update_time(self):
        self.update_text()
        self.root.after(60000, self.update_time)
        
    def add_main_widgets(self):
        
        self.img = ImageTk.PhotoImage(Image.open('BG.png').resize([self.w, self.h]))
        
        self.canvas = tk.Canvas(self.root, background = 'black', width = self.w, height = self.h)
        self.canvas.place(x = 0, y = 0, anchor = tk.NW)
        self.canvas.create_image(0, 0, image = self.img, anchor = tk.NW)
        self.time_txt = self.canvas.create_text(self.w/2, 50, anchor = tk.N, font = ("Segoe UI Black", 150), fill = 'white')
        self.name_txt = self.canvas.create_text(self.w/2, 300, anchor = tk.N, font = ("Segoe UI Black", 70), fill = 'white')
        self.root.after(10, self.update_text)
        
        ttk.Button(self.root, text = 'Save & Close', style = 'Accent.TButton', command = self.on_close).place(x = self.w-10, y = self.h-10, anchor = tk.SE, width = 120, height = 35)
        
        ttk.Button(self.root, text = 'Add Subject', style = 'Accent.TButton', command = self.add_subject).place(x = self.w-10, y = self.h-50, anchor = tk.SE, width = 120, height = 35)
        ttk.Button(self.root, text = '_Update Grid', style = 'Accent.TButton', command = self.update_subjects).place(x = self.w-10, y = self.h-90, anchor = tk.SE, width = 120, height = 35)
    
        self.subject_grid = ttk.Frame(self.root)
        self.subject_grid.place(x = self.w/2, y = self.h*(2/3), anchor = tk.CENTER)
        
    def update_text(self):
        try:
            self.canvas.itemconfigure(self.name_txt, text = f'Hi {self.username}')
        except:
            pass
        self.canvas.itemconfigure(self.time_txt, text = f'{datetime.datetime.now().time().hour}:{datetime.datetime.now().time().minute}')
        
    def update_subjects(self):
        for child in self.subject_grid.winfo_children():
            child.destroy()
        counter = 0
        for subject in self.subjects:
            row = int((counter - (counter % 5)) / 5)
            column = counter % 5
            btn = ttk.Button(self.subject_grid, text = subject.name, style = 'Accent.TButton', width = 20)
            btn.grid(row = row, column = column, sticky = tk.NSEW, padx = 10, pady = 10, ipady = 30)
            btn.configure(command = lambda s = subject: SubjectWindow(s))
            counter += 1
        
    def add_subject(self):
        def add(var):
            self.subjects.append(Subject(var.get()))
            self.update_subjects()
        
        _dialog('Subject Name: ', 'Input Subject Name', add)
               
    def on_close(self):
        self.save_date()
        self.root.grab_set()
        self.root.destroy()
        
    def load_data(self):
        with shelve.open('data/userdata') as db:
            def try_load(id, default):
                try:
                    return db[id]
                except:
                    return default
            
            self.username = try_load('username', 'empty1010')
            self.tasks = try_load('tasks', Tasks())
            
            math = Subject('Mathematics')
            topic_one = Topic('Algebra')
            topic_one.add_term(Term('Linear Function', 'y = mx + c'))
            topic_one.add_term(Term('Quadratic Function', 'y = ax^2 + bx + c'))
            math.topics = []
            math.add_topic(topic_one)
            
            self.subjects = try_load('subjects', [math])
            self.update_subjects()
            
            if self.username == 'empty1010':
                def set_username(name):
                    self.username = name.get()
                    self.update_text()
                    self.update_subjects()
                _dialog('Username: ', 'Input Username', set_username)
            else:
                self.update_text()
            
    def save_date(self):
        with shelve.open('data/userdata') as db:
            db['username'] = self.username
            db['tasks'] = self.tasks
            db['subjects'] = self.subjects
            
main()
            