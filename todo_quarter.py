
from datetime import datetime
from todo_item import TodoItem


class TodoQuarter:
    def __init__(self):
        '''
        Constructs a *ToDoQuarter* object.

        * `todo_items`
          - data: list
          - description: list of TodoItem objects
        '''
        self.todo_items = []

    def sort_items(self):
        '''
        Sorts a *todo_items* list decreasing by attribute *deadline*.
        '''
        self.todo_items.sort(key=lambda item: item.deadline, reverse=False)

    def add_item(self, title, deadline):
        '''
        Append *TodoItem* object to attribute *todo_items* sorted decreasing by *deadline*.
        Raises *TypeError* if an argument *deadline* is not an instance of *Datetime* class.
        '''
        self.todo_items.append(TodoItem(title, deadline))

        if type(deadline) is not datetime:
            raise TypeError('Deadline is not an instance of *Datetime* class.')

        self.sort_items()   # for tests passing ;)

    def remove_item(self, index):
        '''
        Removes *TodoItem* object from *index* of attribute *todo_items*.
        '''
        del self.todo_items[index]

    def archive_items(self):
        '''
        Removes all *TodoItem* objects with a parameter *is_done* set to *True* from attribute *todo_items*.
        '''
        for item in self.todo_items:
            if item.is_done is True:
                self.todo_items.remove(item)

    def get_item(self, index):
        '''
        Returns *TodoItem* object from *index* of attribute *todo_items*.
        Raises *IndexError* if an argument *index*  is out of range attribute *todo_items*.
        '''
        if index not in range(len(self.todo_items)):
            raise IndexError('Index is out of range.')

        return self.todo_items[index]

    def __str__(self):
        '''
        Returns a formatted string of *todo_items* sorted decreasing by *deadline*. There is an expecting output:

        1. [ ] 9-6  go to the doctor
        2. [x] 11-6 submit assignment

        Hint: use instance method *__str__()* from class *TodoItem*
        '''
        result = ''
        for i in range(len(self.todo_items)):
            result += str(i+1) + '. ' + str(self.todo_items[i].__str__()) + '\n'
        return result
