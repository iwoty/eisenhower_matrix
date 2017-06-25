
from datetime import datetime
from todo_item import TodoItem
from todo_quarter import TodoQuarter
from todo_matrix import TodoMatrix


def main():
    quarter = TodoQuarter()

    date = datetime(2017, 6, 16)
    date2 = datetime(2017, 6, 14)
    date3 = datetime(2017, 7, 24)

    quarter.add_item('go to Codecool', date)
    quarter.add_item('make a coffee', date2)
    quarter.add_item('code', date3)
    print(quarter)

    quarter.todo_items[0].mark()
    print(quarter)
    quarter.archive_items()
    print(quarter)
    print(quarter.todo_items[0].is_done)


if __name__ == '__main__':
    main()
