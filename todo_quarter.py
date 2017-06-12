
from datetime import datetime
from todo_matrix import TodoMatrix


class TodoQuarter:

    def __init__(self):
        '''
        Constructs a *ToDoQuarter* object.
        '''
        self.todo_items = []
        pass

    def sort_items(self):
        '''
        Sorts a *todo_items* list decreasing by attribute *deadline*.
        '''
        pass

    def add_item(self, title, deadline):
        '''
        Append *TodoItem* object to attribute *todo_items* sorted decreasing by *deadline*.
        Raises *TypeError* if an argument *deadline* is not an instance of *Datetime* class.
        '''
        pass

    def remove_item(self, index):
        '''
        Removes *TodoItem* object from *index* of attribute *todo_items*.
        '''
        pass

    def archive_items(self):
        '''
        Removes all *TodoItem* objects with a parameter *is_done* set to *True* from attribute *todo_items*.
        '''
        pass

    def get_item(self, index):
        '''
        Returns *TodoItem* object from *index* of attribute *todo_items*.
        Raises *IndexError* if an argument *index*  is out of range attribute *todo_items*.
        '''
        pass

    def __str__(self):
        '''
        Returns a formatted string of *todo_items* sorted decreasing by *deadline*. There is an expecting output:

        1. [ ] 9-6  go to the doctor
        2. [x] 11-6 submit assignment

        Hint: use instance method *__str__()* from class *TodoItem*
        '''
        pass
