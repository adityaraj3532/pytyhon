def convert_temperature(temp, unit):
    if unit == "C":
        # Celsius to Fahrenheit
        return (temp * 9 / 5) + 32
    elif unit == "F":
        # Fahrenheit to Celsius
        return (temp - 32) * 5 / 9


def main():
    # Take input
    print("Enter temprature")
    temp = float(input())
    print("Enter unit  (c=celcius and f = fahrenhiet)")
    unit = input().strip().upper()

    # Call the function21
    result = round(convert_temperature(temp, unit),2)

    # Print the result
    print(result)


if __name__ == "__main__":
    main()