# write your code here
import sys

msg_0 = "Enter an equation\n"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):\n"
msg_5 = "Do you want to continue calculations? (y / n):\n"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)\n"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)\n"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)\n"
ops = ["+", "-", "*", "/"]
memory = 0.0


def aggregation(x, y, oper):
    if oper == "+":
        return x + y
    elif oper == "-":
        return x - y
    elif oper == "*":
        return x * y
    elif oper == "/" and y != 0:
        return x / y
    else:
        return msg_3

def check(v1, v2, v3):
    msg = ""
    if one_digit(v1) and one_digit(v2) == True:
        msg += msg_6
    if v1 == 1 or v2 == 1 and v3 == "*":
        msg += msg_7
    if v1 == 0 or v2 == 0 and v3 in ["*", "+", "-"]:
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


def one_digit(a):
    if -10 < a < 10 and a.is_integer() == True:
        return True
    return False


while True:
    calc = input(msg_0)
    x, oper, y = calc.split()
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    try:
        x = float(x) #if "." in x else int(x)
        y = float(y) #if "." in y else int(y)
        if oper not in ops:
            print(msg_2)
            continue
    except ValueError:
        print(msg_1)
    else:
        result = aggregation(x, y, oper)
        check(x, y, oper)
        if result == msg_3:
            print(result)
            continue
        print(float(result))
        while True:
            decision = input(msg_4)
            if decision == "y" and one_digit(result) is True:
                msg_index = [msg_10, msg_11, msg_12]
                i = 0
                while i <= 3:
                    if i <= 2:
                        a = input(msg_index[i])
                    if a == "y" and i <= 2:
                        i += 1
                    elif a != "n" and a != "y":
                        i += 1
                    elif a == "n":
                        break
                    else:
                        memory = float(result)
                        break
                break
            elif decision != "n" and decision != "y":
                continue
            elif decision == "y" and one_digit(result) is False:
                memory = float(result)
                break
            else:
                break
        while True:
            another_decision = input(msg_5)
            if another_decision == "y":
                break
            elif another_decision != "n":
                continue
            else:
                sys.exit()
        continue
