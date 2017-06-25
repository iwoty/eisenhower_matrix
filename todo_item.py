
from datetime import datetime


class TodoItem:

    def __init__(self, title, deadline):
        '''
        Constructs an ToDoItem object.
        Raises ValueError if type of any argument is incorrect.

        * `title`
          - data: string
          - description: title of todo_item

        * `deadline`
          - data: Datetime object
          - description: deadline of todo_item, year is always set to *2017*

        * `is_done`
          - data: bool
          - description: contains True if TODO item is done, otherwise contains False. Default value is False
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
            is_done_mark = '[x] '
        else:
            is_done_mark = '[ ] '

        return is_done_mark + str(self.deadline.day) + '-' + str(self.deadline.month) + ' ' + str(self.title)
