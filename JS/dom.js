// // DOM => document object model => means how u use js to modify html/websete page
//     // document: means u are interacting with an html document
//     // object: b\c the document keyword in js is of the datatype  obj means that it takes the html doc and convert it to js obj 
//     // model: a representation i.e 
//         // html:   <h2 id="count-el">0</h2>  ===> real thing 
//         // js: let countEl = document.getElementById("count-el")-===> representation / model in js

let feature = document.getElementById("save-feature")  // these should be written on top
let countEl = document.getElementById("count-el")

let count = 0;
function increment() {
    count = count + 1;
    countEl.innerText = count;
    console.log("clicked!")
}


function save() {
    let countStr = count + " - "
    feature.textContent += countStr
    countEl.innerText = 0;
    count = 0
}
// executes from top to bottom when it is called from the html file via the attr onclick in the button element


// // STRINGS:
//     // SEQUENCE OF CHARS REPRESENTING TEXT
//     // A DATATYPE


// // IN WRESTLING OF NUMBERS AND STRINGS, STRINGS ALWAYS WIN AS IT IS  A SUPER SET; AS FLOAT WINS AGAINIST INT {IN PYTHON}

// // CAN BE WRITTEN IN BOTH SINGLE AND DOUBLE COTES

// let username = "Maryam MY LIFE"
// let message = "u have 3 new notifications!"
// console.log(message, username)

// // CONCATENATION: COMBINING STRINGS TOGETHER
// let messageToUser = message + ", " + username + "!"
// console
// .log(messageToUser)

// // TEMPLATE STRINGS:
//     // USE BACKTICKS INSTEAD OF QUOTES
//     // EMBED EXPRESSIONS INSIDE ${}
// let messageToUser2 = `${message}, ${username}!`
// console.log(messageToUser2)  

// // CAN SPAN MULTIPLE LINES
// let multiLine = `hi ${username},
// welcome to the js course!
// lets have fun`
// console.log(multiLine)

// // CHALLENGE:
// let name = "per"
// let greeting = "hi my name is "
// let myGreeting = greeting + name + "!"
// console.log(myGreeting)
// let myGreeting0 = greeting , name + " !"
// let myGreeting2 = `${greeting} ${name}!`
// console.log(myGreeting2)

// // , give spACE if u use it instead of plus


// // NUMBERS:
//     // DATATYPE
//     // INTEGERS AND FLOATS
// let points = 3
// let bonusPoints = 1.5
// console.log(points)
// console.log(bonusPoints)

// // ADDITION
// let totalPoints = points + bonusPoints
// console.log(totalPoints)

// // SUBTRACTION
// let diffPoints = points - bonusPoints
// console.log(diffPoints)

// // MULTIPLICATION
// let multPoints = points * 2
// console.log(multPoints)

// // DIVISION
// let divPoints = points / 2
// console.log(divPoints)

// // INCREMENT/DECREMENT                      
// let myPoints = 3
// myPoints = myPoints + 1
// myPoints += 1
// console.log(myPoints)

// myPoints = myPoints - 1
// myPoints -= 1
// console.log(myPoints)

// // CHALLENGE:
// let score = 0
// score += 5
// score -= 3
// score += 7
// score -= 4
// console.log(score)      

// // TYPE CONVERSION:
//     // CONVERTING ONE DATATYPE TO ANOTHER
// let myStr = "123"
// let myNum = 123
// console.log(myStr)
// console.log(myNum)

// // STRING TO NUMBER
// console.log(Number(myStr))

// // NUMBER TO STRING
// console.log(String(myNum))  

// // TYPE COERCION:
//     // JS AUTOMATICALLY CONVERTS DATATYPES AS NEEDED {to the superior set in givens}
// let str = "123"     
// let num = 123

// console.log(str + num) // "123123"  => str
// console.log(Number(str) + num) // 246  => num


// -
// // NaN: NOT A NUMBER
//     // RESULT OF INVALID MATH OPERATION
//     // TYPE OF NaN IS A NUMBER
// let myStr2 = "hello"
// console.log(myStr2 / 2) // NaN
// console.log(typeof NaN) // number

// CHALLENGE:
// let n = "5"
// let m = 7
// console.log(Number(n) + m) // 12

// // ADVANCED CHALLENGE:
// let a = "10"
// let b = "20"
// console.log(Number(a) + Number(b)) //30

// console.log(4 + 5) //9 {added}
// console.log("2" + "4") // 24  {concates}
// console.log("3" + 1) // 31 {num 1 converted to str "1" and then concates}
// console.log(100 + "100") //100100  {num 100 converted to str 100 and then concates}


// anything in quotes consider as str


// // okay ...

// let wish = "i'd love to see ms Maryam." 
// console.log(wish)  // i'd love to see ms Maryam.

// // but what if i wanna empasize/quoted etc a part of the str

// // let wish1 = "i'd love to see "ms Maryam""
// // console.log(wish1)  //error


// // let wish2 = 'i'd love to see 'ms Maryam."' {in js the inverted comma and eppostropy are same things}
// // console.log(wish2)  // error ahgain in this case

// // sols:
// let wish3 = "i'd love to see \"ms Maryam\"."  // we use the escape char bacslash to ignore the coming char {or to not see the next char as string delimeter(means the next char is not starting or stoping the str)}
// console.log(wish3) // i'd love to see "ms Maryam".


// challenge1
// let welcome = document.getElementById("welcome")
// let name = prompt("Enter your name! ")
// let greeting = "Welcome back,"
// let usrGreeting = greeting + " " + name + "!"

// welcome.innerText = usrGreeting; 

// // not allow to modify the code above and add the emoji //👋

// welcome.innerText += "👋"  // incrementing    /// emojie are str   