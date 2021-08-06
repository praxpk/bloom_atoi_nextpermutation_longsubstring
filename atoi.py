"""
The idea is to think of this as a state diagram, we first encounter empty characters, this is state 0,
as soon as we encounter a positive or negative sign we enter into state 1 and then after that if we encounter
a number we enter into state 2. Now at each state the following can occur:

Encounter a white space
Encounter a negative sign or positive sign
Encounter a number
Encounter a character that is none of the above

IF at state 0:
Encounter a white space => do nothing
Encounter a negative sign or positive sign => go to state 2 and declare negative boolean as true
Encounter a number => go to state 2 and add character to string
Encounter a character that is none of the above =>return 0

IF at state 1:
Encounter a white space => return 0
Encounter a negative sign or positive sign => return 0
Encounter a number => got to state 2 and add character to string
Encounter a character that is none of the above =>return 0

IF at state 2:
Encounter a white space => break out of the while loop
Encounter a negative sign or positive sign => break out of the while loop
Encounter a number => add to string
Encounter a character that is none of the above => break out of the loop

"""

import logging


def myAtoi(s: str) -> int:
    state = 0
    index = 0
    negative = False
    str_num = ""
    string_length = len(s)
    while index < string_length:
        # state 0 represents " " characters
        if state == 0:
            # we encounter a white space character
            if s[index] == ' ':
                state = 0
            # we encounter a negative or positive sign
            elif s[index] == "+":
                state = 1
            elif s[index] == "-":
                state = 1
                negative = True
            # we encounter a number
            elif s[index].isdigit():
                state = 2
                str_num += s[index]
            # we encounter a non digit
            elif not s[index].isdigit():
                return 0

        # state 1 represents having encountered a "+" or "-" sign
        elif state == 1:
            # we encounter a white space character
            if s[index] == " ":
                return 0
            # we encounter a negative or positive sign
            elif s[index] == "+" or s[index] == "-":
                return 0
            # we encounter a number
            elif s[index].isdigit():
                str_num += s[index]
                state = 2
            # we encounter a non digit
            else:
                return 0
        # state 2 represents having encountered a number
        elif state == 2:
            # we encounter a white space character
            if s[index] == ' ':
                break
            # we encounter a negative or positive sign
            elif s[index] == "-" or s[index] == "+":
                break
            # we encounter a number
            elif s[index].isdigit():
                str_num += s[index]
            # we encounter a non digit
            else:
                break

        index += 1

    # printing out results and checking if its greater than or lesser than limit
    if not str_num:
        return 0
    value = int(str_num)
    if negative:
        value *= (-1)
        if value < (-1) * (2 ** 31):
            return (-1) * (2 ** 31)

    if value > ((2 ** 31) - 1):
        return (2 ** 31) - 1
    else:
        return value


def main():
    print("This program converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).")
    print("Type exit if you wish to quit the program")
    while True:
        input_string = input()
        if input_string.lower() == "exit":
            logger.info("Exiting program")
            return

        logger.info("User provided: {}".format(input_string))
        output = myAtoi(input_string)
        logger.info("Response: {}".format(output))
        print(output)


if __name__ == '__main__':
    logging.basicConfig(filename='myAtoi.log', filemode='a', level=logging.DEBUG,
                        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)
    main()
