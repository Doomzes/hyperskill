def remaining(a, b, c, d, e):
    print("")
    print("{} ml of water".format(a))
    print("{} ml of milk".format(b))
    print("{} g of coffee beans".format(c))
    print("{} disposable cups".format(d))
    print("${} of money".format(e))
    print("")
# показывает запасы

def action_buy():
    global stock_water
    global stock_milk
    global stock_coffee_b
    global money
    global cups
    print("")
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
    try:
        a = int(input())
        if a == 1:
            b = check(stock_water, stock_milk, stock_coffee_b, cups, 1)
            if b == 1:
                stock_water -= 250
                stock_coffee_b -= 16
                stock_milk -= 0
                money += 4
                cups -= 1
                print("I have enough resources, making you a coffee!")
            else:
                pass
        elif a == 2:
            b = check(stock_water, stock_milk, stock_coffee_b, cups, 2)
            if b == 1:
                stock_water -= 350
                stock_milk -= 75
                stock_coffee_b -= 20
                money += 7
                cups -= 1
            else:
                pass
        else:
            b = check(stock_water, stock_milk, stock_coffee_b, cups, 3)
            if b == 1:
                stock_water -= 200
                stock_milk -= 100
                stock_coffee_b -= 12
                money += 6
                cups -= 1
            else:
                pass
    except:
        pass
    print("")
# действие покупки


def action_fill():
    global stock_water
    global stock_milk
    global stock_coffee_b
    global cups
    print("")
    print("Write how many ml of water you want to add: ")
    add_water = int(input())
    stock_water += add_water
    print("Write how many ml of milk you want to add: ")
    add_milk = int(input())
    stock_milk += add_milk
    print("Write how many grams of coffee beans you want to add: ")
    add_coffee_b = int(input())
    stock_coffee_b += add_coffee_b
    print("Write how many disposable cups you want to add: ")
    add_cups = int(input())
    cups += add_cups
# действие пополнение запасов


def action_take():
    global money
    print("I gave you ${}".format(money))
    money -= money
# действие снятия денег


def check(stock_water, stock_milk, stock_coffee_b, cups, number):
    info = []
    if number == 1:
        info.append(stock_water // resource_need['espresso_w'])
        info.append(1)
        info.append(stock_coffee_b // resource_need['espresso_c_b'])
        info.append(cups // 1)
    elif number == 2:
        info.append(stock_water // resource_need['latte_w'])
        info.append(stock_milk // resource_need['latte_m'])
        info.append(stock_coffee_b // resource_need['latte_c_b'])
        info.append(cups // 1)
    elif number == 3:
        info.append(stock_water // resource_need['cappuccino_w'])
        info.append(stock_milk // resource_need['cappuccino_m'])
        info.append(stock_coffee_b // resource_need['cappuccino_c_b'])
        info.append(cups // 1)
    if info[0] == 0:
        print("Sorry, not enough water!")
        return 0
    elif info[1] == 0:
        print("Sorry, not enough milk!")
        return 0
    elif info[2] == 0:
        print("Sorry, not enough coffee beans!")
        return 0
    elif info[3] == 0:
        print("Sorry, not enough cups!")
        return 0
    else:
        return 1


stock_water = 400
stock_milk = 540
stock_coffee_b = 120
cups = 9
money = 550

resource_need = {'espresso_w': 250,
                 'espresso_m': 0,
                 'espresso_c_b': 16,
                 'latte_w': 350,
                 'latte_m': 75,
                 'latte_c_b': 20,
                 'cappuccino_w': 200,
                 'cappuccino_m': 100,
                 'cappuccino_c_b': 12,
                 }


while True:
    print("Write action (buy, fill, remaining, take, exit): ")
    answer = input()
    if answer == "buy":
        action_buy()
    elif answer == "fill":
        action_fill()
    elif answer == "remaining":
        remaining(stock_water, stock_milk, stock_coffee_b, cups, money)
    elif answer == "take":
        action_take()
    else:
        break
