var temperature = "cold";
var weather = "foggy";

if (temperature == "cold" && weather == "raining") {
    console.log("take an umbrella and a warm jacket.");
} else if (temperature == "warm" && weather == "raining") {
    console.log("take an umbrella and a t-shirt.");
} else if (temperature == "cold" && weather == "sunny") {
    console.log("take sunglasses and a warm jacket.");
} else if (temperature == "warm" && weather == "sunny") {
    console.log("take sunglasses and a t-shirt.");
} else {
    console.log("stay home");
}