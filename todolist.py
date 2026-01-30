import os

from todoitem import Todo


class ToDoList:
    """
    Module for managing a simple to-do list application.
    This module provides a ToDoList class that allows users to create and manage
    a list of tasks with basic operations such as adding, removing, and editing items.
        A simple to-do list manager.
        This class provides functionality to manage a list of items with operations
        including adding items, removing items, editing items, displaying all items,
        and retrieving a string representation of the list.
        Attributes:
            __todo_items (list): A private list to store to-do items.
    """

    def __init__(self, file_name="todo_list.txt"):
        self.__todo_items = []
        self.__file_name = file_name
        self.load_items_from_file()

    @classmethod
    def prompt_for_index(cls, message="Enter item index: "):
        """
        Prompt the user to enter an index number.

        Returns:
            int: The index number entered by the user.
        """
        valid = False
        index = 0
        while not valid:
            try:
                index = int(input(message))
                valid = True
            except ValueError:
                print("Please enter a valid number.")
        return index

    def is_valid_index(self, index):
        try:
            item = self.__todo_items[index - 1]
            return True
        except IndexError:
            return False

    def load_items_from_file(self):
        """
        Loads items from a specified file into the object's internal list. If the file does not
        exist, it will be created. This method ensures the file is always present for subsequent
        operations.

        :raises FileNotFoundError: When an error other than the absence of the file prevents it
            from being opened.
        :return: None
        """
        #Check if the filename exists
        if not os.path.exists(self.__file_name):
            #Create a file if it doesn't exist
            open(self.__file_name, "w").close()
            return

        with open(self.__file_name, "r") as file:
            todo_items = file.read().splitlines()

        for todo_item in todo_items:
            todo = todo_item.split(',')
            if len(todo) < 3:
                self.__todo_items.append(Todo(todo))
            else:
                self.__todo_items.append(Todo(todo[0], todo[1], todo[2]))

    def save_items_to_file(self):
        """
        Saves the current list of items to a file. Each item in the list is written to a
        new line in the specified file.

        :param self: The instance of the class containing the list of items to be saved
            and the file name.
        :return: None
        """
        with open(self.__file_name, "w") as file:
            for todo_item in self.__todo_items:
                file.write(f"{todo_item.task},{todo_item.priority},{todo_item.time_estimate}\n")



    def show(self):
        """
        Display all items in the to-do list.

        Prints each item with its index number. If the list is empty, it
        displays a message indicating there are no items.
        """
        if not self.__todo_items:
            print("No items in the list!")
            return
        for index, todo_item in enumerate(self.__todo_items, 1):
            print(f"{index}: {todo_item}")

    def __str__(self):
        return f"Items: {self.__todo_items}"

    def add_todo_item(self, todo_item):
        """
        Add an item to the to-do list.

        Args:
            todo_item: The item to be added to the list.

        Raises:
            None: Prints a message if the item already exists instead of raising an exception.
        """
        if todo_item in self.__todo_items:
            print("Item already exists!")
            return
        self.__todo_items.append(todo_item)

    def complete_todo(self, index):
        """
        Remove an item from the todo list by its index.

        Args:
            index (int): The position of the item to remove (1-indexed).

        Raises:
            IndexError: If the index is out of range.
        """
        try:
            self.__todo_items.pop(index - 1)
        except IndexError:
            print("That item does not exist.")

    def edit_todo_item(self, index, todo_item):
        """
        Edit an existing item in the todo list at the specified index.

        Args:
            index (int): The position of the item to edit (1-indexed).
            todo_item (Todo): The new todo item for todo_items list.

        Returns:
            None
        """
        self.__todo_items[index - 1] = todo_item

    def get_todo_items(self):
        return self.__todo_items

    def get_todo_item_by_index(self, index):
        return self.__todo_items[index - 1]

    def get_todo_item_index(self, todo_item):
        return self.__todo_items.index(todo_item)

    def todo_item_exists(self, todo_item):
        tasks = [todo.task for todo in self.__todo_items]
        return todo_item.task in tasks


if __name__ == "__main__":
    sample_list = ToDoList("test_todo_list.txt")
    sample_list.add_todo_item(Todo("First Todo", "High", "10"))
    sample_list.edit_todo_item(1, Todo("Next Todo", "Low", "5"))
    sample_list.show()
    sample_list.save_items_to_file()

