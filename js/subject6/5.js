// This function takes a boolean parameter
// that says if password was entered correctly
// (true = yes, false = no)
function logIn(passwordIsCorrect) {
    if (passwordIsCorrect != true) {
      console.log("Your password is not correct, you can't log in");
    } else {
        console.log("Welcome back! You are now signed in.");
    }
  } 
logIn(true); //log
logIn(false); //log

function litersToGallons(liters) {
    var result = liters / 3.785;
    var message = liters.toString() + " liters are " + result.toString() + " gallons.";
    console.log(message);
  }
litersToGallons(2); //log

function isGreatherThan10(number) {
    if (number > 10) {
      return "The number is greater than 10.";
    } else if (number == 10){
        return "The number is 10.";
    } else {
      return "The number is smaller than 10.";
    }
  }
console.log(isGreatherThan10(2)); //log
console.log(isGreatherThan10(11)); //log
console.log(isGreatherThan10(10)); //log