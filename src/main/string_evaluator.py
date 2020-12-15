# Created by Leon Hunter at 3:57 PM 10/23/2020
class StringManipulator(object):
    def get_hello_world(self):
        return "Hello World"

    def concatenate(self, value_to_be_added_to, value_to_add):
        return str(value_to_be_added_to) + str(value_to_add)

    def substring_inclusive(self, string_to_fetch_from, starting_index, ending_index):
        return string_to_fetch_from[starting_index:ending_index + 1]

    def substring_exclusive(self, string_to_fetch_from, starting_index, ending_index):
        substring = string_to_fetch_from[starting_index + 1:ending_index]
        return substring

    def compare(self, first_value, second_value):
        if first_value == False:
            first_value = 0
        elif first_value == True:
            first_value = 1
        if second_value == False:
            second_value = 0
        elif second_value == True:
            second_value = 1
        if str(first_value) == str(second_value):
            return True
        else:
            return False

    def get_middle_character(self, string_to_fetch_from):
        middle_index = len(string_to_fetch_from) // 2 + 1
        return string_to_fetch_from[middle_index]

    def get_first_word(self, string_to_fetch_from):
        split_string_list = string_to_fetch_from.split()
        return split_string_list[0]

    def get_second_word(self, string_to_fetch_from):
        split_string_list = string_to_fetch_from.split()
        return split_string_list[1]

    def reverse(self, string_to_be_reversed):
        return string_to_be_reversed[::-1]