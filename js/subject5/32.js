var secret_number = 8;
var secret_color = "green";

function guess(number, color){
    if (number == secret_number && color == secret_color){
        return "You've found both the secret number and the secret color!";
    }
    else if (number == secret_number || color == secret_color){
        return "You found at least one of the secrets!";
    } else {
        var msg_1 = "You didn't find any of the secrets!";
        var msg_2 = "Better luck next time!";
        return msg_1 + " " + msg_2;
    }
}
console.log(guess(8, "green"));
console.log(guess(7, "green"));
console.log(guess(6, "blue"));
console.log("Try again?");