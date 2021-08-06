import logging
from atoi import myAtoi


def next_permutation(nums: list) -> list:
    """

    :param nums:
    :return:
    """
    if len(nums) == 0:
        return []
    elif len(nums) == 1:
        return nums

    first_drop = -1
    # first we check if the list is sorted in reverse order or if there is a dip in the values from the right end.
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] > nums[i - 1]:
            first_drop = i - 1
            break

    if first_drop == -1:
        # next greater permutation is not possible as the list sorted in reverse order
        # hence returning sorted order
        nums.sort()
        return nums

    # next we find the first number from the end of the list that is greater than the first dip
    first_greater = 0
    for i in range(len(nums) - 1, first_drop, -1):
        if nums[first_drop] < nums[i]:
            first_greater = i
            break
    # we then exchange the numbers at first drop and first greatest
    nums[first_drop], nums[first_greater] = nums[first_greater], nums[first_drop]

    """
    we need to reverse the list from after the first dip. This is because, the list after the first dip is still 
    in increasing order even with the swap. The swap has ensured that from index 0 to first dip the subarray is 
    the next greatest permutation, now to get the next greatest from there we need to reverse the part after 
    the first dip.
    """
    left = first_drop + 1
    right = len(nums) - 1
    while (left < right):
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums


def process_string(input_string):
    """

    :param input_string:
    :return:
    """
    # removing leading and trailing white spaces.
    input_string = input_string.strip()
    input_string_list = input_string.split(",")
    number_list = []
    for i in input_string_list:
        # using the myatoi method to get the number from string
        num = myAtoi(i)
        if not i.isdigit() and num == 0:
            # if character given by user is a non digit character, atoi returns 0, here we don't add it to the list
            continue
        number_list.append(i)

    return number_list


def main():
    print("This program rearranges numbers into the lexicographically next greater permutation of numbers. "
          "Each number has to be an integer between -2,147,483,647 to 2,147,483,647")
    print("Enter comma separated numbers, any non digit character will be ignored")
    print("Type exit if you wish to quit the program")

    while True:
        input_string = input()
        if input_string.lower() == "exit":
            logger.info("Exiting program")
            return

        logger.info("User provided: {}".format(input_string))
        number_list = process_string(input_string)
        output = next_permutation(number_list)
        logger.info("Response: {}".format(output))
        print(output)


if __name__ == '__main__':
    logging.basicConfig(filename='next_permutation.log', filemode='a', level=logging.DEBUG,
                        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)
    main()
