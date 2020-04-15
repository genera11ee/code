function temperature_converter(celsius){
var result = (celsius * 9/5) + 32;
return result;
}

console.log(temperature_converter(21.5));
console.log(temperature_converter(-7));
console.log(temperature_converter(11));
console.log(temperature_converter(0));