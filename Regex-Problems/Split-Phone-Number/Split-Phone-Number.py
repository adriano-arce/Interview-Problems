import re


if __name__ == "__main__":
    test_phone_nums = [
        "1 877 2638277",
        "91-011-23413627",
        "123 4-5678",
        "",
        "987-654-0123456789",
        "(604) 942-1234",
        "1-2 3456",
        " 123-456-7890",
        "12-413-4567 ",
        "abc-def-1234",
        "123 456 12312312312"
    ]

    # ^           Start from the beginning of the string.
    # (\d{1,3})   The country code is 1-3 digits long.
    # [ |-]       Segments are delimited by a space or a hyphen.
    # (\d{1,3})   The area code is 1-3 digits long.
    # [ |-]       Segments are delimited by a space or a hyphen.
    # (\d{4,10})  The number is 4-10 digits long.
    # $           Finish at the end of the string.
    pattern = r"^(\d{1,3})[ |-](\d{1,3})[ |-](\d{4,10})$"
    regex = re.compile(pattern)
    for (index, phone_num) in enumerate(test_phone_nums):
        print("Test Case #{}: {}".format(index + 1, phone_num))
        match = regex.search(phone_num)
        if match:
            data = match.groups()
            print("  Country Code: {}, Area Code: {}, Number: {}".format(*data))
        else:
            print("  Invalid phone number.")