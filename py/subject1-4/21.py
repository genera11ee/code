
def bytes_bits_converter(_bytes):
    bits = _bytes / 8
    message = str(_bytes) + " bytes are " + str(bits) + " bits."
    return message

print(bytes_bits_converter(1))
print(bytes_bits_converter(8))
