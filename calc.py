import math
import re
import sys

userStep = input("What would you like to do?: ")

exit = False


def crossProduct():
    def transformCrossProduct(vector):
        componentVector = re.match(
            "\((\s*?\d*\s*?,)(\s*?\d*\s*?,)(\s*?\d*\s*?)\)", vector)
        if componentVector:
            return [vector.strip() for vector in vector[1:-1].split(',')]
        else:
            vectorAndAngle = [vector.strip() for vector in vector.split(',')]
            if len(vectorAndAngle) > 3:
                print(
                    "Vecotor must be in either component form (i, j, k) or in M, A1, A2, where M is magnitude, "
                    "A1 is the x-y plane angle, and A2 is the y-z angle")
                sys.exit()
            elif len(vectorAndAngle) < 3 and len(vectorAndAngle) > 1:
                x = float(
                    vectorAndAngle[0]) * math.cos(float(vectorAndAngle[1]) / 180 * math.pi)
                y = float(
                    vectorAndAngle[0]) * math.sin(float(vectorAndAngle[1]) / 180 * math.pi)
                z = 0
                return [x, y, z]
            else:
                return False

    def doCrossProduct(vector1, vector2):
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

    a = transformCrossProduct(input('Enter vector A: '))
    b = transformCrossProduct(input('Enter vector B: '))
    if a and b:
        print(doCrossProduct(a, b))
    else:
        print("Vectors not recognized")


def definiteIntegral():
    userMathFunction = input("Enter your function (in terms of x): ").replace(
        "^", "**").replace("ln", "log").replace("e", "E")
    variables = input("Enter a, b, and n: ").split(",")

    a = int(variables[0].strip())
    b = int(variables[1].strip())
    n = int(variables[2].strip())

    def mathFunc(x):
        return (eval(userMathFunction))

    def midPointRule():
        integrated = 0
        for i in range(n):
            deltax = (b - a) / n
            integrated += deltax * \
                          mathFunc(a + (deltax * i + deltax * (i + 1)) / 2)
        return integrated

    def simpsonsRule():
        integrated = 0
        for i in range(n + 1):
            if i == 0 or i == n:
                coefficient = 1
            elif i % 2 == 0:
                coefficient = 2
            else:
                coefficient = 4

            deltax = (b - a) / n
            integrated += deltax / 3 * coefficient * mathFunc(a + deltax * i)

        return integrated

    if n % 2 != 0:
        print(midPointRule())
    else:
        print(simpsonsRule())


def listAllOptions():
    for key in userOptions:
        print('{}: {}'.format(", ".join(key.split(',')), userOptions[key][1]))


def exitProgram():
    global exit
    exit = True


def bin_to_dec():
    try:
        bin_str = input("Enter binary number: ")
        bin_number = int(bin_str, 2)
        print("Decimal for {} is {}".format(bin_str, bin_number))
    except TypeError or ValueError:
        print("Enter valid binary number")


def dec_to_bin():
    try:
        dec_str = input("Enter decimal number: ")
        dec_number = bin(int(dec_str))
        print("Binary for {} is {}".format(dec_str, dec_number))
    except:
        print("Enter valid decimal number")

def bin_to_hex():



userOptions = {
    'definite integral,di': (definiteIntegral, "Evaluate a definite integral (using Simpson's method)"),
    'crossProduct,cp': (crossProduct, "Evaluate a cross product of two vectors"),
    'exit,leave,quit,stop': (exitProgram, "Exit the Program"),
    'bin to decimal,btd': (bin_to_dec, "Convert binary number to decimal"),
    'decimal to bin,dtb': (dec_to_bin, "Convert decimal number to binary"),
    'list': (listAllOptions, "Gives a list of all current options"),
}

allOptions = {key: userOptions[keys][0]
              for keys in userOptions for key in keys.split(',')}

while True:
    if userStep.lower().strip() in allOptions:
        allOptions[userStep.lower().strip()]()
    else:
        print('Option unrecognized or not supported, to see a list of all possible options, enter "list"')

    if not exit:
        userStep = input("What would you like to do?: ")
    else:
        break

print('Thanks for using Calc.py!')
