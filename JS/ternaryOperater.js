// ternary operaters:
//     alternative to if/else {sometimes}

// syntax:
    // condition ? expresion1 : expresion2
        // the condition should return either a truthy or falsy value
        // expresion1 will execute only if the condition is truthy
        // expresion2 will execute only if the condition is falsy

// const exerciseTime = 20;
// let message ="";

if (exerciseTime  < 30) {
    message = "try hard";
}
else {
    message = "time over";
}
console.log(message) // it works fine 

// but 
// UPDAYING VALUE OF VARIBLE DEPENDING ON WHETER A CONDDION IS MET  is a greate use case for ternary

exerciseTime < 70 ? message = "time over" : message = "time over";
console.log(message)  // better way



// // the teranry for comples conditionals


const exerciseTime = 40;
let message ="";

if (exerciseTime  < 30) {
    message = "try hard";
}
else if (exerciseTime  < 60) {
    message = "Doing good"
}
else  {
    message = "time over";
}
// console.log(message)

// // in ternary:

// exerciseTime  < 30 ?  message = "try hard" : exerciseTime  < 60 ? message = "Doing good" : message = "time over" ;
// what we doing is: 1st we asked a question and if this is true then expresioon after the condion and ? will exe and if not then we asked a 2nd question and if this is true then we will exe the statement after the ? and if this is also falsy then we will exe thye lass staement 
// console.log(message)

// but it is hard to read so wecan break the line
exerciseTime  < 30 ?  message = "try hard" 
    : exerciseTime  < 60 ? message = "Doing good" 
    : message = "time over" ;


// // we can do more complex stuff with ternary but we shouldn't b/c it become difficult to read undrestand etc

//     // WE SHOULD USE TERNARY FOR SMALL CONDITIONS LIKE TWO CONDIONS AND NOT FOR MORE COMPLEX WE SHOULD USE IF ELSE FOR COMPLEX


// challenge
const playerGuess = 3;
const correctGuess = 5;

let message = "";

// playerGuess === correctGuess ? message = "Correct Guess" : message = "try another one";

// console.log(message)

// more functionality should be add by if else 

if (playerGuess === correctGuess) {
    message = "Correct Guess"
}
else if (playerGuess > correctGuess) {
    message = "too high! and try agian..."
}
else {
    message = "too low! and try again..."
}
console.log(message)



// if you can use const instead of let


// think about the complexity and then deside which to use ternary {for small} or if else {for complex}