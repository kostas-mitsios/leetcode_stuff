def get_column_number(column_letter):
    result = 0

    for char in column_letter:
        # Calculate the value of the current character relative to 'A'
        value = ord(char) - ord('A') + 1
        result = result * 26 + value

    return result

print(get_column_number("AZ"))