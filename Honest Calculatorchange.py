def restart():
    global result
    global memory
    global i
    print(msg_dict["4"])
    answer_1 = input()
    if answer_1 == "y":
        if is_one_digit(result) is True:
            msg_index = 10
            while True:
                print(msg_dict["{}".format(msg_index)])
                answer_3 = input()
                if answer_3 == "y":
                    if msg_index < 12:
                        msg_index = msg_index + 1
                    else:
                        memory = result
                        break
                else:
                    break
        else:
            memory = result
    elif answer_1 == "n":
        pass
    print(msg_dict["5"])
    answer_2 = input()
    if answer_2 == "y":
        pass
    elif answer_2 == "n":
        i = 1


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2) is True:
        msg = msg + msg_dict["6"]
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_dict["7"]
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_dict["8"]
    if msg != "":
        msg = msg_dict["9"] + msg
        print(msg)
    else:
        pass


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        output = True
    else:
        output = False
    return output

msg_dict = {"0": "Enter an equation",
            "1": "Do you even know what numbers are? Stay focused!",
            "2": "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
            "3": "Yeah... division by zero. Smart move...",
            "4": "Do you want to store the result? (y / n):",
            "5": "Do you want to continue calculations? (y / n):",
            "6": " ... lazy",
            "7": " ... very lazy",
            "8": " ... very, very lazy",
            "9": "You are",
            "10": "Are you sure? It is only one digit! (y / n)",
            "11": "Don't be silly! It's just one number! Add to the memory? (y / n)",
            "12": "Last chance! Do you really want to embarrass yourself? (y / n)"
            }

msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

msg_3 = "Yeah... division by zero. Smart move..."

msg_4 = "Do you want to store the result? (y / n):"

msg_5 = "Do you want to continue calculations? (y / n):"

msg_6 = " ... lazy"

msg_7 = " ... very lazy"

msg_8 = " ... very, very lazy"

msg_9 = "You are"

msg_10 = "Are you sure? It is only one digit! (y / n)"

msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"

msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

memory = 0.0
i = 0

while i == 0:
    print(msg_dict["0"])
    calc = input()
    calc_list = calc.split()
    x = calc_list[0]
    y = calc_list[2]
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    while True:
        try:
            x = float(x)
            y = float(y)
            if calc_list[1] in ["+", "-", "*", "/"]:
                check(x, y, calc_list[1])
                if calc_list[1] == "+":
                    result = x + y
                    print(result)
                elif calc_list[1] == "-":
                    result = x - y
                    print(result)
                elif calc_list[1] == "*":
                    result = x * y
                    print(result)
                elif calc_list[1] == "/":
                    if y == 0:
                        print(msg_dict["3"])
                        break
                    else:
                        result = x / y
                        print(result)
                restart()
                break
            else:
                print(msg_dict["2"])
        except ValueError:
            print(msg_dict["1"])
