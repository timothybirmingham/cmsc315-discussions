"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    library = "Manheim Township Public Library"

    def __init__(self, book_name, book_author):
        self.book_name = book_name
        self.book_author = book_author

    def display_info(self):
        print(f"{self.book_name} {self.book_author}")

    def display_library(self):
        print(self.library)

book1 = ParentClass("Let My People Go Surfing", "Yvon C.")
book2 = ParentClass("Animal Farm", "George O.")

book1.display_info()
book2.display_info()


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    book_type = "eBook"

    def __init__(self, book_name, book_author, file_format, file_size):
        super().__init__(book_name, book_author)
        self.file_format = file_format
        self.file_size = file_size

    def display_info(self):
        print(f"{self.book_name} - {self.book_author} - {self.file_format} - {self.file_size} MB")

    def display_file_info(self):
        print(f"{self.file_format} {self.file_size}")

eBook1 = ChildClass("The Way of the Shepard", "Kevin L.", "PDF", 20)
eBook2 = ChildClass("High Output Management", "Andrew G.", "PDF", 40)

eBook1.display_info()
eBook2.display_info()

eBook1.display_file_info()
eBook2.display_file_info()


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    # print("\n=== Namespace Demonstration ===")
    # print("TODO: Implement namespace demonstration")

    eBook1 = ChildClass("The Way of the Shepard", "Kevin L.", "PDF", 20)
    eBook2 = ChildClass("High Output Management", "Andrew G.", "PDF", 40)

    eBook1.book_review = 4.3

    print(ChildClass.book_type)
    print(eBook1.book_type)

    print(eBook1.__dict__)
    print(eBook2.__dict__)

    print(ChildClass.__dict__)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    # print("\n=== Copy Demonstration ===")
    # print("TODO: Implement shallow copy and deep copy demonstration")

    books = [
        ["The Way of the Shepard", "High Output Management"], ["The Wealth of Nations", "The Intelligent Investor"]
    ]

    shallow_books = copy(books)
    deep_books = deepcopy(books)

    books[1][0] = "Animal Farm"

    print(f"Original list: {books}")
    print(f"Shallow copy: {shallow_books}")
    print(f"Deep Copy: {deep_books}")

    # Shallow copying and deep copying both create new outer list, while where they differ lies in the inner lists. In
    # regard to shallow copying, the inner list is shared with the original list, while the deep copying creates a
    # separate inner list independent of the original list.


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    # print("=== Unit 1 OOP Assignment ===")
    #
    # print("\nTODO: Create and test your parent object")
    #
    # print("\nTODO: Create and test your child object")

    book1 = ParentClass("Let My People Go Surfing", "Yvon C.")

    book1.display_info()
    book1.display_library()

    eBook1 = ChildClass("The Way of the Shepard", "Kevin L.", "PDF", 20)

    eBook1.display_info()
    eBook1.display_file_info()

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()