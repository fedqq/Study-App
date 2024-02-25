import tkinter as tk
from tkinter import ttk
from term import Term

class Flashcards:
    def __init__(self, terms: list[Term], subject_name: str, return_grab_func, learn_func) -> None:
        self.terms = terms
        self.window = tk.Toplevel()
        self.grab_to_root = return_grab_func
        self.learn_term = learn_func
        self.window.grab_set()
        self.window.resizable(False, False)
        self.window.title(f'Flashcards for {subject_name}')
        self.window.wm_protocol('WM_DELETE_WINDOW', self._on_close)
        
        ttk.Label(self.window, text = f'Flashcards for {subject_name}', font = ('Segoe UI Bold', 30)).grid(column = 0, row = 0, columnspan = 3, padx = 20, pady = 20)
        
        self.current_term_index = 0
        self.showing_name = True
        
        self.next_arrow = ttk.Button(self.window, style = 'Accent.TButton', text = '⇛', command = self._next)
        self.previous_arrow = ttk.Button(self.window, style = 'Accent.TButton', text = '⇚', command = self._previous)
        
        self.big_display = ttk.Button(self.window, command = self._flip_flashcard, width = 20)
        
        self.learned_var = tk.StringVar(value = 'Mark As Learned')
        self.learn_btn = ttk.Button(self.window, textvariable = self.learned_var, command = self._mark_learned)
        
        self.prog_var = tk.DoubleVar(value = 0)
        self.prog_bar = ttk.Progressbar(self.window, length = 100, maximum = len(self.terms)+0.00000000001, mode = 'determinate')
        
        self.next_arrow.grid(row = 1, column = 2, padx = 20, pady = 20)
        self.previous_arrow.grid(row = 1, column = 0, padx = 20, pady = 20)
        self.big_display.grid(row = 1, column = 1, sticky = tk.NSEW, padx = 20, pady = 20, ipady = 30)
        self.learn_btn.grid(row = 2, column = 0, padx = 20, pady = 20, columnspan = 3, sticky = tk.NSEW)
        self.prog_bar.grid(row = 3, column = 1, padx = 20, pady = 20, columnspan = 3, sticky = tk.NSEW)
        
        self._update()
        
        self.window.mainloop()
        
    def _mark_learned(self) -> None:
        term = self.terms[self.current_term_index]
        if term.learned:
            self.terms[self.current_term_index].unlearn()
            self.learn_term(term.id, False)
        else:
            self.terms[self.current_term_index].learn()
            self.learn_term(term.id, True)
        self._update()
        
    def _current_term(self):
        return self.terms[self.current_term_index]
        
    def _flip_flashcard(self) -> None:
        term = self._current_term()
        self.showing_name = not self.showing_name
        if self.showing_name:
            self.big_display.configure(text = term.name, style = 'Card.Accent.TButton')
        else:
            self.big_display.configure(text = term.meaning, style = 'Card.TButton')
        
    def _on_close(self):
        self.grab_to_root()
        self.window.grab_release()
        self.window.destroy()
        
    def _update(self):
        self.showing_name = True
        self.big_display.configure(text = term.name, style = 'Card.Accent.TButton')
        term = self._current_term()
        
        if term.learned:
            self.learned_var.set('Mark As Unlearned')
        else:
            self.learned_var.set('Mark As Learned')
            
        self.prog_bar['value'] = len([1 for term in self.terms if term.learned])
        self.current_term_index = self.current_term_index % (len(self.terms))
        
    def _next(self) -> None:
        self.current_term_index += 1
        self._update()
    
    def _previous(self) -> None:
        self.current_term_index -= 1
        self._update()