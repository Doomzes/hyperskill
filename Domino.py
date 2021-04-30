# Write your code here
import random


def main_menu(status):
    while True:
        print("=" * 70)
        print("Stock size: ", len(n_list))
        print("Computer pieces: ", len(value[0]))
        print('')
        if len(snake) <= 6:
            print(''.join(map(str, snake)))
        else:
            fst_three = ''.join(map(str, snake[:3]))
            lst_three = ''.join(map(str, snake[-3:]))
            print('{}...{}'.format(fst_three, lst_three))
        print('')
        print('Your pieces:')
        y_pieces(p_pieces)
        print('')
        if len(p_pieces) == 0:
            print("Status: The game is over. You won!")
            return
        elif len(c_pieces) == 0:
            print("Status: The game is over. The computer won!")
            return
        elif len(n_list) == 0:
            if len(c_pieces) > len(p_pieces):
                print("Status: The game is over. You won!")
                return
            elif len(c_pieces) < len(p_pieces):
                print("Status: The game is over. The computer won!")
                return
            else:
                print("Status: The game is over. It's a draw!")
                return
        else:
            status = p_turn(status)


def set(n_list):
    a = list()
    b = list()
    i = 0
    while i < 7:
        a.append(n_list[0])
        b.append(n_list[1])
        n_list.pop(0)
        n_list.pop(0)
        i += 1
    return a, b, n_list


def start_(a, b):
    a_max = max(a)
    b_max = max(b)
    if a_max > b_max:
        a.remove(a_max)
        return a, b, a_max, 'player'
    else:
        b.remove(b_max)
        return a, b, b_max, 'computer'


def y_pieces(p):
    number = 0
    for i in p_pieces:
        print("{}:{}".format(number + 1, p_pieces[number]))
        number += 1


def score_(snake):
    score_ = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
    }
    for i in str(snake):
        if i == '0':
            score_[0] += 1
        elif i == '1':
            score_[1] += 1
        elif i == '2':
            score_[2] += 1
        elif i == '3':
            score_[3] += 1
        elif i == '4':
            score_[4] += 1
        elif i == '5':
            score_[5] += 1
        elif i == '6':
            score_[6] += 1
    for i in str(c_pieces):
        if i == '0':
            score_[0] += 1
        elif i == '1':
            score_[1] += 1
        elif i == '2':
            score_[2] += 1
        elif i == '3':
            score_[3] += 1
        elif i == '4':
            score_[4] += 1
        elif i == '5':
            score_[5] += 1
        elif i == '6':
            score_[6] += 1
    return score_


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


def p_turn(s):
    if s == "player":
        print("Status: It's your turn to make a move. Enter your command: ")
        while True:
            getNumber = input()
            if (getNumber.replace("-", "")).isdigit() and int((getNumber.replace("-", ""))) <= len(p_pieces):
                if getNumber == '0':
                    p_pieces.append(n_list[0])
                    n_list.pop(0)
                    return "computer"
                elif getNumber[0:1] == '-':
                    if int(p_pieces[abs(int(getNumber)) - 1][1]) == (snake[0])[0]:
                        snake.insert(0, p_pieces[abs(int(getNumber)) - 1])
                        p_pieces.pop(int(getNumber[1:]) - 1)
                        return "computer"
                    elif int(p_pieces[abs(int(getNumber)) - 1][0]) == (snake[0])[0]:
                        orientation = p_pieces[abs(int(getNumber)) - 1]
                        snake.insert(0, orientation[::-1])
                        p_pieces.pop(abs(int(getNumber)) - 1)
                        return "computer"
                    else:
                        print('Illegal move. Please try again.')
                elif getNumber[0:1] != '-':
                    if int(p_pieces[int(getNumber) - 1][0]) == (snake[-1])[1]:
                        snake.append(p_pieces[int(getNumber) - 1])
                        p_pieces.pop(int(getNumber) - 1)
                        return "computer"
                    elif int(p_pieces[int(getNumber) - 1][1]) == (snake[-1])[1]:
                        orientation = p_pieces[abs(int(getNumber)) - 1]
                        snake.append(orientation[::-1])
                        p_pieces.pop(int(getNumber) - 1)
                        return "computer"
                    else:
                        print('Illegal move. Please try again.')
            else:
                print("Invalid input. Please try again.")
    else:
        print("Status: Computer is about to make a move. Press Enter to continue...")
        input()
        computer_score = score_(snake)
        h_score = dict()
        b = 0
        for i in c_pieces:
            new_pieces = ''.join(map(str, i))
            a = computer_score[int(new_pieces[0])] + computer_score[int(new_pieces[1])]
            h_score[b] = a
            b += 1
        while True:
            number_pieces = get_key(h_score, (max(h_score.values())))
            if int(c_pieces[number_pieces][1]) == (snake[0])[0]:
                snake.insert(0, c_pieces[number_pieces])
                c_pieces.pop(number_pieces)
                return "player"
            elif int(c_pieces[number_pieces][0]) == (snake[0])[0]:
                orientation = c_pieces[number_pieces]
                snake.insert(0, orientation[::-1])
                c_pieces.pop(number_pieces)
                return "player"
            elif int(c_pieces[number_pieces][0]) == (snake[-1])[1]:
                snake.append(c_pieces[number_pieces])
                c_pieces.pop(number_pieces)
                return "player"
            elif int(c_pieces[number_pieces][1]) == (snake[-1])[1]:
                orientation = c_pieces[number_pieces]
                snake.append(orientation[::-1])
                c_pieces.pop(number_pieces)
                return "player"
            else:
                del h_score[number_pieces]
                if len(h_score) == 0:
                    c_pieces.append(n_list[0])
                    n_list.pop(0)
                    return "player"


list_pieces = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6],
               [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [3, 3], [3, 4], [3, 5], [3, 6], [4, 4], [4, 5], [4, 6], [5, 5],
               [5, 6], [6, 6]]

random.shuffle(list_pieces)

n_list = list_pieces[:]
c_pieces = list()
p_pieces = list()
snake = list()
i = True

list_ = set(n_list)
c_pieces = list_[0]
p_pieces = list_[1]
n_list = list_[2]

value = start_(a=c_pieces, b=p_pieces)

snake.append(value[2])

status = value[3]

main_menu(status)