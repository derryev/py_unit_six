
import random


def get_input_how_many():
    """
    Gets input on how many times a user wants to run the birthday simulation, not returning the user's input until they
    enter a positive and whole number by using a while loop to check if the input is digits and not decimals (which
    negative values also register as).
    :return: How many times the user wants to run the birthday simulation (string)
    """
    while True:
        times_run_sim = input("How many times would you like to simulate the birthday problem? ")
        if times_run_sim.isdigit() is False or times_run_sim.isdecimal() is False:
            print("Please enter a positive, whole number in digits.")
        else:
            return times_run_sim


def generate_birthdays():
    """
    Generates a list of 23 random numbers from 1-365, simulating a class of 23 people with random birthdays
    throughout the 365-day year.
    :return: a list of random numbers representing the random birthdays of 23 people in a class.
    """
    birthday_list = []
    for x in range(23):
        birthday = random.randint(1, 365)
        birthday_list.append(birthday)
    return birthday_list


def is_duplicate(birthday_list):
    """
    For each birthday in the birthday list, it compares said birthday with every other birthday after it to check if it
    is the same as any other birthday in the list (if the two generated numbers are equal), which determines if
    the simulated class has any duplicate birthdays in it
    :param birthday_list: a list of random numbers representing the random birthdays of 23 people in a class.
    :return: True if a duplicate birthday is found in the list, and False if no duplicate birthdays are found after
    going through the entire list, which will allow the program to count how many lists with duplicate birthdays were
    discovered.
    """
    for birthday in birthday_list:
        for x in birthday_list[birthday+1:24]:
            if birthday == x:
                return True
    return False


def main():
    times_run_sim = get_input_how_many()
    duplicate_counter = 0
    for x in range(int(times_run_sim)):                                                                                 # this for loops repeats the list generation and duplicate determination as many times as the user wanted to run the simulation
        birthday_list = generate_birthdays()
        if is_duplicate(birthday_list) is True:
            duplicate_counter = duplicate_counter+1                                                                     # if a list is found to have duplicate birthdays, 1 is added to a counter that keeps track of how many duplicate birthdays were found
    if int(times_run_sim) == 1:                                                                                         # if and elif statements to ensure grammatically correct output based on if the user ran only 1 or multiple class simulations
        print("Out of 1 simulated class, " + str(duplicate_counter) + " had duplicate birthdays.")
    elif int(times_run_sim) != 1:
        print("Out of " + times_run_sim + " simulated classes, " + str(duplicate_counter) + " had duplicate birthdays.")
    proportion_duplicate_lists = (duplicate_counter / int(times_run_sim))*100                                           # calculates the decimal proportion of duplicate lists and then multiplies by 100 so that the number will work with the language of the later output statement
    print("This means there were duplicate birthdays about "+str(round(proportion_duplicate_lists, 4)) +                # chose to round proportion to four decimal points for more concise and clean output
          " percent of the time.")


main()
