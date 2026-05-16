// // document.getElementById("count-el").innerText=5

// // variables
// let count = 5;   // let count be zero {pronounced}  // value assigned from right to left
// // console.log(count);  // log to console //will print it to console both to vs code debug consule{mainly for debug purpuses} and browser real console

// // reassigning te var => declaration/updation
// count = 7;
// count = 8;
// // js use the latest value to a var
// console.log(count);

// // incrementing
// count = count + 1;  // this time the incrementing value is one
// console.log(count);

// let bonusPoint = 50;
// console.log(bonusPoint);
// bonusPoint = bonusPoint + 50;
// console.log(bonusPoint);
// bonusPoint = bonusPoint - 75;  // decrementing by 75
// console.log(bonusPoint);
// bonusPoint = bonusPoint + 45;
// console.log(bonusPoint);

// psudocode
// inittialize the count to 0
// listen for clocks on the button
// incrementing the count with clicks
// showing the inremented value in html
// let count = 0;
// let countEl = document.getElementById("count-el")   // getting the element  // count-el is the argument
// // console.log(countEl) // give th html elemnt of the id
// function increment() {   // func that will trigered when the increment button will clicked
//     console.log("button was clicked! ")
//     count = count + 1;
//     countEl.innerText = count;
//     // console.log("count:",count)
// }
// what happening is that we connected this file with the html and from that we calling to this func via an attr


// // let myAge = 17;
// // console.log(myAge)

// // but
// // console.log(myAge)
// // let myAge = 17;
// // script.js:11 Uncaught ReferenceError: Cannot access 'myAge' before initialization

// // b\c js execute top to bottom let to right so the var is undefined for it at the time it were exe to log statement
// // and error in such case stop the exe of the code after the error


// // arithmatic ops

// let sum = 1234 + 1234567;
// console.log(sum)
// let total = sum;  // value assigned from right to left
// console.log("total:",total)

// console.log("hello world!")


// // my age to dog age
// let myAge = 17;
// console.log(myAge)
// let humanDogRatio = 7;
// console.log(humanDogRatio)
// let myAgeInDog = myAge * humanDogRatio;
// console.log(myAgeInDog)


// function / commands
    // to to avoid repetition

// function fifeToOne(n) {
//     console.log(n);
//     if (n > 1) {
//         fifeToOne(n-1);
//     };
// };
//i can call it via both the browser or here 


// func

// function lapsLog(lap1, lap2, lap3) {
//     console.log(lap1 + lap2 + lap3);
// }
// lapsLog(12,345,56);


// {
//     let lap1 = 12;
//     let lap2 = 345;
//     let lap3 = 56;
// }

// function lapsLog() {
//     console.log(lap1 + lap2 + lap3);
// }
// lapsLog()

// can't be accessed as i call it out of its scope => let vars are block scope


// assignments
let firstName = "Jamal";
let lastName = "Nasar";
let fullName = firstName + " " + lastName;  // concatenation
console.log(fullName)


function greetLog() {
    console.log("Hello, " + fullName + "!");
}


// incre/decrement

let myPoints = 3;

function add3Points() {
    myPoints += 3;
}

function remove1Point() {
    myPoints -= 1;
}

add3Points();
add3Points();
add3Points();
remove1Point();
console.log(myPoints);