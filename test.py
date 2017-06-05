import unittest
from datetime import datetime
from todo_item import TodoItem
from todo_quarter import TodoQuarter
from todo_matrix import TodoMatrix


class TodoItemTester(unittest.TestCase):


    def test_constructor(self):
        date = datetime(2017, 6, 4)
        item = TodoItem('implement ToDoItem class', date)
        self.assertEqual(item.title, 'implement ToDoItem class', "Wrong todo_item")
        self.assertEqual(item.deadline, date, 'Wrong deadline')
        self.assertEqual(item.is_done, False, 'dupa')
        self.assertIsInstance


    def test_constructor2(self):
        d = datetime(2017, 5, 16)
        t = TodoItem('implement TodoItem class', d)
        self.assertEqual(t.title, 'implement TodoItem class', "Wrong todo_item")
        self.assertEqual(t.deadline, d, 'Wrong deadline')


    def test_value_error(self):
        date = '2017-03-05'
        with self.assertRaises(ValueError, msg='Deadline must be a Datetime object'):
            item = TodoItem('implement TodoItem class', date)


    def test_value_error2(self):
        date = datetime(2017, 5, 16)
        with self.assertRaises(ValueError, msg='Title must be a string'):
            item = TodoItem(100, date)


    def test_mark(self):
        date = datetime(2017, 6, 4)
        item = TodoItem('implement TodoItem class', date)
        item.mark()
        self.assertEqual(item.is_done, True, 'Item wasn\'t marked')


    def test_unmark(self):
        date = datetime(2017, 6, 4)
        item = TodoItem('implement TodoItem class', date)
        item.mark()
        item.unmark()
        self.assertEqual(item.is_done, False, 'Item wasn\'t unmarked')


    def test_str(self):
        date = datetime(2017, 6, 4)
        item = TodoItem('implement TodoItem class', date)
        self.assertIsInstance(item.__str__(), str)


    def test_str2(self):
        date = datetime(2017, 6, 4)
        item = TodoItem('implement TodoItem class', date)
        test_string = item.__str__()
        self.assertEqual(test_string[1], ' ', 'Wrong sign')


    def test_str3(self):
        date = datetime(2017, 6, 4)
        item = TodoItem('implement TodoItem class', date)
        item.mark()
        test_string = item.__str__()
        self.assertEqual(test_string[1], 'x', 'Wrong sign')


class TodoQuarterTester(unittest.TestCase):


    def test_constructor(self):
        quarter = TodoQuarter()
        self.assertEqual(quarter.todo_items, [])


    def test_add_item2(self):
        quarter = TodoQuarter()
        date = datetime(2017, 7, 4)
        quarter.add_item('implement Quarter Class', date)
        self.assertEqual(quarter.todo_items[0].deadline, date)
        self.assertEqual(quarter.todo_items[0].title, 'implement Quarter Class')


    def test_add_item_error(self):
        quarter = TodoQuarter()
        with self.assertRaises(ValueError, msg='Incorrect deadline'):
            quarter.add_item('implement Quarter Class', 'error date')


    def test_sort_items(self):
        quarter = TodoQuarter()
        date1 = datetime(2017, 6, 14)
        date2 = datetime(2017, 5, 24)
        date3 = datetime(2017, 6, 4)
        date4 = datetime(2017, 7, 3)
        date5 = datetime(2017, 6, 23)

        quarter.add_item('go to Codecool', date1)
        quarter.add_item('make a coffee', date2)
        quarter.add_item('start coding', date3)
        quarter.add_item('more coffee', date4)
        quarter.add_item('more coding', date5)

        self.assertEqual(quarter.todo_items[0].deadline, date2)
        self.assertEqual(quarter.todo_items[1].deadline, date3)
        self.assertEqual(quarter.todo_items[2].deadline, date1)
        self.assertEqual(quarter.todo_items[3].deadline, date5)
        self.assertEqual(quarter.todo_items[4].deadline, date4)


    def test_get_item(self):
        date = datetime(2017, 7, 4)
        quarter = TodoQuarter()
        quarter.add_item('implement Quarter Class', date)
        item = quarter.get_item(0)
        self.assertIsInstance(item, TodoItem)


    def test_get_item_error(self):
        quarter = TodoQuarter()
        with self.assertRaises(IndexError,
                                msg='Index out of range list todo_items'):
            quarter.get_item(5)


    def test_remove_item(self):
        quarter = TodoQuarter()

        date = datetime(2017, 7, 4)
        date2 = datetime(2017, 6, 14)
        date3 = datetime(2017, 9, 24)

        quarter.add_item('go to Codecool', date)
        quarter.add_item('make a coffee', date2)
        quarter.add_item('code', date3)

        quarter.remove_item(1)

        self.assertEqual(len(quarter.todo_items), 2, 'Incorrect lenght of todo_items list')
        self.assertEqual(quarter.todo_items[1].title,'code', 'Incorrect item')


    def test_archive_items(self):
        quarter = TodoQuarter()

        date = datetime(2017, 6, 16)
        date2 = datetime(2017, 6, 14)
        date3 = datetime(2017, 7, 24)

        quarter.add_item('go to Codecool', date)
        quarter.add_item('make a coffee', date2)
        quarter.add_item('code', date3)

        quarter.todo_items[0].mark()
        quarter.archive_items()

        self.assertEqual(len(quarter.todo_items), 2, 'Incorrect lenght of todo_items list')
        self.assertEqual(quarter.todo_items[0].title,'go to Codecool', 'Incorrect item')


    def test_str(self):
        quarter = TodoQuarter()

        date = datetime(2017, 6, 16)
        date2 = datetime(2017, 6, 14)
        date3 = datetime(2017, 7, 24)

        quarter.add_item('go to Codecool', date)
        quarter.add_item('make a coffee', date2)
        quarter.add_item('code', date3)

        quarter.todo_items[1].mark()
        quarter_string = quarter.__str__()

        self.assertIsInstance(quarter_string, str,
                                msg='it\'s not a string!')
        self.assertEqual(quarter_string[0:6], '1. [ ]')
        self.assertEqual(quarter_string[26:32], '2. [x]')


class TodoMatrixTester(unittest.TestCase):


    def test_constructor(self):
        matrix = TodoMatrix()
        self.assertEqual(tuple(matrix.todo_quarters), ('IU', 'IN', 'NU', 'NN'))


    def test_add_items_from_file(self):
        matrix = TodoMatrix()
        matrix.add_items_from_file('todo_items_read_test.csv')

        self.assertEqual(matrix.todo_quarters['IU'].__str__(),
                        '1. [ ] 5-6 make a coffee\n2. [ ] 6-6 read about OOP\n')
        self.assertEqual(matrix.todo_quarters['IN'].__str__(),
                        '1. [ ] 30-6 give mentors a feedback\n2. [ ] 23-10 go to the doctor\n')
        self.assertEqual(matrix.todo_quarters['NU'].__str__(),
                        '1. [ ] 7-6 start coding\n')
        self.assertEqual(matrix.todo_quarters['NN'].__str__(),
                        '1. [ ] 28-6 buy flowers\n2. [ ] 15-7 cook a dinner\n')


    def test_file_error(self):
        matrix = TodoMatrix()
        with self.assertRaises(FileNotFoundError, msg='Problem with open a file'):
            matrix.add_items_from_file('no_file.csv')


    def test_add_item(self):
        matrix = TodoMatrix()
        title = 'test add_item function'
        date_urgent = datetime(2017, 6, 6)
        date_not_urgent = datetime(2017, 7, 24)

        matrix.add_item(title, date_urgent, True)
        matrix.add_item(title, date_urgent, False)
        matrix.add_item(title, date_not_urgent, True)
        matrix.add_item(title, date_not_urgent, False)

        self.assertEqual(matrix.todo_quarters['IU'].todo_items[0].title,
                        'test add_item function' )
        self.assertEqual(matrix.todo_quarters['IN'].todo_items[0].title,
                        'test add_item function' )
        self.assertEqual(matrix.todo_quarters['NU'].todo_items[0].title,
                        'test add_item function' )
        self.assertEqual(matrix.todo_quarters['NN'].todo_items[0].title,
                        'test add_item function' )


    def test_add_item_error(self):
        matrix = TodoMatrix()
        with self.assertRaises(TypeError, msg='Incorrect deadline'):
            matrix.add_item('test error', 'error date')


    def test_archive_items(self):
        matrix = TodoMatrix()
        title = 'test add_item function'
        date_urgent = datetime(2017, 6, 6)
        date_not_urgent = datetime(2017, 7, 24)

        matrix.add_item(title, date_urgent, True)
        matrix.add_item(title, date_urgent, False)
        matrix.add_item(title, date_not_urgent, True)
        matrix.add_item(title, date_not_urgent, False)

        matrix.todo_quarters['IU'].todo_items[0].mark()
        matrix.todo_quarters['IN'].todo_items[0].mark()
        matrix.todo_quarters['NU'].todo_items[0].mark()
        matrix.todo_quarters['NN'].todo_items[0].mark()

        matrix.archive_items()

        self.assertEqual(matrix.todo_quarters['IU'].todo_items, [])
        self.assertEqual(matrix.todo_quarters['IN'].todo_items, [])
        self.assertEqual(matrix.todo_quarters['NU'].todo_items, [])
        self.assertEqual(matrix.todo_quarters['NN'].todo_items, [])


    def test_save_items_to_file(self):
        matrix_expected = TodoMatrix()
        matrix_expected.add_items_from_file('todo_items_read_test.csv')
        matrix_expected.save_items_to_file('todo_items_save_test.csv')

        matrix_tested = TodoMatrix()
        matrix_tested.add_items_from_file('todo_items_save_test.csv')

        self.assertEqual(matrix_tested.todo_quarters['IU'].__str__(),
                        matrix_expected.todo_quarters['IU'].__str__())

        self.assertEqual(matrix_tested.todo_quarters['IN'].__str__(),
                        matrix_expected.todo_quarters['IN'].__str__())

        self.assertEqual(matrix_tested.todo_quarters['NU'].__str__(),
                        matrix_expected.todo_quarters['NU'].__str__())

        self.assertEqual(matrix_tested.todo_quarters['NN'].__str__(),
                        matrix_expected.todo_quarters['NN'].__str__())



def main():
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
