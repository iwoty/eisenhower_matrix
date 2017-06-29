from todo_matrix import TodoMatrix
from datetime import datetime
import os


class Application:
    options = ['1. Add new item to matrix',
               '2. Mark item as done',
               '3. Undo marking item as done',
               '4. Remove TODO item',
               '5. Archive TODO items (remove done items)',
               '0. Exit']

    def __init__(self):
        self.is_running = True

    def run(self):
        os.system('clear')
        matrix = TodoMatrix()
        matrix.add_items_from_file('todo.csv')

        while self.is_running:
            os.system('clear')
            print(matrix)
            self.display_menu()
            option = self.get_input('Enter choice of menu: ')

            if option == '1':
                title = self.get_input('Enter title of TODO item: ')
                deadline_year = self.get_input('Enter year of deadline: ')
                deadline_month = self.get_input('Enter month of deadline: ')
                deadline_day = self.get_input('Enter day of deadline: ')
                deadline = datetime(int(deadline_year), int(deadline_month), int(deadline_day))
                is_important = self.get_input('Is the task important? True/False: ')
                if is_important == 'True':
                    is_important = True
                elif is_important == 'False':
                    is_important = False
                matrix.add_item(title, deadline, is_important)

            elif option == '2':
                quarter_choice = self.get_input('Choose quarter (IU/IN/NU/NN): ')
                item_choice = int(self.get_input('Choose number of item to mark as done: ')) - 1
                quarter = matrix.todo_quarters[quarter_choice]
                item = quarter.todo_items[item_choice]
                item.mark()

            elif option == '3':
                quarter_choice = self.get_input('Choose quarter (IU/IN/NU/NN): ')
                item_choice = int(self.get_input('Choose number of item to unmark from done: ')) - 1
                quarter = matrix.todo_quarters[quarter_choice]
                item = quarter.todo_items[item_choice]
                item.unmark()

            elif option == '4':
                quarter_choice = self.get_input('Choose quarter (IU/IN/NU/NN): ')
                item_choice = int(self.get_input('Choose number of item to remove: ')) - 1
                quarter = matrix.todo_quarters[quarter_choice]
                quarter.remove_item(item_choice)
                # item = quarter.todo_items[item_choice]
                # item.unmark()

            elif option == '5':
                matrix.archive_items()

            elif option == '0':
                self.is_running = False

        matrix.archive_items()
        matrix.save_items_to_file('todo.csv')

    def get_input(self, message):
        return input(message)

    def display_menu(self):
        print('\n'.join(self.options))
