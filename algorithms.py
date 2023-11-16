
def add_numbers(numbers):
    """
    Ex. add_numbers([9, 5, 11, 6, 1, 15]) returns 47
    :param numbers: a list of numbers
    :return: the sum of all the numbers in the list
    """
    sum_of_list = 0
    for number in numbers:
        sum_of_list = sum_of_list + number
    print("Sum of the list:")
    return sum_of_list

def get_max(numbers_2):
    """
    Ex. get_max([45, 23, 99, 34, 67, 98, 0]) returns 99
    :param numbers: a list of numbers
    :return: The largest number in the list
    """
    max_number = numbers_2[0]
    for number in numbers_2:
        if number >= max_number:
            max_number = number
    print("Maximum number:")
    return max_number

def get_min(numbers_3):
    """
    Ex. get_min([45, 23, 99, 34, 67, 98, 0]) returns 0
    :param numbers: a list of numbers
    :return: The smallest number in the list
    """
    min_number = numbers_3[0]
    for number in numbers_3:
        if number <= min_number:
            min_number = number
    print("Minimum number:")
    return min_number


def merge(list1, list2):
    """
        Ex. merge([3, 4, 7, 9], [1, 5, 8, 11]) return [3, 4, 7, 9, 1, 5, 8, 11]
        :param list1: a list in sorted order
        :param list2: a second list in sorted order
        :return: a single list consisting of both smaller lists combined.
        """
    new_list = list1
    for number in list2:
        new_list.append(number)
    print("List 1 and 2 merged:")
    return new_list


def merge_in_order(list1, list2):
    """
    Ex. merge([3, 4, 7, 9], [1, 5, 8, 11]) return [1, 3, 4, 5, 7, 8, 9, 11]
    :param list1: a list in sorted order
    :param list2: a second list in sorted order
    :return: a single list consisting of both smaller lists combined in sorted order.
    """
    new_list = list1
    for number in list2:
        new_list.append(number)
    new_list = sorted(new_list)
    print("List 1 and 2 merged in ascending order:")
    return new_list

def main():
    print(add_numbers([9, 5, 11, 6, 1, 15]))
    print(get_max([45, 23, 99, 34, 67, 98, 0]))
    print(get_min([45, 23, 99, 34, 67, 98, 0]))
    print(merge([3, 4, 7, 9], [1, 5, 8, 11]))
    print(merge_in_order([3, 4, 7, 9], [1, 5, 8, 11]))

main()