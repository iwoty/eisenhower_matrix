
from datetime import datetime
from datetime import timedelta
from todo_item import TodoItem
from todo_quarter import TodoQuarter
import csv


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
        self.todo_quarters = {'IU': TodoQuarter(),
                              'IN': TodoQuarter(),
                              'NU': TodoQuarter(),
                              'NN': TodoQuarter()}

    def get_quarter(self, status):
        '''
        Returns a chosen *TodoQuarter* object from the attribute *todo_quarters*.
        Status should be one of the possible statuses ('IU', 'IN', 'NU', 'NN').
        '''
        return(todo_quarters[status])

    def add_item(self, title, deadline, is_important=False):
        '''
        Append a *TodoQuarterItem* object to attribute *todo_items* in the properly *TodoQuarter* object.
        Raises *TypeError* if an argument *deadline* is not an instance of class *Datetime*.
        '''
        if deadline - datetime.now() < timedelta(days=3):
            is_urgent = True
        else:
            is_urgent = False

        if is_important is True and is_urgent is True:
            status = 'IU'
        elif is_important is True and is_urgent is False:
            status = 'IN'
        elif is_important is False and is_urgent is True:
            status = 'NU'
        elif is_important is False and is_urgent is False:
            status = 'NN'

        self.todo_quarters[status].add_item(title, deadline)

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
        try:
            with open(file_name, 'r') as f:
                lines = f.readlines()
            table = [element.replace('\n', '').split('|') for element in lines]

            for item in table:
                item[1] = item[1].split('-')  # split deadline from 'DD-MM' to day and month seperately
                month = int(item[1][1])
                day = int(item[1][0])
                year = datetime.now().year

                if item[2] == 'important':
                    is_important = True
                else:
                    is_important = False

                self.add_item(item[0], datetime(year, month, day), is_important)

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
        with open(file_name, "w") as file:
            for key in self.todo_quarters:
                for element in self.todo_quarters[key].todo_items:
                    row = []
                    row.append(element.title)
                    row.append(str(element.deadline.day) + '-' + str(element.deadline.month))

                    if key == 'IU' or key == 'IN':
                        row.append('important')
                    else:
                        row.append('')

                    file.write('|'.join(row) + '\n')

    def archive_items(self):
        '''
        Removes all *TodoItem* objects with a parameter *is_done* set to *True* from list *todo_items* in every element
        of the attribute *todo_quarters*
        '''
        for obj in self.todo_quarters.values():
            obj.archive_items()

    def __str__(self):
        '''
        Returns all elements of attribute *todo_quarters* formatted to string.
        str.center(width[, fillchar])
        '''
        CELL_WIDTH = 40
        TABLE_WIDTH = 2*CELL_WIDTH + 9
        line = '-'*TABLE_WIDTH + '\n'

        view_matrix = [' '*4 + '|' +
                       'URGENT'.center(CELL_WIDTH) + '|' +
                       'NOT URGENT'.center(CELL_WIDTH) + '|' + ' '*2 + '\n']
        view_matrix.append(line)
        # ljust(width[, fillchar])
        # for i in range(16):
        #     view_matrix.append(dict)
        view_matrix.append('IU' + '\n')
        view_matrix.append(self.todo_quarters['IU'].__str__())

        view_matrix.append('IN' + '\n')
        view_matrix.append(self.todo_quarters['IN'].__str__())

        view_matrix.append('NU' + '\n')
        view_matrix.append(self.todo_quarters['NU'].__str__())

        view_matrix.append('NN' + '\n')
        view_matrix.append(self.todo_quarters['NN'].__str__())

        view_matrix.append(line)
        return ''.join(view_matrix)
