import math
import sys
from itertools import chain, combinations
from tabulate import tabulate
import re


def cross_product():
    def transform_cross_product(vector):
        component_vector = re.match(
            "\((\s*?\d*\s*?,)(\s*?\d*\s*?,)(\s*?\d*\s*?)\)", vector)
        if component_vector:
            return [vector.strip() for vector in vector[1:-1].split(',')]
        else:
            vector_and_angle = [vector.strip() for vector in vector.split(',')]
            if len(vector_and_angle) > 3:
                print(
                    "Vecotor must be in either component form (i, j, k) or in M, A1, A2, where M is magnitude, "
                    "A1 is the x-y plane angle, and A2 is the y-z angle")
                sys.exit()
            elif 3 > len(vector_and_angle) > 1:
                x = float(
                    vector_and_angle[0]) * math.cos(float(vector_and_angle[1]) / 180 * math.pi)
                y = float(
                    vector_and_angle[0]) * math.sin(float(vector_and_angle[1]) / 180 * math.pi)
                z = 0
                return [x, y, z]
            else:
                return False

    def do_cross_product(vector1, vector2):
        a = float(vector1[0])
        b = float(vector1[1])
        c = float(vector1[2])
        x = float(vector2[0])
        y = float(vector2[1])
        z = float(vector2[2])

        resultant = [0, 0, 0]
        resultant[0] = b * z - c * y
        resultant[1] = c * x - a * z
        resultant[2] = a * y - b * x
        return resultant

    a = transform_cross_product(input('Enter vector A: '))
    b = transform_cross_product(input('Enter vector B: '))
    if a and b:
        print(do_cross_product(a, b))
    else:
        print("Vectors not recognized")


def definite_integral():
    user_math_function = input("Enter your function (in terms of x): ").replace(
        "^", "**").replace("ln", "log").replace("e", "E")
    variables = input("Enter a, b, and n: ").split(",")

    a = int(variables[0].strip())
    b = int(variables[1].strip())
    n = int(variables[2].strip())

    def math_func(x):
        return (eval(user_math_function))

    def mid_point_rule():
        integrated = 0
        for i in range(n):
            deltax = (b - a) / n
            integrated += deltax * \
                math_func(a + (deltax * i + deltax * (i + 1)) / 2)
        return integrated

    def simpsons_rule():
        integrated = 0
        for i in range(n + 1):
            if i == 0 or i == n:
                coefficient = 1
            elif i % 2 == 0:
                coefficient = 2
            else:
                coefficient = 4

            deltax = (b - a) / n
            integrated += deltax / 3 * coefficient * math_func(a + deltax * i)

        return integrated

    if n % 2 != 0:
        print(mid_point_rule())
    else:
        print(simpsons_rule())


def gcd():
    ints = [int(i) for i in input(
        "Enter two integers separated by a comma: ").split(",")]
    x = ints[0]
    y = ints[1]
    while y != 0:
        r = x % y
        x = y
        y = r
    print(x)


def base_to_decimal():
    nums = [int(i) for i in input(
        "Enter number, base of number: ").split(",")]
    print(int(str(nums[0]), base=nums[1]))


def decimal_to_base():
    nums = [int(i) for i in input(
        "Enter decimal number, base to convert: ").split(",")]
    base = nums[1]
    dec = nums[0]
    if base == 2:
        print(bin(dec)[2::])
    if base == 8:
        print(oct(dec)[2::])
    if base == 16:
        print(hex(dec)[2::])


def powerset():
    s = [s.strip() for s in input("Enter set separated by commas: ").split(",")]
    for combination in chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)):
        print(combination)


def generate_truth_table():

    def transform_expression(expr):
        expr_copy = expr
        if "implies" in expr:
            expr_arr = expr.split('implies')
            expr_copy = f"(not {expr_arr[0]} or {expr_arr[1]})"
        if "=>" in expr:
            expr_arr = expr.split('=>')
            expr_copy = f"(not {expr_arr[0]} or {expr_arr[1]})"
        return expr_copy

    variables = {i.strip(): [] for i in
                 input("Enter your variables separated by a comma: ").split(",")}
    i = 2
    num_rows = int(math.pow(2, len(variables.keys())))

    # generate truth table without expressions
    for key in variables:
        step = num_rows // i
        for j in range(num_rows // step):
            val = j % 2
            variables[key][step * j:step] = [val for q in range(step)]
        i *= 2

    # add expressions to truth table
    user_expressions = [s.strip() for s in input(
        "Enter truth table expressions separated by a comma: ").split(",")]
    expressions = {}
    for expression in user_expressions:
        expressions[expression] = []
        for i in range(num_rows):
            for key in variables:
                globals()[key] = variables[key][i]
            expressions[expression].append(
                int(eval(transform_expression(expression))))

    # add results of truth table
    for key in expressions:
        variables[key] = expressions[key]

    # print tabular data for user to see
    print(tabulate(variables, headers="keys",
          tablefmt='pretty', numalign="center"))


def start():
    user_step = input("What would you like to do?: ")
    exit_status = False

    def list_all_options():
        for key in user_options:
            print('{}: {}'.format(
                ", ".join(key.split(',')), user_options[key][1]))

    def exit_program():
        nonlocal exit_status
        exit_status = True

    user_options = {
        'definite integral,di': (definite_integral, "Evaluate a definite integral (using Simpson's method)"),
        'crossProduct,cp': (cross_product, "Evaluate a cross product of two vectors"),
        'exit,leave,quit,stop': (exit_program, "Exit the Program"),
        'greatest common denominator,gcd': (gcd, "Find the greatest common denominator of two integers"),
        'convert to digit,ctd': (base_to_decimal, "Converts num with base to digital equivalent"),
        'convert to base,ctb': (
            decimal_to_base,
            "Converts decimal to a specified base (only supported options are binary, octal, and hex)"),
        'get subsets,get powerset,gp,gs': (
            powerset, "Generates the powerset for elements specified and separated by a comma"),
        'generate truth table,truth table,gtt,tt': (
            generate_truth_table, "Generates a truth table with specified variables and expressions"),
        'list,options,help': (list_all_options, "Gives a list of all current options"),
    }

    all_options = {key: user_options[keys][0]
                   for keys in user_options for key in keys.split(',')}

    while True:
        if user_step.lower().strip() in all_options:
            all_options[user_step.lower().strip()]()
        else:
            print(
                'Option unrecognized or not supported, to see a list of all possible options, enter "list"')

        if not exit_status:
            user_step = input("What would you like to do?: ")
        else:
            break

    print('Thanks for using Calc.py!')


if __name__ == "__main__":
    start()
