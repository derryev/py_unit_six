
def create_list(starting, ending):
    """
    Ex. create_list(4, 10) would return [4, 5, 6, 7, 8, 9, 10]
    :param starting: an integer number
    :param ending: A number greater than the starting number
    :return: list of numbers starting with the first number and going up to and including the second number
    """
    created_list = []
    for x in range(starting,ending+1):
        created_list.append(x)
    return created_list


def find_odds(numbers):
    """
    Ex. find_odds([13, 2, 9, 14, 16, 18, 9, 11, 21]) would return [13, 9, 9, 11, 21]
    :param numbers: a list of numbers
    :return: a new list consisting of only the odd numbers from the original list
    """
    odds_list = []
    for number in numbers:
        if (number % 2) != 0:
            odds_list.append(number)
    return odds_list


def remove_duplicates(list):
    """
    Ex. remove_duplicates([1, 2, 3, 3, 4, 5, 6, 6, 7, 7, 7])  would return  [1, 2, 3, 4, 5, 6, 7]
    remove_duplicates9[‘apple’, ‘banana’, ‘banana’, ‘cherry’]) would return [‘apple’, ‘banana’, ‘cherry’]
    :param list: a list of either numbers or words
    :return: a list that is the same as the list given in the parameter, but without any duplicates
    """
    no_duplicate_list = []
    for item in list:
        if item not in no_duplicate_list:
            no_duplicate_list.append(item)
    return no_duplicate_list


def main():
    print(create_list(8, 20))
    print(find_odds([13, 2, 9, 14, 16, 18, 9, 11, 21]))
    numbers_list = [1, 2, 3, 3, 4, 5, 6, 6, 7, 7, 7]
    words_list = ["apple", "banana", "banana", "cherry"]
    print(remove_duplicates(words_list))
main()