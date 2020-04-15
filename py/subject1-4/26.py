def temperature_converter(celsius):
    msg_1 = " degrees Celsius are "
    msg_2 = " degrees Farenheit."
    result = float(celsius) * 9/5 + 32
    message =str(celsius) + msg_1 + str(result) + msg_2
    return message

print(temperature_converter(input("Enter a temperature in degrees celsius: ")))
