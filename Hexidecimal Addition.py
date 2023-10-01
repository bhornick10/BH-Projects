def hex_addition(hex_num1, hex_num2):
    # Function to perform hexadecimal addition step by step.

    # Remove any spaces from the input.
    hex_num1 = hex_num1.replace(" ", "").upper()
    hex_num2 = hex_num2.replace(" ", "").upper()

    # Initialize variables for carrying and the result.
    carry = 0
    result = ""

    # Ensure both hexadecimal numbers have the same length by adding leading zeros if necessary.
    max_len = max(len(hex_num1), len(hex_num2))
    hex_num1 = hex_num1.zfill(max_len)
    hex_num2 = hex_num2.zfill(max_len)

    # Reverse the strings to start from the rightmost digit (ones place).
    hex_num1 = hex_num1[::-1]
    hex_num2 = hex_num2[::-1]

    # Perform hexadecimal addition column by column.
    for i in range(max_len):
        # Convert hexadecimal digits to decimal values.
        digit1 = int(hex_num1[i], 16)
        digit2 = int(hex_num2[i], 16)

        # Calculate the sum along with the carry from the previous step.
        column_sum = digit1 + digit2 + carry

        # Determine the carry for the next step.
        carry = column_sum // 16

        # Get the remainder to form the current digit of the result.
        current_digit = column_sum % 16

        # Convert the decimal digit to hexadecimal and add it to the result.
        result += format(current_digit, 'X')

        # Print the step.
        print(f"Step {i + 1}: {hex_num1[i]} + {hex_num2[i]} (with carry {carry}) = {result[::-1]}")

    # If there's a carry left after all columns, add it to the result.
    if carry > 0:
        result += format(carry, 'X')
        print(f"Final Carry: {carry}")

    # Reverse the result to get the correct order.
    result = result[::-1]

    return result

# Input two hexadecimal numbers from the user.
hex_num1 = input("Enter the first hexadecimal number: ")
hex_num2 = input("Enter the second hexadecimal number: ")

# Perform hexadecimal addition and print the final result.
sum_hex = hex_addition(hex_num1, hex_num2)
print(f"\nResult: {hex_num1} + {hex_num2} = {sum_hex}")
