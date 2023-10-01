# Formuals for converting between decimal and other bases

"""
Decimal to Other Bases
----------------------
Decimal to Binary:
    1. Divide the decimal number by 2
    2. Keep track of the remainder
    3. Repeat until the decimal number is 0
    4. The binary number is the remainders in reverse order

Decimal to Hexadecimal:
    1. Divide the decimal number by 16
    2. Keep track of the remainder
    3. Repeat until the decimal number is 0
    4. The hexadecimal number is the remainders in reverse order
    5. If the remainder is greater than 9, replace it with the corresponding letter
    6. The letter values are as follows:
        10 = A
        11 = B
        12 = C
        13 = D
        14 = E
        15 = F

Decimal to Octal:
    1. Divide the decimal number by 8
    2. Keep track of the remainder
    3. Repeat until the decimal number is 0
    4. The octal number is the remainders in reverse order


Binary to Other Bases
---------------------
Binary to Decimal:
    1. Multiply each digit by 2 to the power of its place value
    2. Add the results together

Binary to Hexadecimal:
    1. Convert the binary number to decimal
        1. Multiply each digit by 2 to the power of its place value
        2. Add the results together
    2. Convert the decimal number to hexadecimal
        1. Divide the decimal number by 16
        2. Keep track of the remainder
        3. Repeat until the decimal number is 0
        4. The hexadecimal number is the remainders in reverse order
        5. If the remainder is greater than 9, replace it with the corresponding letter

Binary to Octal:
    1. Convert the binary number to decimal
        1. Multiply each digit by 2 to the power of its place value
        2. Add the results together
    2. Convert the decimal number to octal
        1. Divide the decimal number by 8
        2. Keep track of the remainder
        3. Repeat until the decimal number is 0
        4. The octal number is the remainders in reverse order


Hexadecimal to Other Bases
---------------------------
Hexadecimal to Decimal:
    1. Multiply each digit by 16 to the power of its place value
    2. Add the results together

Hexadecimal to Binary:
    1. Convert the hexadecimal number to decimal
        1. Multiply each digit by 16 to the power of its place value
        2. Add the results together
    2. Convert the decimal number to binary
        1. Divide the decimal number by 2
        2. Keep track of the remainder
        3. Repeat until the decimal number is 0
        4. The binary number is the remainders in reverse order

Hexadecimal to Octal:
    1. Convert the hexadecimal number to decimal
        1. Multiply each digit by 16 to the power of its place value
        2. Add the results together
    2. Convert the decimal number to octal
        1. Divide the decimal number by 8
        2. Keep track of the remainder
        3. Repeat until the decimal number is 0
        4. The octal number is the remainders in reverse order


Octal to Other Bases
--------------------
Octal to Decimal:
    1. Multiply each digit by 8 to the power of its place value
    2. Add the results together

Octal to Binary:
    1. Convert the octal number to decimal
        1. Multiply each digit by 8 to the power of its place value
        2. Add the results together
    2. Convert the decimal number to binary
        1. Divide the decimal number by 2
        2. Keep track of the remainder
        3. Repeat until the decimal number is 0
        4. The binary number is the remainders in reverse order

Octal to Hexadecimal:
    1. Convert the octal number to decimal
        1. Multiply each digit by 8 to the power of its place value
        2. Add the results together
    2. Convert the decimal number to hexadecimal
        1. Divide the decimal number by 16
        2. Keep track of the remainder
        3. Repeat until the decimal number is 0
        4. The hexadecimal number is the remainders in reverse order
        5. If the remainder is greater than 9, replace it with the corresponding letter
"""


while True:
    # Ask the user which conversion they want to do and give a list whith integers to choose from
    choose_conversion = int(input("Which conversion do you want to do?\n1. Decimal to Binary\n2. Decimal to Hexadecimal\n3. Decimal to Octal\n4. Binary to Decimal\n5. Binary to Hexadecimal\n"
                                  "6. Binary to Octal\n7. Hexadecimal to Decimal\n8. Hexadecimal to Binary\n9. Hexadecimal to Octal"
                                  "\n10. Octal to Decimal\n11. Octal to Binary\n12. Octal to Hexadecimal\n"))


    # If the user chooses 1, do the decimal to binary conversion
    if choose_conversion == 1:
        # Ask the user for the decimal number
        decimal = int(input("Enter the decimal number that is a whole number: "))
        # Decimal to Other Bases coded with print statements for every step
        def decimal_to_binary(decimal):
            # Initialize variables
            binary = ""
            quotient = decimal
            remainder = 0
            # Repeat until the quotient is 0
            while quotient != 0:
                # Divide the decimal number by 2
                quotient = decimal // 2
                # Print the step above
                print(str(decimal) + " / 2 = " + str(quotient))
                # Keep track of the remainder
                remainder = decimal % 2
                # Print the step above
                print(str(decimal) + " % 2 = " + str(remainder))
                # Repeat until the decimal number is 0
                decimal = quotient
                # The binary number is the remainders in reverse order
                binary = str(remainder) + binary
                # Print the step above
                print("Binary number so far: " + binary)
            # Return the binary number
            return binary
        # Explain the steps to reach the conversion number
        print("The steps to convert the decimal number to binary are:")
        print("1. Divide the decimal number by 2")
        print("2. Keep track of the remainder")
        print("3. Repeat until the decimal number is 0")
        print("4. The binary number is the remainders in reverse order")
        # Print the binary number
        print("The number in binary is: " + decimal_to_binary(decimal))

    # If the user chooses 2, do the decimal to hexadecimal conversion
    elif choose_conversion == 2:
        # Ask the user for the decimal number
        decimal = int(input("Enter the decimal number that is a whole number: "))
        # Decimal to Other Bases coded with print statements for every step
        def decimal_to_hexadecimal(decimal):
            # Initialize variables
            hexadecimal = ""
            quotient = decimal
            remainder = 0
            # Repeat until the quotient is 0
            while quotient != 0:
                # Divide the decimal number by 16
                quotient = decimal // 16
                # Print the step above
                print(str(decimal) + " / 16 = " + str(quotient))
                # Keep track of the remainder
                remainder = decimal % 16
                # Print the step above
                print(str(decimal) + " % 16 = " + str(remainder))
                # Repeat until the decimal number is 0
                decimal = quotient
                # The hexadecimal number is the remainders in reverse order
                # If the remainder is greater than 9, replace it with the corresponding letter
                if remainder == 10:
                    hexadecimal = "A" + hexadecimal
                    # Print the step above
                    print("Hexadecimal number so far: " + hexadecimal)
                elif remainder == 11:
                    hexadecimal = "B" + hexadecimal
                    # Print the step above
                    print("Hexadecimal number so far: " + hexadecimal)
                elif remainder == 12:
                    hexadecimal = "C" + hexadecimal
                    # Print the step above
                    print("Hexadecimal number so far: " + hexadecimal)
                elif remainder == 13:
                    hexadecimal = "D" + hexadecimal
                    # Print the step above
                    print("Hexadecimal number so far: " + hexadecimal)
                elif remainder == 14:
                    hexadecimal = "E" + hexadecimal
                    # Print the step above
                    print("Hexadecimal number so far: " + hexadecimal)
                elif remainder == 15:
                    hexadecimal = "F" + hexadecimal
                    # Print the step above
                    print("Hexadecimal number so far: " + hexadecimal)
                else:
                    hexadecimal = str(remainder) + hexadecimal
                    # Print the step above
                    print("Hexadecimal number so far: " + hexadecimal)
            # Return the hexadecimal number
            return hexadecimal
        # Explain the steps to reach the conversion number
        print("The steps to convert the decimal number to hexadecimal are:")
        print("1. Divide the decimal number by 16")
        print("2. Keep track of the remainder")
        print("3. Repeat until the decimal number is 0")
        print("4. The hexadecimal number is the remainders in reverse order")
        print("If the remainder is greater than 9, replace it with the corresponding letter")
        # Print the hexadecimal number
        print("The number in hexadecimal is: " + decimal_to_hexadecimal(decimal))

    # If the user chooses 3, do the decimal to octal conversion
    elif choose_conversion == 3:
        # Ask the user for the decimal number
        decimal = int(input("Enter the decimal number that is a whole number: "))
        # Decimal to Other Bases coded with print statements for every step
        def decimal_to_octal(decimal):
            # Initialize variables
            octal = ""
            quotient = decimal
            remainder = 0
            # Repeat until the quotient is 0
            while quotient != 0:
                # Divide the decimal number by 8
                quotient = decimal // 8
                # Print the step above
                print(str(decimal) + " / 8 = " + str(quotient))
                # Keep track of the remainder
                remainder = decimal % 8
                # Print the step above
                print(str(decimal) + " % 8 = " + str(remainder))
                # Repeat until the decimal number is 0
                decimal = quotient
                # The octal number is the remainders in reverse order
                octal = str(remainder) + octal
                # Print the step above
                print("Octal number so far: " + octal)
            # Return the octal number
            return octal
        # Explain the steps to reach the conversion number
        print("The steps to convert the number to octal are:")
        print("1. Divide the decimal number by 8")
        print("2. Keep track of the remainder")
        print("3. Repeat until the decimal number is 0")
        print("4. The octal number is the remainders in reverse order")
        # Print the octal number
        print(decimal_to_octal(decimal))

    # If the user chooses 4, do the binary to decimal conversion
    elif choose_conversion == 4:
        # Ask the user for the binary number
        binary = input("Enter the binary number that is a whole number: ")
        # Binary to Other Bases coded with print statements for every step
        def binary_to_decimal(binary):
            # Initialize variables
            decimal = 0
            # Multiply each digit by 2 to the power of its place value
            # Add the results together
            for i in range(len(binary)):
                decimal += int(binary[i]) * 2 ** (len(binary) - i - 1)
                # Print the step above
                print(str(binary[i]) + " * 2^" + str(len(binary) - i - 1) + " = " + str(int(binary[i]) * 2 ** (len(binary) - i - 1)))
            # Return the decimal number
            return decimal
        # Explain the steps to reach the conversion number
        print("The steps to convert the binary number to decimal are:")
        print("Multiply each digit by 2 to the power of its place value")
        print("Add the results together")


        # Print the decimal number
        print("The number in decimal is " + str(binary_to_decimal(binary)))

    # If the user chooses 5, do the binary to hexadecimal conversion
    elif choose_conversion == 5:
        # Ask the user for the binary number
        binary = input("Enter the binary number that is a whole number: ")
        # Binary to Other Bases coded with print statements for every step
        def binary_to_hexadecimal(binary):
            # Initialize variables
            decimal = 0
            hexadecimal = ""
            quotient = 0
            remainder = 0
            # Multiply each digit by 2 to the power of its place value
            # Add the results together
            for i in range(len(binary)):
                decimal += int(binary[i]) * 2 ** (len(binary) - i - 1)
                # Print the step above
                print(str(binary[i]) + " * 2^" + str(len(binary) - i - 1) + " = " + str(int(binary[i]) * 2 ** (len(binary) - i - 1)))
            # Repeat until the quotient is 0
            while quotient != 0:
                # Divide the decimal number by 16
                quotient = decimal // 16
                # Print the step above
                print(str(decimal) + " / 16 = " + str(quotient))
                # Keep track of the remainder
                remainder = decimal % 16
                # Print the step above
                print(str(decimal) + " % 16 = " + str(remainder))
                # Repeat until the decimal number is 0
                decimal = quotient
                # The hexadecimal number is the remainders in reverse order
                # If the remainder is greater than 9, replace it with the corresponding letter
                if remainder == 10:
                    hexadecimal = "A" + hexadecimal
                    # Print the step above
                    print("Hexadecimal number so far: " + hexadecimal)
                elif remainder == 11:
                    hexadecimal = "B" + hexadecimal
                    # Print the step above
                    print("Hexadecimal number so far: " + hexadecimal)
                elif remainder == 12:
                    hexadecimal = "C" + hexadecimal
                    # Print the step above
                    print("Hexadecimal number so far: " + hexadecimal)
                elif remainder == 13:
                    hexadecimal = "D" + hexadecimal
                    # Print the step above
                    print("Hexadecimal number so far: " + hexadecimal)
                elif remainder == 14:
                    hexadecimal = "E" + hexadecimal
                    # Print the step above
                    print("Hexadecimal number so far: " + hexadecimal)
                elif remainder == 15:
                    hexadecimal = "F" + hexadecimal
                    # Print the step above
                    print("Hexadecimal number so far: " + hexadecimal)
                else:
                    hexadecimal = str(remainder) + hexadecimal
                    # Print the step above
                    print("Hexadecimal number so far: " + hexadecimal)
            # Return the hexadecimal number
            return hexadecimal
        # Explain the steps to reach the conversion number
        print("The steps to convert binary to hexadecimal are:")
        print("1. Convert the binary number to decimal")
        print("1.1 Multiply each digit by 2 to the power of its place value")
        print("1.2 Add the results together")
        print("2. Convert the decimal number to hexadecimal")
        print("2.1 Divide the decimal number by 16")
        print("2.2 Keep track of the remainder")
        print("2.3 Repeat until the decimal number is 0")
        print("2.4 The hexadecimal number is the remainders in reverse order")
        # Print the hexadecimal number
        print("The number in hexadecimal is: " + binary_to_hexadecimal(binary))

    # If the user chooses 6, do the binary to octal conversion
    elif choose_conversion == 6:
        # Ask the user for the binary number
        binary = input("Enter the binary number that is a whole number: ")
        # Binary to Other Bases coded with print statements for every step
        def binary_to_octal(binary):
            # Initialize variables
            decimal = 0
            octal = ""
            quotient = 0
            remainder = 0
            # Multiply each digit by 2 to the power of its place value
            # Add the results together
            for i in range(len(binary)):
                decimal += int(binary[i]) * 2 ** (len(binary) - i - 1)
                # Print the step above
                print(str(binary[i]) + " * 2^" + str(len(binary) - i - 1) + " = " + str(int(binary[i]) * 2 ** (len(binary) - i - 1)))
            # Repeat until the quotient is 0
            while quotient != 0:
                # Divide the decimal number by 8
                quotient = decimal // 8
                # Print the step above
                print(str(decimal) + " / 8 = " + str(quotient))
                # Keep track of the remainder
                remainder = decimal % 8
                # Print the step above
                print(str(decimal) + " % 8 = " + str(remainder))
                # Repeat until the decimal number is 0
                decimal = quotient
                # The octal number is the remainders in reverse order
                octal = str(remainder) + octal
                # Print the step above
                print("Octal number so far: " + octal)
            # Return the octal number
            return octal
        # Explain the steps to reach the conversion number
        print("To convert binary to octal:")
        print("1. Multiply each digit by 2 to the power of its place value")
        print("2. Add the results together")
        print("3. Repeat until the quotient is 0")
        print("4. Divide the decimal number by 8")
        print("5. Keep track of the remainder")
        print("6. Repeat until the decimal number is 0")
        print("7. The octal number is the remainders in reverse order")
        # Print the octal number
        print("The number in octal is " + binary_to_octal(binary))


    # If the user chooses 7, do the hexadecimal to decimal conversion
    elif choose_conversion == 7:
        # Ask the user for the hexadecimal number
        hexadecimal = input("Enter the hexadecimal number that is a whole number: ")
        # Hexadecimal to Other Bases coded with print statements for every step
        def hexadecimal_to_decimal(hexadecimal):
            # Initialize variables
            decimal = 0
            # Multiply each digit by 16 to the power of its place value
            # Add the results together
            for i in range(len(hexadecimal)):
                if hexadecimal[i] == "A":
                    decimal += 10 * 16 ** (len(hexadecimal) - i - 1)
                    # Print the step above
                    print(str(hexadecimal[i]) + " * 16^" + str(len(hexadecimal) - i - 1) + " = " + str(10 * 16 ** (len(hexadecimal) - i - 1)))
                elif hexadecimal[i] == "B":
                    decimal += 11 * 16 ** (len(hexadecimal) - i - 1)
                    # Print the step above
                    print(str(hexadecimal[i]) + " * 16^" + str(len(hexadecimal) - i - 1) + " = " + str(11 * 16 ** (len(hexadecimal) - i - 1)))
                elif hexadecimal[i] == "C":
                    decimal += 12 * 16 ** (len(hexadecimal) - i - 1)
                    # Print the step above
                    print(str(hexadecimal[i]) + " * 16^" + str(len(hexadecimal) - i - 1) + " = " + str(12 * 16 ** (len(hexadecimal) - i - 1)))
                elif hexadecimal[i] == "D":
                    decimal += 13 * 16 ** (len(hexadecimal) - i - 1)
                    # Print the step above
                    print(str(hexadecimal[i]) + " * 16^" + str(len(hexadecimal) - i - 1) + " = " + str(13 * 16 ** (len(hexadecimal) - i - 1)))
                elif hexadecimal[i] == "E":
                    decimal += 14 * 16 ** (len(hexadecimal) - i - 1)
                    # Print the step above
                    print(str(hexadecimal[i]) + " * 16^" + str(len(hexadecimal) - i - 1) + " = " + str(14 * 16 ** (len(hexadecimal) - i - 1)))
                elif hexadecimal[i] == "F":
                    decimal += 15 * 16 ** (len(hexadecimal) - i - 1)
                    # Print the step above
                    print(str(hexadecimal[i]) + " * 16^" + str(len(hexadecimal) - i - 1) + " = " + str(15 * 16 ** (len(hexadecimal) - i - 1)))
                else:
                    decimal += int(hexadecimal[i]) * 16 ** (len(hexadecimal) - i - 1)
                    # Print the step above
                    print(str(hexadecimal[i]) + " * 16^" + str(len(hexadecimal) - i - 1) + " = " + str(int(hexadecimal[i]) * 16 ** (len(hexadecimal) - i - 1)))
            # Return the decimal number
            return decimal
        # Explain the steps to reach the conversion number
        print("Multiply each digit by 16 to the power of its place value.")
        print("Add the results together.")
        print("The number in decimal is " + str(hexadecimal_to_decimal(hexadecimal)) + ".")


    # If the user chooses 8, do the hexadecimal to binary conversion
    elif choose_conversion == 8:
        # Ask the user for the hexadecimal number
        hexadecimal = input("Enter the hexadecimal number that is a whole number: ")
        # Hexadecimal to Other Bases coded with print statements for every step
        def hexadecimal_to_binary(hexadecimal):
            # Initialize variables
            decimal = 0
            binary = ""
            quotient = 0
            remainder = 0
            # Multiply each digit by 16 to the power of its place value
            # Add the results together
            for i in range(len(hexadecimal)):
                if hexadecimal[i] == "A":
                    decimal += 10 * 16 ** (len(hexadecimal) - i - 1)
                    # Print the step above
                    print(str(hexadecimal[i]) + " * 16^" + str(len(hexadecimal) - i - 1) + " = " + str(10 * 16 ** (len(hexadecimal) - i - 1)))
                elif hexadecimal[i] == "B":
                    decimal += 11 * 16 ** (len(hexadecimal) - i - 1)
                    # Print the step above
                    print(str(hexadecimal[i]) + " * 16^" + str(len(hexadecimal) - i - 1) + " = " + str(11 * 16 ** (len(hexadecimal) - i - 1)))
                elif hexadecimal[i] == "C":
                    decimal += 12 * 16 ** (len(hexadecimal) - i - 1)
                    # Print the step above
                    print(str(hexadecimal[i]) + " * 16^" + str(len(hexadecimal) - i - 1) + " = " + str(12 * 16 ** (len(hexadecimal) - i - 1)))
                elif hexadecimal[i] == "D":
                    decimal += 13 * 16 ** (len(hexadecimal) - i - 1)
                    # Print the step above
                    print(str(hexadecimal[i]) + " * 16^" + str(len(hexadecimal) - i - 1) + " = " + str(13 * 16 ** (len(hexadecimal) - i - 1)))
                elif hexadecimal[i] == "E":
                    decimal += 14 * 16 ** (len(hexadecimal) - i - 1)
                    # Print the step above
                    print(str(hexadecimal[i]) + " * 16^" + str(len(hexadecimal) - i - 1) + " = " + str(14 * 16 ** (len(hexadecimal) - i - 1)))
                elif hexadecimal[i] == "F":
                    decimal += 15 * 16 ** (len(hexadecimal) - i - 1)
                    # Print the step above
                    print(str(hexadecimal[i]) + " * 16^" + str(len(hexadecimal) - i - 1) + " = " + str(15 * 16 ** (len(hexadecimal) - i - 1)))
                else:
                    decimal += int(hexadecimal[i]) * 16 ** (len(hexadecimal) - i - 1)
                    # Print the step above
                    print(str(hexadecimal[i]) + " * 16^" + str(len(hexadecimal) - i - 1) + " = " + str(int(hexadecimal[i]) * 16 ** (len(hexadecimal) - i - 1)))
            # Repeat until the quotient is 0
            while quotient != 0:
                # Divide the decimal number by 2
                quotient = decimal // 2
                # Print the step above
                print(str(decimal) + " / 2 = " + str(quotient))
                # Keep track of the remainder
                remainder = decimal % 2
                # Print the step above
                print(str(decimal) + " % 2 = " + str(remainder))
                # Repeat until the decimal number is 0
                decimal = quotient
                # The binary number is the remainders in reverse order
                binary = str(remainder) + binary
                # Print the step above
                print("Binary number so far: " + binary)
            # Return the binary number
            return binary
        # Explain the steps to reach the conversion number
        print("Steps to reach hexadecimal to binary conversion:")
        print("1. Multiply each digit by 16 to the power of its place value")
        print("2. Add the results together")
        print("3. Repeat until the quotient is 0")
        print("4. Divide the decimal number by 2")
        print("5. Keep track of the remainder")
        print("6. Repeat until the decimal number is 0")
        print("7. The binary number is the remainders in reverse order")
        print("The number in binary is " + str(hexadecimal_to_binary(hexadecimal)) + ".")

    # If the user chooses 9, do the hexadecimal to octal conversion
    elif choose_conversion == 9:
        # Ask the user for the hexadecimal number
        hexadecimal = input("Enter the hexadecimal number that is a whole number: ")
        # Hexadecimal to Other Bases coded with print statements for every step
        def hexadecimal_to_octal(hexadecimal):
            # Initialize variables
            decimal = 0
            octal = ""
            quotient = 0
            remainder = 0
            # Multiply each digit by 16 to the power of its place value
            # Add the results together
            for i in range(len(hexadecimal)):
                if hexadecimal[i] == "A":
                    decimal += 10 * 16 ** (len(hexadecimal) - i - 1)
                    # Print the step above
                    print(str(hexadecimal[i]) + " * 16^" + str(len(hexadecimal) - i - 1) + " = " + str(10 * 16 ** (len(hexadecimal) - i - 1)))
                elif hexadecimal[i] == "B":
                    decimal += 11 * 16 ** (len(hexadecimal) - i - 1)
                    # Print the step above
                    print(str(hexadecimal[i]) + " * 16^" + str(len(hexadecimal) - i - 1) + " = " + str(11 * 16 ** (len(hexadecimal) - i - 1)))
                elif hexadecimal[i] == "C":
                    decimal += 12 * 16 ** (len(hexadecimal) - i - 1)
                    # Print the step above
                    print(str(hexadecimal[i]) + " * 16^" + str(len(hexadecimal) - i - 1) + " = " + str(12 * 16 ** (len(hexadecimal) - i - 1)))
                elif hexadecimal[i] == "D":
                    decimal += 13 * 16 ** (len(hexadecimal) - i - 1)
                    # Print the step above
                    print(str(hexadecimal[i]) + " * 16^" + str(len(hexadecimal) - i - 1) + " = " + str(13 * 16 ** (len(hexadecimal) - i - 1)))
                elif hexadecimal[i] == "E":
                    decimal += 14 * 16 ** (len(hexadecimal) - i - 1)
                    # Print the step above
                    print(str(hexadecimal[i]) + " * 16^" + str(len(hexadecimal) - i - 1) + " = " + str(14 * 16 ** (len(hexadecimal) - i - 1)))
                elif hexadecimal[i] == "F":
                    decimal += 15 * 16 ** (len(hexadecimal) - i - 1)
                    # Print the step above
                    print(str(hexadecimal[i]) + " * 16^" + str(len(hexadecimal) - i - 1) + " = " + str(15 * 16 ** (len(hexadecimal) - i - 1)))
                else:
                    decimal += int(hexadecimal[i]) * 16 ** (len(hexadecimal) - i - 1)
                    # Print the step above
                    print(str(hexadecimal[i]) + " * 16^" + str(len(hexadecimal) - i - 1) + " = " + str(int(hexadecimal[i]) * 16 ** (len(hexadecimal) - i - 1)))
            # Repeat until the quotient is 0
            while quotient != 0:
                # Divide the decimal number by 8
                quotient = decimal // 8
                # Print the step above
                print(str(decimal) + " / 8 = " + str(quotient))
                # Keep track of the remainder
                remainder = decimal % 8
                # Print the step above
                print(str(decimal) + " % 8 = " + str(remainder))
                # Repeat until the decimal number is 0
                decimal = quotient
                # The octal number is the remainders in reverse order
                octal = str(remainder) + octal
                # Print the step above
                print("Octal number so far: " + octal)
            # Return the octal number
            return octal
        # Explain the steps to reach the conversion number
        print("Hexadecimal to Octal Conversion Steps:")
        print("1. Multiply each digit by 16 to the power of its place value")
        print("2. Add the results together")
        print("3. Divide the decimal number by 8")
        print("4. Keep track of the remainder")
        print("5. Repeat until the decimal number is 0")
        print("6. The octal number is the remainders in reverse order")
        # Print the octal number
        print(hexadecimal_to_octal(hexadecimal))

    # If the user chooses 10, do the binary to decimal conversion
    elif choose_conversion == 10:
        # Ask the user for the binary number
        binary = input("Enter the binary number that is a whole number: ")
        # Binary to Other Bases coded with print statements for every step
        def binary_to_decimal(binary):
            # Initialize variables
            decimal = 0
            # Multiply each digit by 2 to the power of its place value
            # Add the results together
            for i in range(len(binary)):
                decimal += int(binary[i]) * 2 ** (len(binary) - i - 1)
                # Print the step above
                print(str(binary[i]) + " * 2^" + str(len(binary) - i - 1) + " = " + str(int(binary[i]) * 2 ** (len(binary) - i - 1)))
            # Return the decimal number
            return decimal
        # Explain the steps to reach the conversion number
        print("To reach the decimal you must multiply each digit by 2 to the power of its place value and add the results together.")
        # Print the decimal number
        print(binary_to_decimal(binary))

    # If the user chooses 11, do the binary to hexadecimal conversion
    elif choose_conversion == 11:
        # Ask the user for the binary number
        binary = input("Enter the binary number that is a whole number: ")
        # Binary to Other Bases coded with print statements for every step
        def binary_to_hexadecimal(binary):
            # Initialize variables
            decimal = 0
            hexadecimal = ""
            quotient = 0
            remainder = 0
            # Multiply each digit by 2 to the power of its place value
            # Add the results together
            for i in range(len(binary)):
                decimal += int(binary[i]) * 2 ** (len(binary) - i - 1)
                # Print the step above
                print(str(binary[i]) + " * 2^" + str(len(binary) - i - 1) + " = " + str(int(binary[i]) * 2 ** (len(binary) - i - 1)))
            # Repeat until the quotient is 0
            while quotient != 0:
                # Divide the decimal number by 16
                quotient = decimal // 16
                # Print the step above
                print(str(decimal) + " / 16 = " + str(quotient))
                # Keep track of the remainder
                remainder = decimal % 16
                # Print the step above
                print(str(decimal) + " % 16 = " + str(remainder))
                # Repeat until the decimal number is 0
                decimal = quotient
                # If the remainder is greater than 9, convert it to a letter
                if remainder == 10:
                    hexadecimal = "A" + hexadecimal
                    # Print the step above
                    print("A" + " * 16^" + str(len(hexadecimal) - i - 1) + " = " + str(10 * 16 ** (len(hexadecimal) - i - 1)))
                elif remainder == 11:
                    hexadecimal = "B" + hexadecimal
                    # Print the step above
                    print("B" + " * 16^" + str(len(hexadecimal) - i - 1) + " = " + str(11 * 16 ** (len(hexadecimal) - i - 1)))
                elif remainder == 12:
                    hexadecimal = "C" + hexadecimal
                    # Print the step above
                    print("C" + " * 16^" + str(len(hexadecimal) - i - 1) + " = " + str(12 * 16 ** (len(hexadecimal) - i - 1)))
                elif remainder == 13:
                    hexadecimal = "D" + hexadecimal
                    # Print the step above
                    print("D" + " * 16^" + str(len(hexadecimal) - i - 1) + " = " + str(13 * 16 ** (len(hexadecimal) - i - 1)))
                elif remainder == 14:
                    hexadecimal = "E" + hexadecimal
                    # Print the step above
                    print("E" + " * 16^" + str(len(hexadecimal) - i - 1) + " = " + str(14 * 16 ** (len(hexadecimal) - i - 1)))
                elif remainder == 15:
                    hexadecimal = "F" + hexadecimal
                    # Print the step above
                    print("F" + " * 16^" + str(len(hexadecimal) - i - 1) + " = " + str(15 * 16 ** (len(hexadecimal) - i - 1)))
                else:
                    hexadecimal = str(remainder) + hexadecimal
                    # Print the step above
                    print(str(remainder) + " * 16^" + str(len(hexadecimal) - i - 1) + " = " + str(remainder * 16 ** (len(hexadecimal) - i - 1)))
            # Return the hexadecimal number
            return hexadecimal
        # Explain the steps to reach the conversion number
        print("To reach the hexadecimal you must multiply each digit by 2 to the power of its place value and add the results together.")
        # Print the hexadecimal number
        print(binary_to_hexadecimal(binary))

    # If the user chooses 12, do the binary to octal conversion
    elif choose_conversion == 12:
        # Ask the user for the binary number
        binary = input("Enter the binary number that is a whole number: ")
        # Binary to Other Bases coded with print statements for every step
        def binary_to_octal(binary):
            # Initialize variables
            decimal = 0
            octal = ""
            quotient = 0
            remainder = 0
            # Multiply each digit by 2 to the power of its place value
            # Add the results together
            for i in range(len(binary)):
                decimal += int(binary[i]) * 2 ** (len(binary) - i - 1)
                # Print the step above
                print(str(binary[i]) + " * 2^" + str(len(binary) - i - 1) + " = " + str(int(binary[i]) * 2 ** (len(binary) - i - 1)))
            # Repeat until the quotient is 0
            while quotient != 0:
                # Divide the decimal number by 8
                quotient = decimal // 8
                # Print the step above
                print(str(decimal) + " / 8 = " + str(quotient))
                # Keep track of the remainder
                remainder = decimal % 8
                # Print the step above
                print(str(decimal) + " % 8 = " + str(remainder))
                # Repeat until the decimal number is 0
                decimal = quotient
                # The octal number is the remainders in reverse order
                octal = str(remainder) + octal
                # Print the step above
                print(str(remainder) + " * 8^" + str(len(octal) - i - 1) + " = " + str(remainder * 8 ** (len(octal) - i - 1)))
            # Return the octal number
            return octal
            # Print the octal number
        print(binary_to_octal(binary))



    else:
        print("Invalid input. Please try again.")



















