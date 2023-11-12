def swap(list_one):
    """
    Function that swaps the first and last elements of the list, regardless of length
    :param list_one: a list of at least two elements
    :return: the same list with the first and last elements swapped
    """
    num_elements = len(list_one)
    place_last_variable = num_elements-1
    og_last_variable = list_one.pop(place_last_variable)
    og_first_variable = list_one[0]
    list_one[0] = og_last_variable
    list_one.append(og_first_variable)
    return list_one


def rotate_left(list_one):
    """
    Given a list of ints length 3, return a list with the elements "rotated left" so [1, 2, 3] yields [2, 3, 1].
    :param list_one: A list consisting of exactly three integers
    :return: a list where all the elements have been shifted 1 place to the left
    """
    first_element = list_one.pop(0)
    list_one.append(first_element)
    return list_one


def max_end(list_one):
    """
    This function will find if the first or last element of an list is larger, then set all the elements
    of that list to that value.
    :param list_one: A list consisting of three elements - all integers
    :return: A list where all the elements are the larger of the first or last element of the original list
    """
    first_element = list_one[0]
    last_element = list_one[2]
    if list_one[0] > list_one[2]:
        list_one = [first_element, first_element, first_element]
    elif list_one[2] > list_one[0]:
        list_one = [last_element, last_element, last_element]
    return list_one

def main():
    list_one = [1,2,3]
    print(list_one)
    print(swap(list_one))
    list_one = [1,2,3]
    print(list_one)
    print(rotate_left(list_one))
    list_one = [1, 2, 3]
    print(list_one)
    print(max_end(list_one))


main()
