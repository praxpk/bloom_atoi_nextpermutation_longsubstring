import logging
import argparse
import random
import string


def longest_substring(query_string: str) -> int:
    """
    This method returns the length of the longest substring without repeating characters
    :param query_string: The string for which we need to find the longest substring without repeating characters
    :return: int: the length of the longest substring that has no repeating characters
    """
    left = 0
    # creating a set to store unique characters encountered by the left end of the window
    unique = set()
    result = 0

    query_string = query_string.lower()

    if ' ' in query_string:
        print("Please provide one word only, not many.")
        raise ValueError

    for right in range(len(query_string)):
        if query_string[right] not in unique:
            # adding to set
            unique.add(query_string[right])
        else:
            # if character already in set then shrink the window
            # by removing the character at left side of the window till
            # character at the right end of the window can be added
            while query_string[right] in unique:
                unique.remove(query_string[left])
                left += 1
            unique.add(query_string[right])

        result = max(result, len(unique))

    return result


def generate_random_string() -> str:
    # get a random string size between 2 and 20
    string_size = random.randint(2, 20)
    logger.info("Generating random string of size {}".format(string_size))
    # generate string
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(string_size))


def main():
    parser = argparse.ArgumentParser(description='Given a string, this program returns the length of the longest'
                                                 'substring with non repeating characters')
    parser.add_argument('--random', action='store_true', help='Use a randomly generated string and '
                                                              'find its longest substring with non repeating'
                                                              'characters.\n'
                                                              'Example: python longest_substring.py --random.')
    parser.add_argument('--word', action='store', help='Provide the word for which you want to find the longest '
                                                       'substring with non repeating characters.\n Example:'
                                                       ' python longest_substring.py --word aacbklmjjixmlp')
    args = parser.parse_args()
    if args.random and args.word:
        print("Please use one argument only, either --random or --word. Not both together.")
        logger.info("Exiting program as user used both --random and --word arguments")

    elif args.random and not args.word:
        random_string = generate_random_string()
        logger.info("Generated random string: {}".format(random_string))
        length_of_substring = longest_substring(random_string)
        print("Length of longest substring without repeating characters for {} = {}".format(random_string,
                                                                                            length_of_substring))
    elif args.word and not args.random:
        logger.info("User provided string: {}".format(args.word))
        try:
            length_of_substring = longest_substring(args.word)
            print("Length of longest substring without repeating characters for {} = {}".format(args.word,
                                                                                                length_of_substring))
        except ValueError:
            logger.exception("User provided multiple words")
    else:
        parser.print_help()
        parser.exit()


if __name__ == '__main__':
    logging.basicConfig(filename='longest_substring.log', filemode='a', level=logging.DEBUG,
                        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)
    main()
