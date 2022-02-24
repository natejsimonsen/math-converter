from audioop import add
import math

mappings = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "a": "10",
    "b": "11",
    "c": "12",
    "d": "13",
    "e": "14",
    "f": "15"
}

decimal_to_hex_map = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "10": "a",
    "11": "b",
    "12": "c",
    "13": "d",
    "14": "e",
    "15": "f"
}


def binary_to_decimal(input_str=""):
    if input_str == "":
        input_str = input("Enter 16 digit binary string: ")
    converted_decimal = 0
    for (i, digit) in enumerate(input_str[::-1]):
        converted_decimal += 2 ** i * int(digit)
    return converted_decimal


def hexidecimal_to_decimal(input_str=""):
    if input_str == "":
        input_str = input("Enter hexidecimal string: ")
    converted_decimal = 0
    for (i, digit) in enumerate(input_str[::-1]):
        converted_decimal += 16 ** i * int(mappings[digit.lower()])
    return converted_decimal


def decimal_to_binary(input_str=""):
    if input_str == "":
        input_str = input("Enter decimal: ")
    converted_binary = ""
    quotient = int(input_str)
    while quotient != 0:
        converted_binary += str(quotient % 2)
        quotient = math.floor(quotient / 2)
    return converted_binary[::-1]


def decimal_to_hexidecimal(input_str=""):
    if input_str == "":
        input_str = input("Enter decimal: ")
    converted_hexidecimal = ""
    quotient = int(input_str)
    while quotient != 0:
        converted_hexidecimal += decimal_to_hex_map[str(quotient % 16)].upper()
        quotient = math.floor(quotient / 16)
    return converted_hexidecimal[::-1]


def add_binary_numbers(num1, num2):
    added_str = ""
    carry = 0
    for (i, bit) in enumerate(num1):
        bit1 = int(bit)
        bit2 = int(num2[i])
        if ((bit1 + bit2 + carry) >= 2):
            added_str += str((bit1 + bit2) % 2)
            carry = 1
        else:
            added_str += str(bit1 + bit2 + carry)
            carry = 0
    return added_str[::-1]


# def add_hexidecimal_numbers(num1, num2):
#     added_str = ""
#     carry = 0
#     num1 = num1[::-1]
#     num2 = num2[::-1]
#     for (i, bit) in enumerate(num1):
#         bit1 = int(mappings[bit.lower()])
#         bit2 = int(mappings[num2[i].lower()])
#         if ((bit1 + bit2 + carry) >= 16):
#             added_str += decimal_to_hex_map[str((bit1 + bit2 + carry) % 16)]
#             carry = 1
#         else:
#             added_str += decimal_to_hex_map[str(bit1 + bit2 + carry)]
#             carry = 0
#     return added_str.upper()[::-1]

def add_hexidecimal_numbers(num1, num2):
    return decimal_to_hexidecimal(str(hexidecimal_to_decimal(num1) + hexidecimal_to_decimal(num2)))


def subtract_hexidecimal_numbers(num1, num2):
    return decimal_to_hexidecimal(str(hexidecimal_to_decimal(num1) - hexidecimal_to_decimal(num2)))


def subtract_binary_numbers(num1, num2):
    return decimal_to_binary(str(binary_to_decimal(num1) - binary_to_decimal(num2)))


def multiply_hexidecimal_numbers(num1, num2):
    return decimal_to_hexidecimal(str(hexidecimal_to_decimal(num1) * hexidecimal_to_decimal(num2)))


print(subtract_binary_numbers("10001000", "00000101"))
