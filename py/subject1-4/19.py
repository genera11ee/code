#18.5 degrees Celsius are 65.3 degrees Farenheit.
# fahrenheit = celsius * (9/5) + 32

def temperature_converter(celsius):
    msg_1 = " degrees Celsius are "
    msg_2 = " degrees Farenheit."
    result = round(celsius * (9/5) + 32)
    return str(celsius) + msg_1 + str(result) + msg_2

print(temperature_converter(18.5))