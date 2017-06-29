
from datetime import datetime
from todo_item import TodoItem
from todo_quarter import TodoQuarter
from todo_matrix import TodoMatrix


def main():
    matrix_expected = TodoMatrix()
    matrix_expected.add_items_from_file('todo_items_read_test.csv')
    matrix_expected.save_items_to_file('todo_items_save_test.csv')

    matrix_tested = TodoMatrix()
    matrix_tested.add_items_from_file('todo_items_save_test.csv')


if __name__ == '__main__':
    main()
