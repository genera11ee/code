function greeter(gender){
    if (gender == "male"){
        return "Hello Sir! Welcome back.";
    } else if (gender == "female"){
        return "Hello Madam! Welcome back.";
    } else {
        return "Hello! Welcome back.";
    }
}

// From this line, we are testing
// console.log(greeter("male"));
// console.log(greeter("female"));
// console.log(greeter("non specified"));