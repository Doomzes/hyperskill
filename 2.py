import random

def choose_level():
    global level

    while True:
        print("Which level do you want? Enter a number:")
        print("1 - simple operations with numbers 2-9")
        print("2 - integral squares of 11-29")
        try:
            level = int(input())
            if 1 <= level <= 2:
                setteings.append(level)
                break
            else:
                print("Incorrect format.")
        except ValueError:
            print("Incorrect format.")


def random_level_1():
    global equation
    global math_operation
    random.shuffle(math_operation)
    random.randrange(2, 10, 1)
    equation = random.randrange(2, 10, 1), random.randrange(2, 10, 1)


def random_level_2():
    global squares
    squares = random.randrange(11, 30, 1)


def action_1(answer):
    global i
    global point
    if math_operation[1] == "+":
        if answer == equation[0] + equation[1]:
            print("Right!")
            point += 1
        else:
            print("Wrong!")
    elif math_operation[1] == "-":
        if answer == equation[0] - equation[1]:
            print("Right!")
            point += 1
        else:
            print("Wrong!")
    elif math_operation[1] == "*":
        if answer == equation[0] * equation[1]:
            print("Right!")
            point += 1
        else:
            print("Wrong!")
    i += 1


def action_2(answer):
    global i
    global point
    if answer == squares ** 2:
        print("Right!")
        point += 1
    else:
        print("Wrong!")
    i += 1


def save(name, point, lvl, desc):
    file = open('results.txt', 'a', encoding='utf-8')
    file.writelines("{}: {}/5 in level {} ({})".format(name, point, lvl, desc) + '\n')
    file.close()


point = 0
i = 0
squares = 0
equation = []
setteings = []
math_operation = ["+", "-", "*"]


while True:
    choose_level()
    if level == 1:
        setteings.append("1 - simple operations with numbers 2-9")
        while i < 5:
            random_level_1()
            while True:
                print("{} {} {}".format(equation[0], math_operation[1], equation[1]))
                try:
                    answer = int(input())
                    action_1(answer)
                    break
                except ValueError:
                    print("Incorrect format.")
        break
    else:
        setteings.append("2 - integral squares of 11-29")
        while i < 5:
            random_level_2()
            while True:
                print("{}".format(squares))
                try:
                    answer = int(input())
                    action_2(answer)
                    break
                except ValueError:
                    print("Incorrect format.")
        break




print("Your mark is {}/5. Would you like to save the result? Enter yes or no.".format(point))
answer_save = input()
if answer_save in ["Yes","yes","YES","y"]:
    print("What is your name?")
    name = input()
    save(name, point, setteings[0], setteings[1])
    print('The results are saved in "results.txt".')
else:
    exit()