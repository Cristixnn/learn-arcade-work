import re


# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def main():
    # Dictionary list.
    dictionary_list = open("dictionary.txt")

    name_list = []

    for line in dictionary_list:
        line = line.strip()

    dictionary_list.close()

    # Linear Search
    print("--- Linear search ---")
    # My file.
    open("AliceInWonderLand200.txt")
    for file in dictionary_list:
        file = file.strip()
        word_list = split_line(dictionary_list)
        return word_list



main()
