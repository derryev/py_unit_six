
import random


def generate_birthdays():
    birthday_list = []
    for x in range(23):
        birthday = random.randint(1, 365)
        birthday_list.append(birthday)
    return birthday_list


def is_duplicate(birthday_list):
    for birthday in birthday_list:
        for x in birthday_list[birthday+1:24]:
            if birthday == x:
                return True
    return False


def main():
    while True:
        times_run_sim = input(print("How many times would you like to simulate the birthday problem?"))
        if times_run_sim.isdigit() is False or times_run_sim.isdecimal() is False:
            print("Please enter a positive, whole number in digits.")
        else:
            break
    print(times_run_sim)
    duplicate_counter = 0
    for x in range(int(times_run_sim)):
        birthday_list = generate_birthdays()
        #print(birthday_list)
        if is_duplicate(birthday_list) is True:
            print("true")
            duplicate_counter = duplicate_counter+1
        elif is_duplicate(birthday_list) is False:
            print("False")
    print(duplicate_counter)
    proportion_duplicate_lists = duplicate_counter/int(times_run_sim)
    print("There were two of the same birthday")


main()
