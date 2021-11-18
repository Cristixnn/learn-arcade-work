import re


# This function takes in a line of text and returns
# a list of words in the line.

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def main():
    """ Read in lines from a file """
    dictionary_file = open("dictionary.txt")
    dictionary_list = []
    for line in dictionary_file:
        line = line.strip()
        dictionary_list.append(line)
    dictionary_file.close()
    print("--- Linear Search ---")

    my_file = open("AliceInWonderLand200.txt")
    line_number = 0
    for line in my_file:
        line_number += 1
        word_list = split_line(line)
        for word in word_list:

            # Start in beginning of list
            current_list_position = 0

            # Loop until you reach the end of the list, or the value at the
            # current position is equal to the key
            while current_list_position < len(dictionary_list) \
                    and dictionary_list[current_list_position] != word.upper():

                # Advance next item in the list
                current_list_position += 1

            if current_list_position == len(dictionary_list):
                print("line " + str(line_number) + " Possible Misspelled word: " + word)
    my_file.close()

    print("--- Binary Search ---")

    my_file = open("AliceInWonderLand200.txt")
    line_number = 0
    for line in my_file:
        line_number += 1
        word_list = split_line(line)
        for word in word_list:
            lower_bound = 0
            upper_bound = len(dictionary_list) - 1
            found = False

            # Loops until we find the item, or upper and lower bounds meet
            while lower_bound <= upper_bound and not found:

                # Finds middle position
                middle_pos = (lower_bound + upper_bound) // 2


                # Find out what we are looking for
                if dictionary_list[middle_pos] < word.upper():
                    lower_bound = middle_pos + 1
                elif dictionary_list[middle_pos] > word.upper():
                    upper_bound = middle_pos - 1
                else:
                    found = True
            if not found:
                print("line " + str(line_number) + " Possible Misspelled word: " + word)
    my_file.close()


main()
