
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
    birthday_list = generate_birthdays()
    print(birthday_list)
    if is_duplicate(birthday_list) is True:
        print("true")
    else:
        print("False")

main()
