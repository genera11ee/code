function bytesBitsConverter(bytes){
    var bits = bytes / 8;
    var message = bytes.toString() + " bytes are " + bits.toString() + " bits.";
    return message;
}

console.log(bytesBitsConverter(1));
console.log(bytesBitsConverter(8));