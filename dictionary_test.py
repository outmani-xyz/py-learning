"""
Python Dictionary Test
----------------------
This file contains exercises to test your understanding of Python dictionaries.
Complete each section by writing code where indicated.
"""

def test_basics():
    print("--- Section 1: Basics ---")
    # 1. Create an empty dictionary named 'my_dict'
    my_dict = {}

    # 2. Add the following key-value pairs to 'my_dict':
    #    "name": "Alice"
    #    "age": 25
    #    "city": "New York"
    my_dict["name"] = "Alice"
    my_dict["age"] = 25
    my_dict["city"] = "New York"

    # 3. Print the value associated with the key "name"
    print(my_dict["name"])

    # 4. Update the "age" to 26
    my_dict["age"] = 26

    # 5. Add a new key "job" with value "Engineer"
    my_dict["job"] = "Engineer"

    # 6. Print the modified dictionary
    print(my_dict)
    
    # Validation (Do not key)
    # expected = {'name': 'Alice', 'age': 26, 'city': 'New York', 'job': 'Engineer'}
    print("\n[Your Output Should Match Expected Dictionary above check logic if you implement it]")


def test_methods():
    print("\n--- Section 2: Methods ---")
    student = {
        "id": 101,
        "name": "Bob",
        "courses": ["Math", "Science"],
        "grade": "A"
    }

    # 1. Use the .get() method to print the value of "name"
    print(student.get("name"))

    # 2. Use the .get() method to try to get a key "GPA", providing a default value of 0.0
    #    Print the result.
    # TODO: write code here

    # 3. Print all the keys in the dictionary using .keys()
    # TODO: write code here

    # 4. Print all the values in the dictionary using .values()
    # TODO: write code here

    # 5. Print all key-value pairs using .items()
    # TODO: write code here

    # 6. Remove the key "grade" using .pop() and print the removed value
    # TODO: write code here


def test_iteration():
    print("\n--- Section 3: Iteration ---")
    country_capitals = {
        "France": "Paris",
        "Japan": "Tokyo",
        "USA": "Washington D.C."
    }

    # 1. Loop through the dictionary and print each country (key)
    # TODO: write code here

    # 2. Loop through the dictionary and print each capital (value)
    # TODO: write code here

    # 3. Loop through the dictionary and print "The capital of [Country] is [Capital]"
    # TODO: write code here


def test_nested_dictionaries():
    print("\n--- Section 4: Nested Dictionaries ---")
    # 1. Create a dictionary named 'employees' where:
    #    - The keys are employee IDs (integers like 1, 2)
    #    - The values are dictionaries containing 'name' and 'role'
    #    Example: 1: {"name": "John", "role": "Dev"}, 2: {"name": "Jane", "role": "PM"}
    # TODO: write code here

    # 2. Access and print the 'role' of employee with ID 1
    # TODO: write code here

    # 3. Add a new employee with ID 3, name "Sam", role "Designer"
    # TODO: write code here


if __name__ == "__main__":
    test_basics()
    test_methods()
    test_iteration()
    test_nested_dictionaries()
