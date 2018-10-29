import math
import random


# EX.1
def ex1():
    print("EX.1: Add up all the integer numbers from 1 to 1000000")
    result = sum(x for x in range(1, 1001))
    print("Result: {}".format(result))


# EX.2
def ex2():
    print("EX.2: Check if given segments can form a triangle")
    print("Please input variables, to check if You can make triangle out of them (a,b,c)")
    a = int(input())
    b = int(input())
    c = int(input())
    if (a + b) > c \
            and (a + c) > b \
            and (b + c) > a:
        print("That variables can form a triangle")
    else:
        print("That variables can't form a triangle")


# EX.3
def ex3():
    result = 0

    print("EX.3 Find such numbers, in range 1:100, that fulfills such condition: a^2+b^2=c^2")
    for a in range(1, 101):
        for b in range(1, 101):
            product = math.sqrt(a * a + b * b)
            if 1 <= product <= 100 \
                    and product == int(product):
                result += 1
    print("There are: {} such numbers".format(result))


# EX.4
def ex4():
    print("EX.4: Create time calculator, to add up given minutes to given current time");
    print("Input numbers as follows : hour, minutes, increment in minutes")

    hours = int(input())
    minutes = int(input())
    minutes_increment = int(input())
    time_calculated: int = hours * 60 + minutes + minutes_increment

    if time_calculated % 60 <= 9:
        minutes_formatted = "0" + str(time_calculated % 60)
    else:
        minutes_formatted = time_calculated % 60
    if time_calculated // 60 >= 25:
        time_calculated -= 24 * 60

    print(
        "It is: {}:{}, in {} minutes it will be {}:{}".format(hours, minutes, minutes_increment,
                                                              time_calculated // 60, minutes_formatted))


# EX.5
def ex5():
    player_a_position = 1
    player_b_position = 1

    print("EX.5: write simple board game simulator aka Ludo")
    while player_a_position < 1000 and player_b_position < 1000:
        player_a_position += random.randint(1, 6)
        if player_a_position == player_b_position:
            player_b_position = 1

        player_b_position += random.randint(1, 6)
        if player_a_position == player_b_position:
            player_a_position = 1

    if player_a_position >= 1000:
        print("Player A won!")
    else:
        print("Player B won!")


def switch(argument: int):
    switcher = {
        1: ex1,
        2: ex2,
        3: ex3,
        4: ex4,
        5: ex5,
    }
    func = switcher.get(argument, lambda: "No such exercise!")
    func()


if __name__ == "__main__":
    print("Chose which exercise to run: 1/2/3/4/5")
    exercise = input()
    switch(int(exercise))
