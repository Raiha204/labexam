def isPalindrome(valStr):
    valStr = valStr.lower()
    return valStr == valStr[::-1]


def toBinaryIfNumber(value):
    if value.isdigit():
        return bin(int(value))[2:]
    else:
        return None


def main():
    value = input("Enter a value: ").strip()
    input_palindrome = isPalindrome(value)
    print(f"Input is a palindrome: {input_palindrome}")

    binary = toBinaryIfNumber(value)
    if binary:
        print(f"Binary equivalent: {binary}")
        binary_palindrome = isPalindrome(binary)
        print(f"Binary is a palindrome: {binary_palindrome}")
    else:
        print("(No binary conversion since input is text)")


if __name__ == "__main__":
    main()
