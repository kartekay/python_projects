import re
import sys


def extract_user_ids(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()

        regex = r'\b[a-zA-Z]\d[a-zA-Z]\d_\d{3}\b'
        matches = re.findall(regex, content)

        last_three_digits = [match[-3:] for match in matches]

        unique_digits = list(dict.fromkeys(last_three_digits))
        for digits in unique_digits:
            print(digits)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python hw1_p1.py <input_file>")
    else:
        extract_user_ids(sys.argv[1])
