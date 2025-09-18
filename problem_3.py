def get_network(number):
    # Dictionary of known prefixes and networks
    networks = {
        '906': 'TM',
        '917': 'Globe',
        '922': 'Smart',
        '939': 'Sun'
    }


    cleaned = number.replace(" ", "").replace("-", "")


    if len(cleaned) != 11 or not cleaned.startswith("09") or not cleaned.isdigit():
        return "Invalid mobile number format."

    prefix = cleaned[2:5]
    return networks.get(prefix, "Unknown network")


def main():
    number = input("Enter a mobile number: ")
    network = get_network(number)
    print(f"The network of the mobile number is {network}")


if __name__ == "__main__":
    main()
