#upgraded own converter
def bytes_bits_converter(_bytes):
    if _bytes < 0:
        print("That is a negative value")
    msg_1 = " bytes are "
    msg_2 = " bits."
    result = float(_bytes) / 8
    return str(_bytes) + msg_1 + str(result) + msg_2
    

print(bytes_bits_converter(6.7))
print(bytes_bits_converter(-9))