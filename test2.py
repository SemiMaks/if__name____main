# print выполнится лишь в том случае,
# если к функции будет фактическое обращение,
# а если модуль импортировать - этого не произойдёт.

def main():
    print("It's from main function")


if __name__ == '__main__': main()
