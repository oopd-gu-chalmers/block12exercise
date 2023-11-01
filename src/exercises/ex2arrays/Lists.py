# package exercises
#
#
# Program to exercise lists
#
# See:
# - ListBasics
#


# THE INPUT FUNCTIONS
def get_list_of_ints_from_user():
    input_as_string = input("Input 5 integers (space between, then enter) > ")
    the_int_strs = input_as_string.split(" ")
    the_ints = []
    for int_str in the_int_strs:
        the_ints.append(int(int_str))
    return the_ints


def get_value_from_user():
    return int(input("Input a value to find > "))


# THE OUTPUT FUNCTIONS
def print_index_to_user(the_index, the_value):
    print(f"Value {the_value} is at index {the_index}")


def print_not_found_to_user(the_value):
    print(f"Value {the_value} not found")


def print_result_to_user(the_index, the_value):
    if the_index is None:
        print_not_found_to_user(the_value)
    else:
        print_index_to_user(the_index, the_value)
    pass


# THE ALGORITHM
def find_index_of_value(a_list, a_value):
    for i in range(len(a_list)):
        if a_value == a_list[i]:
            return i


# THE TOP-LEVEL BEHAVIOR
def list_basics_program():
    # INPUT
    the_list = get_list_of_ints_from_user()
    the_value = get_value_from_user()
    # PROCESS
    the_index = find_index_of_value(the_list, the_value)
    # OUTPUT
    print_result_to_user(the_index, the_value)


# Recommended way to make module executable
if __name__ == "__main__":
    list_basics_program()
