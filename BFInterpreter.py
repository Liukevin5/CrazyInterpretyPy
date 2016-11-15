print("                      /^--^\     /^--^\     /^--^\ ")
print("                      \____/     \____/     \____/ ")
print("                     /      \   /      \   /      \ ")
print("                    |        | |        | |        | ")
print("                     \__  __/   \__  __/   \__  __/ ")
print("|^|^|^|^|^|^|^|^|^|^|^|^\ \^|^|^|^/ /^|^|^|^|^\ \^|^|^|^|^|^|^|^|^|^|^|^| ")
print("| | | | | | | | | | | | |\ \| | |/ /| | | | | | \ \ | | | | | | | | | | | ")
print("########################/ /######\ \###########/ /####################### ")
print("| | | | | | | | | | | | \/| | | | \/| | | | | |\/ | | | | | | | | | | | | ")
print("|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_| ")
print()
print()
print()

tape = [0] * 1000
index = 0;
tape[994] = 1


def display():
    print('%9s' % 'Index:', end="")
    if index > 3 and index < 993:
        for i in range(7):
            print('%9s' % str(index + i - 3), end="")
        print()

        print('%9s' % 'int: ', end="")
        for i in range(7):
            print('%9s' % str(tape[index + i - 3]), end="")
        print()

        print('%9s' % 'pointer: ', end="")
        for i in range(7):
            if index == i + index - 3:
                print('%9s' % '^', end="")
            else:
                print('%9s' % ' ', end="")
        print()

    elif index > 992:

        for i in range(7):
            print('%9s' % str(i + 993), end="")

        print()
        print('%9s' % 'int: ', end="")
        for i in range(7):
            print('%9s' % str(tape[i + 993]), end="")

        print()
        print('%9s' % 'pointer: ', end="")

        for i in range(7):
            if index == i + 993:
                print('%9s' % "^", end="")
            else:
                print('%9s' % " ", end="")
        print()
    else:
        for i in range(7):
            print('%9s' % str(i), end="")
        print()

        print('%9s' % "int: ", end="")
        for i in range(7):
            print('%9s' % str(tape[i]), end="")
        print()
        print('%9s' % 'pointer: ', end="")

        for i in range(7):
            if index == i:
                print('%9s' % "^", end="")
            else:
                print('%9s' % ' ', end="")
        print()


def interactive():
    global index
    command_ptr = 0
    c = str(input("enter command(s)"))
    commands = list(c)

    while command_ptr < len(commands):

        char = commands[command_ptr]

        if char == '+':

            tape[index] += 1
        elif char == '-':

            tape[index] -= 1
        elif char == '>':

            index += 1
        elif char == '<':

            index -= 1
        elif char == ':':

            print(tape[index])
        elif char == '.':

            print(chr(int(tape[index])))

        elif char == '{':

            count1 = 1
            if tape[index] == 0:

                while count1 != 0:

                    command_ptr += 1

                    if commands[command_ptr] == '{':
                        count1 += 1
                    if commands[command_ptr] == '}':
                        count1 -= 1



        elif char == '}':

            count2 = 0

            while(True):

                if commands[command_ptr] == '{':
                    count2 += 1

                if commands[command_ptr] == '}':
                    count2 -= 1

                command_ptr = command_ptr - 1

                if count2 == 0:
                    break
        else:
            break

        command_ptr += 1


while True:
    display()
    interactive()

