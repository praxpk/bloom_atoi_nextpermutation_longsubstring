from GeneralHashFunctions import RSHash, JSHash, ELFHash, BKDRHash, SDBMHash, DJBHash, DEKHash
import logging
import string
import random


class GenerateStrings:
    def __init__(self, size) -> None:
        self.size = size

    def __generate_string(self):
        """
        This method generates a string of random size (size between 2 and 12)
        :return: randomly generated string
        """
        # get a random string size between 2 and 12
        string_size = random.randint(2, 12)
        # generate string
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(string_size))

    def get_bag(self):
        """
        This method returns a bag of randomly generated strings of size given to the constructor.
        :return:
        """
        bag = []
        for i in range(self.size):
            bag.append(self.__generate_string())
        return bag


class BloomFilterStrings:
    """
    https://stackoverflow.com/questions/658439/how-many-hash-functions-does-my-bloom-filter-need

        n: Number of items = 1000
        p: False positive rate = 0.01 (1%)

        m: the number of bits in bloom filter
        k: the number of hash functions we need


    m = -n*ln(p) / (ln(2)^2) the number of bits => 9585
    k = m/n * ln(2) the number of hash functions => 6.64 ~ 7

    We need 7 hash functions, they are all obtained from:
    http://www.partow.net/programming/hashfunctions/index.html
    Author, Arash Partow provides the python implementation of all the algorithms, they are in the file
    GneneralHashFunctions.py

    """

    def __init__(self):
        self.__bloom_filters_list = []
        self.__bags_list = []
        self.__bits_size = 9585
        self.__hash_functions = [RSHash, JSHash, DEKHash, ELFHash, BKDRHash, SDBMHash, DJBHash]

    def add_bag(self, bag_of_words):
        """
        This method takes a bag of words, generates the bloom filter for it and adds the bag of words
        and bloom filter to their respective lists in this object.
        :param bag_of_words: a bag of words
        :return: None
        """
        bits = [0] * self.__bits_size
        for word in bag_of_words:
            for hash_function in self.__hash_functions:
                index = hash_function(word) % self.__bits_size
                bits[index] = 1

        self.__bloom_filters_list.append(bits)
        self.__bags_list.append(bag_of_words)

    def __get_index_list(self, queried_string):
        """
        The presence of a word is checked against the bloom filter. We take the word and get an index from each hash
        function, we check the bits in the bloom filter at these indices and verify if the word is present or not.
        This methods provides us with those indices for a queried word.
        :param queried_string: the word that will be queried
        :return:
        """
        index_list = []
        for hash_function in self.__hash_functions:
            index = hash_function(queried_string) % self.__bits_size
            index_list.append(index)

        return index_list

    def __check_bloom_filter(self, bloom_filter, index_list):
        """
        This method takes an index list and checks if the
        :param bloom_filter:
        :param index_list:
        :return:
        """
        for index in index_list:
            if bloom_filter[index] == 0:
                return False

        return True

    def check_string(self, queried_string: str) -> set:
        """
        This method checks if the query string is present in a bag by checking the bloom filter associated with the bag
        :param queried_string: check the string against all bloom filters.
        :return: a set of bags that contain the string according to the bloom filter (could have false positives)
        """
        index_list = self.__get_index_list(queried_string)
        set_of_bags = set()
        for i in range(len(self.__bloom_filters_list)):
            bloom_filter = self.__bloom_filters_list[i]
            if self.__check_bloom_filter(bloom_filter, index_list):
                set_of_bags.add(tuple(self.__bags_list[i]))

        return set_of_bags

    def get_random_word_from_random_bag(self, size: int) -> str:
        """
        Extracts one string at random from the bags of strings.
        :param size: the number of bags
        :return: random word
        """
        random_bag = random.randint(0, size - 1)
        random_index = random.randint(0, size - 1)
        return self.__bags_list[random_bag][random_index]


def print_result(query_string: str, result: set) -> None:
    """
    This method prints out the final result, it finds out false positives by checking if the result actually contains
    the term or not.
    :param query_string: This is string that is checked
    :param result: the bags that contain the query string
    :return: None
    """
    if len(result) == 0:
        # if string is not in result
        print("{} not in bag of words".format(query_string))
        logger.info("{} not in bag of words".format(query_string))
    else:
        # if string is in result, print the number of bags that contain the word
        print("{} found in {} bags".format(query_string, len(result)))
        logger.info("{} found in {} bags".format(query_string, len(result)))
        false_positive_count = 0
        for bag in result:
            # check if the word is actually present in the bag and print its relative position in the bag
            # relative position being the string and its neighbours
            if query_string in bag:
                index = bag.index(query_string)
                if index != 0 and index != len(bag) - 1:
                    # if word is in the middle of the bag
                    print("..., {}, {}, {}...".format(bag[index - 1], query_string, bag[index + 1]))
                    logger.info("..., {}, {}, {}...".format(bag[index - 1], query_string, bag[index + 1]))
                elif index == 0:
                    # if word is at the start of the bag
                    print("{}, {}, {}....".format(query_string, bag[index + 1], bag[index + 2]))
                    logger.info("{}, {}, {}....".format(query_string, bag[index + 1], bag[index + 2]))
                elif index == len(bag) - 1:
                    # if word is at the end of the bag
                    print("...{}, {}, {}".format(bag[index - 2], bag[index - 1], query_string))
                    logger.info("...{}, {}, {}".format(bag[index - 2], bag[index - 1], query_string))
            else:
                false_positive_count += 1

        print("False positive count for {} = {}".format(query_string, false_positive_count))
        logging.info("False positive count for {} = {}".format(query_string, false_positive_count))


def main():
    bloom_filter_object = BloomFilterStrings()
    generate_strings_object = GenerateStrings(1000)
    # generating 1000 bags of random strings of size 1000 each
    print("Generating 1000 bags of 1000 strings each and adding each bag to Bloomfilter object")
    logger.info("Generating 1000 bags of 1000 strings each and adding each bag to Bloomfilter object")
    for i in range(1000):
        bloom_filter_object.add_bag(generate_strings_object.get_bag())

    # we will extract a random string from the bags of strings that were added to bloom_filter_object
    # additionally we will shuffle the characters of this string to form a random string and check if
    # both the randomly selected string and the randomly shuffled string are present in the list.
    # we will perform this 10 times.

    for i in range(10):
        print("*" * 100)
        logger.info("*" * 100)
        random_string = bloom_filter_object.get_random_word_from_random_bag(1000)
        print("Randomly chosen string = {}".format(random_string))
        logger.info("Randomly chosen string = {}".format(random_string))
        random_string_result = bloom_filter_object.check_string(random_string)
        print_result(random_string, random_string_result)
        print("*" * 100)
        logger.info("*" * 100)


if __name__ == "__main__":
    logging.basicConfig(filename='bloom_filter.log', filemode='a', level=logging.DEBUG,
                        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)
    main()
