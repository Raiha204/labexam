def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
def lcm(a, b):
    return (a * b) // gcd(a, b)
def get_positive_int(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val <= 0:
                print("Please enter a positive integer greater than zero.")
            else:
                return val
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    x = get_positive_int("Enter a value for x: ")
    y = get_positive_int("Enter a value for y: ")
    print(f"The LCM of {x} and {y} is = {lcm(x, y)}")

if __name__ == "__main__":
    main()
