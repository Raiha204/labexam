def find_network(mobile_number):
   

    network_key_digits = {
        "Smart": ["13", "14", "20", "21", "28", "29", "30"],
        "TNT": ["09", "10", "11", "12", "18", "19"],
        "Sun": ["22", "23", "32", "33"],
        "Globe": ["15", "16", "17", "25", "26", "27"],
        "TM": ["03", "04", "05", "06", "07"],
        "Red": ["01", "02", "24"],
        "Dito": ["91", "92", "93", "94", "95", "96", "97", "98"],
    }

 
    if len(mobile_number) != 11 or not mobile_number.isdigit():
        return "Invalid mobile number"

   
    prefix = mobile_number[:4]

    
    if mobile_number[:2] != "09":
        return "Invalid mobile number: Must start with '09'"

    
    key_digits = mobile_number[2:4]

    
    for network, digits in network_key_digits.items():
        if key_digits in digits:
            return network

    return "Network provider not found"



mobile_number = input("Enter a mobile number: ")


network = find_network(mobile_number)


print("The network of the mobile number is", network)
