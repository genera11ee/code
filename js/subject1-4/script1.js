var aNumber = 5;
var aString = "3";
var result = aNumber.toString() + aString;
var result2 = aNumber + Number(aString);

console.log(result);

console.log(result2);


function add(a,b){
    var result = "The result is" + (Number(a) + Number(b)) + "!";
    return console.log(result);
}
add(2,3);

