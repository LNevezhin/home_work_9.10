from sys import path as path

path = path[0]
args = []

with open(path + '/registrations_.txt', 'r', encoding="utf-8") as file:
    for i, line, in enumerate(file):
        args.append(line.rstrip().split(" "))

        # print(args[i])
print(len(args))

args_valid = []
args_invalid = []


class NotEmailError(ValueError):
    def __init__(self):
        return


class NotNameError(ValueError):
    def __init__(self):
        return


def check_data():
    for i in range(len(args)):

        if len(args[i]) == 3:
            if args[i][0].isalpha():
                if (args[i][1].find("@") != - 1) and (args[i][1].find(".") != -1):
                    if 10 <= int(args[i][2]) <= 99:
                        args_valid.append(args[i])
                    else:
                        try:
                            raise ValueError
                        except ValueError:
                            args_invalid.append(args[i] + ["- Неверный возраст"])
                else:
                    try:
                        raise NotEmailError
                    except NotEmailError:
                        args_invalid.append(args[i] + ["- Неверный формат эл. почты"])
            else:
                try:
                    raise NotNameError
                except NotNameError:
                    args_invalid.append(args[i] + ["- Неверный формат имени"])
        else:
            try:
                raise ValueError
            except ValueError:
                args_invalid.append(args[i] + ["- Не все поля"])

    print(len(args_valid))
    print(args_invalid[100:120])
    return args_valid, args_invalid


agrs2 = check_data()
args_good = agrs2[0]
args_bad = agrs2[1]


with open(path + '/registrations_good.txt', 'w', encoding="utf-8") as file:
    for i, line, in enumerate(args_good):
        file.write(" ".join(line) + "\n")

with open(path + '/registrations_bad.txt', 'w', encoding="utf-8") as file:
    for i, line, in enumerate(args_bad):
        file.write(" ".join(line) + "\n")
