def temperature_converter(celsius):
    result = (celsius * 9/5) + 32
    return result

print(temperature_converter(21.5))
print(temperature_converter(-7))
print(temperature_converter(11))
print(temperature_converter(0))