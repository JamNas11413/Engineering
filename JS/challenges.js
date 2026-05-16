// let and const
// great approach:
    // see if you don't need let then do with const b\c it gives you strictness in your code and thus less bugs will found
    // if you will change value of a var you can define it with let other wise always do with const



// // log out item in an Array
// let array = ["css", "ui", "clean code"];

// function logOutItem(array) {
//     for (let i of array) {
//         console.log(`"${i}"`)
//     }
// }

// logOutItem(array)



// // saving to local  storage
// let array = ["css", "ui", "clean code"]

// localStorage.setItem("val","hello world")
// // localStorage.setItem("array",JSON.stringify(array))

// let getArray = JSON.parse(localStorage.getItem("array"))

// console.log(getArray);  // still logging even when i deleted the code and refresh the page b\c it is saved in local storage




// // accessing object properties
// const logButton = document.getElementById("logButton");

// const maryam = {
//     name: "maryam",
//     age: 16,
//     scores: {
//         math: 90,
//         physics: 95,  // i am physics lover 
//         chemistry: 88
//     }
// };

// logButton.addEventListener("click", function() {
//     console.log(maryam.scores.physics);
// });

    


// // generating sentences
// const fruits = ["apple", "banana", "orange"];
// const desc = `The ${fruits.length} best fruits are:`;

// function genSentence(desc, array) {
//     console.log(`${desc} ${array.join(", ")}.`);
// }

// genSentence(desc, fruits)




// // rendering images using js
// const images = [
//     "https://www.w3schools.com/w3images/lights.jpg",
//     "https://www.w3schools.com/w3images/nature.jpg",
//     "https://www.w3schools.com/w3images/mountains.jpg"
// ]

// function renderImages(array) {
//     for (let i of array) {
//         let img = document.createElement("img");
//         img.src = i;
//         document.body.appendChild(img);
//     }

// }
// renderImages(images)



// const btn = document.createElement("button");
// btn.textContent = "buy! $89.1234567890";
// document.body.appendChild(btn);
// btn.textContent = `buy! $${parseFloat("89.1234567890").toFixed(2)}`;  // toFixed() method formats a number using fixed-point notation, it takes the number of digits to appear after the decimal point as an argument. in this case we want only 2 digits after the decimal point