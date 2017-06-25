
from datetime import datetime
from todo_item import TodoItem
from todo_quarter import TodoQuarter


class TodoMatrix:

    def __init__(self):
        '''
        Constructs a *TodoMatrix* object with all possible quarters.
        * `todo_quarters`
          - data: dictionary
          - description: contains *TodoQuarter* objects
          key: string - status of todo_quarter, value: *TodoQuarter* object

        possible status of TODO quarter:
        - 'IU' means that todo_quarter contains important todo_items & urgent
        - 'IN' means that todo_quarter contains important todo_items & not urgent
        - 'NU' means that todo_quarter contains not important todo_items & urgent
        - 'NN' means that todo_quarter contains not important & not urgent todo_items
        '''
        self.todo_quarters = {}

    def get_quarter(self, status):
        '''
        Returns a chosen *TodoQuarter* object from the attribute *todo_quarters*.
        Status should be one of the possible statuses ('IU', 'IN', 'NU', 'NN').
        '''
        pass

    def add_item(self, title, deadline, is_important=False):
        '''
        Append a *TodoQuarterItem* object to attribute *todo_items* in the properly *TodoQuarter* object.
        Raises *TypeError* if an argument *deadline* is not an instance of class *Datetime*.
        '''
        self.todo_quarters.append(TodoItem(title, deadline))

        if type(deadline) is not datetime:
            raise TypeError('Deadline is not an instance of *Datetime* class.')

    def add_items_from_file(self, file_name):
        '''
        Reads data from *file_name.csv* file and append *TodoItem* objects to attributes *todo_items* in the properly
        *TodoQuarter*   objects.
        Raises *FileNotFoundError* if a file doesn't exist.
        Every item is written to a separate line in the following format:

        `title|day-month|is_important`

        If *is_important* is equal to False then last element is en empty string. Otherwise the last element
        is an arbitrary string.
        If the last element of line is an empty string, *is_important* is equal to False - it means that the item
        should be assign to a not important TODO quarter. Otherwise item should be assign to an important TODO quarter.
        '''
        file_name += '.csv'
        try:
            with open(file_name, "r") as file:
                lines = file.readlines()
            table = [element.replace("\n", "") for element in lines]

        except FileNotFoundError:
            raise FileNotFoundError('File doesn\'t exist')

    def save_items_to_file(self, file_name):
        '''
        Writes all details about TODO items to *file_name.csv* file
        Every item is written to a separate line in the following format:

        `title|day-month|is_important`

        If *is_important* contains False then the last element of line should be an empty string. Otherwise last element
        is an arbitrary string.
        '''
        file_name += '.csv'
        with open(file_name, "w") as file:
            for record in table:
                row = record
                file.write(row + "\n")

    def archive_items(self):
        '''
        Removes all *TodoItem* objects with a parameter *is_done* set to *True* from list *todo_items* in every element
        of the attribute *todo_quarters*
        '''
        pass

    def __str__(self):
        '''
        Returns all elements of attribute *todo_quarters* formatted to string.
        '''
        pass
