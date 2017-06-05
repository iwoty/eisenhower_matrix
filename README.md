# Eisenhower ToDoMatrix App

## The story

The Eisenhower Matrix is a great tool for time managing and improve your productivity. It is often used in IT projects teams to prioritize tasks.

## Tasks

1. Important & urgent: Implement all modules described in a specification.
2. Important & not urgent: Adjust it for user needs, based on the user story.
3. Not important & urgent: Fill up the specification (use markdown syntax).
4. Not important & not urgent: Add some extra features.


## User story

1. As a user I would like to choose a status of shown TODO items:
  - urgent & important items
  - not urgent & important items
  - urgent & not important items
  - not urgent & not important items

  Urgent means that there's 3 days (72 hours) to deadline at least.

2. As a user I would like to see a list TODO items sorted decreasing by deadline from chosen matrix's quarter with its details.

3. As a user I would like to see a deadline formatted to *day_month*. I use matrix for the 2017 year.

4. As a user I would like to add an item with its deadline and priority, which is automatically assign to a properly quarter.

5. As a user I would like to mark TODO item by cross if it's done.

6. As a user I would like to undo marking a TODO item.

7. As a user I would like to remove a chosen TODO item.

8. As a user I would like to archive TODO items - remove all done items.         

9. A a user I would like to keep all my TODO items in a .csv files.

10. As a user I would like to see a whole Eisenhower matrix (every quarter with its items).

Extras:
11. As a user I would like to see colored (only unmarked) todo_items:
  - green: if the deadline is coming far than 3 days
  - orange: if deadline is coming in the next 3 days
  - red: if deadline is crossed

12. As a user I would like to see a matrix formatted to table.



## Requirements

* Implement all modules described in a specification.
* Implement the *main.py* module and fulfill its specification.
* You are allowed to implement your own custom functions and modules. Remember about clean code.
* Remember about comments and docstrings.
* All tests must pass.
* Please don't change a file *todo_items_read_test.csv*! It's important for passing tests.
* Your program should fulfill cases described in the user story.
* Use module *datetime* for time variables and operations -> https://docs.python.org/3/library/datetime.html
* Program should be based on the Object Oriented Programming paradigm
* Remember about proper constructors - not all attributes object are assign by a parameter!
* Plan your task in Eisenhower matrix. First of all focus on the implement required class (and its instance methods). Then think about usefulness.
* Please fill up specification in this file if you implement new functions. Use markdown syntaxes.

## The specification

### `main.py`
TODO

### `todo_item.py`

This is the file containing an todo_item business logic.

### Class TodoItem

__Attributes__

* `title`
  - data: string
  - description: title of todo_item

* `deadline`
  - data: Datetime object
  - description: deadline of todo_item, year is always set to *2017*

* `is_done`
  - data: bool
  - description: contains True if TODO item is done, otherwise contains False.  Default value is False

__Instance methods__

* ##### ` __init__(self, title, deadline) `
  constructs an ToDoItem object
  raises ValueError if type of any argument is incorrect

* `mark(self)`
  sets the object's * is_done * attribute to True

* `unmark(self)`
  sets the object's * is_done * attribute to False

* `__str__(self)`
  returns a formatted string with details about todo_item.
  Format of deadline is 'day-month'

  Expecting output for example done item:
  ```
  [x] 12-6 submit assignment
  ```

  Expecting output for example undone item:
  ```
  [ ] 28-6 submit assignment
  ```

### `todo_quarter.py`

This is the file containing a logic of an Eisenhower todo_quarter.

### Class TodoQuarter

__Instance Attributes__

* `todo_items`
  - data: list
  - description: list of TodoItem objects

__Instance methods__

* ##### ` __init__(self) `
  constructs a *ToDoQuarter* object

* `sort_items(self)`
  sorts a *todo_items* list decreasing by *deadline* attribute

* `add_item(self, title, deadline)`
  append *TodoItem* object to `archive_todo_items(self)` *todo_items* sorted decreasing by *deadline*
  raises *TypeError* if an argument *deadline* is not an instance of Datetime class

* `remove_item(self)`
  removes *TodoItem* object from *index* of list *todo_items*

* `archive_todo_items(self)`
  removes all *TodoItem* objects with a parameter *is_done* set to *True* from list *todo_items*

* `get_item(self, index)`
  returns *TodoItem* object from *index* of list *todo_items*
  raises *IndexError* if an argument *index*  is out of range list *todo_items*

* `__str__(self)`
  returns a formatted list of *todo_items* sorted decreasing by *deadline*. There is an expecting output:

  ```
  1. [ ] 9-6  go to the doctor
  2. [x] 11-6 submit assignment
  ```
  Hint: use instance method *__str__()* from class *TodoItem*


### todo_matrix.py

### Class TodoMatrix

This is the file containing the logic of an Eisenhower todo_matrix.

__Attributes__

* todo_quarters
  - data: dictionary
  - description: contains *TodoQuarter* objects
    key: string - status of todo_quarter, value: ToDoQuarter object
        possible status of TODO quarter:
        'IU' means that todo_quarter contains important todo_items & urgent
        'IN' means that todo_quarter contains important todo_items & not urgent
        'NU' means that todo_quarter contains not important todo_items & urgent
        'NN' means that todo_quarter contains not important & not urgent todo_items

__Instance methods__

* ##### `__init__(self) `
  constructs a *TodoMatrix* object with all possible quarters

* `get_quarter(self, status)`
  returns a *TodoQuarter* object from a dictionary *todo_quarters*

* `add_item`(self, title, deadline, is_important=False)
  append a *TodoQuarterItem* object to attribute *todo_items* in the properly *TodoQuarter* object  
  raises *TypeError* if an argument *deadline* is not an instance of Datetime class

* `add_items_from_file(self, file_name)`
  reads data from *file_name.csv* file and append *TodoItem* objects to attributes *todo_items* in the properly *TodoQuarter* objects
  raises *FileNotFoundError* if a file doesn't exist

  every item is written in a separate line the following format:
  ```
  title|day-month|is_important
  ```
  If *TodoItem* object attribute *is_important* contains False then last element is en empty string. Otherwise last element is an arbitrary string

* `save_items_to_file`(self, file_name)
  writes all details about TODO items to *file_name.csv* file
  every item is written in a separate line the following format:
  ```
  title|day-month|is_important
  ```
  If *TodoItem* object attribute *is_important* contains False then last element is en empty string. Otherwise last element is an arbitrary string

* `archive_items(self)`
  removes all *TodoItem* objects with a parameter *is_done* set to *True* from list *todo_items* in every element of dictionary *todo_quarters*

* `__str__(self)`
  returns a todo_quarters list (an Eisenhower todo_matrix) formatted to string

  optional:
  output string is formatted to the following table:

    ```
    |            URGENT              |           NOT URGENT           |  
  --|--------------------------------|--------------------------------|--
    | 1. [ ] 9-6  go to the doctor   |                                |
    | 2. [x] 11-6 submit assignment  |                                |
  I |                                |                                |
  M |                                |                                |
  P |                                |                                |
  O |                                |                                |
  R |                                |                                |      
  T |                                |                                |
  A |                                |                                |
  N |                                |                                |
  T |                                |                                |
    |                                |                                |
    |                                |                                |
  --|--------------------------------|--------------------------------|--                               
  N | 1. [ ] 14-6 buy a ticket       | 1. [x] 30-5 House of Cards     |
  O |                                |                                |
  T |                                |                                |
    |                                |                                |
  I |                                |                                |
  P |                                |                                |
  O |                                |                                |
  R |                                |                                |
  T |                                |                                |
  A |                                |                                |
  N |                                |                                |
  T |                                |                                |
  --|--------------------------------|--------------------------------|--
  ```
