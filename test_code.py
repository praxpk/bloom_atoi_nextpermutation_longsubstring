import unittest
from bloom_filter import BloomFilterStrings, GenerateStrings
from longest_substring import longest_substring
from atoi import myAtoi
from next_permutation import next_permutation, process_string


class TestBloomFilterStrings(unittest.TestCase):
    def setUp(self) -> None:
        self.bloom_filter_strings = BloomFilterStrings()
        self.generate_strings = GenerateStrings(10)

    def test_generate_string_instance(self):
        # testing a private method -> https://stackoverflow.com/questions/15453283/testing-private-methods-in-python-an-exception/50164564
        self.assertIsInstance(self.generate_strings._GenerateStrings__generate_string(), str)

    def test_get_bag_instance(self):
        self.assertIsInstance(self.generate_strings.get_bag(), list)

    def test_get_index_list(self):
        self.assertEqual(self.bloom_filter_strings._BloomFilterStrings__get_index_list("abc"),
                         [525, 1051, 2083, 7329, 179, 3738, 3153])


class TestLongestSubstringWithoutRepeatingCharacter(unittest.TestCase):
    def test_raises_value_error(self):
        with self.assertRaises(ValueError):
            # multiple words raises value error
            longest_substring('abc def')

    def test_empty_string(self):
        self.assertEqual(longest_substring(""), 0)

    def test_normal_string(self):
        self.assertEqual(longest_substring("abc"), 3)


class TestMyAToI(unittest.TestCase):
    def test_atoi_value_over_positive_int_limit(self):
        self.assertEqual(myAtoi("9999999999999"), 2147483647)

    def test_atoi_value_below_negative_int_limit(self):
        self.assertEqual(myAtoi("-9999999999999"), -2147483648)

    def test_atoi_only_non_digit_chars(self):
        self.assertEqual(myAtoi("a"), 0)

    def test_atoi_digits_followed_by_non_digit_chars(self):
        self.assertEqual(myAtoi("123a"), 123)

    def test_atoi_non_digits_chars_followed_by_digits(self):
        self.assertEqual(myAtoi("a123"), 0)

    def test_atoi_negative_followed_by_positive_sign(self):
        self.assertEqual(myAtoi("-+123"), 0)

    def test_atoi_positive_followed_by_negative_sign(self):
        self.assertEqual(myAtoi("+-123"), 0)


class TestNextPermutation(unittest.TestCase):
    def test_empty_string_input_to_process_string(self):
        self.assertEqual(process_string(""), [])

    def test_non_digit_input_to_process_string(self):
        self.assertEqual(process_string("abcde"), [])

    def test_next_permutation_sorted_reverse(self):
        self.assertEqual(next_permutation([3, 2, 1]), [1, 2, 3])

    def test_next_permutation_normal_input(self):
        self.assertEqual(next_permutation([1, 2, 3]), [1, 3, 2])

    def test_next_permutation_empty_input(self):
        self.assertEqual(next_permutation([]), [])

    def test_next_permutation_single_list_input(self):
        self.assertEqual(next_permutation([1]), [1])

if __name__ == '__main__':
    unittest.main()