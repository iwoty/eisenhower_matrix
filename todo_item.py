
from datetime import datetime
from todo_quarter import TodoQuarter
from todo_matrix import TodoMatrix


class TodoItem:

    def __init__(self, title, deadline):
        '''
        Constructs an ToDoItem object.
        Raises ValueError if type of any argument is incorrect.
        '''
        self.title = title
        self.deadline = deadline
        self.is_done = False

        if type(title) is not str:
            raise ValueError('Title must be a string.')

        if type(deadline) is not datetime:
            raise ValueError('Deadline must be a Datetime object.')

    def mark(self):
        '''
        Sets the object's * is_done * attribute to True
        '''
        self.is_done = True

    def unmark(self):
        '''
        Sets the object's * is_done * attribute to False
        '''
        self.is_done = False

    def __str__(self):
        '''
        Returns a formatted string with details about todo_item.
        Format of deadline is 'day-month'

        Expecting output for example done item:
        `[x] 12-6 submit assignment`

        Expecting output for example undone item:
        `[ ] 28-6 submit assignment`
        '''
        if self.is_done is True:
            is_done_mark = 'x'
        else:
            is_done_mark = ' '

        return '[' + is_done_mark + '] ' + self.deadline + ' ' + self.title
