let firstCard = getRandomCard();
let secondCard = getRandomCard();
let sum = firstCard + secondCard;
// console.log("Sum: " + sum);

let messageEl = document.getElementById("message-el");
let sumEl = document.getElementById("sum-el");
let cardEl = document.getElementById("card-el");

let message = ""
let blackjack = false;
let isAlive = true;
let age = prompt("Enter you age...");
    let permission = age <=  22 ? "you can't go inside!" : "Welcome to the club!"
    // console.log(permission)

function startGame() {
    
    if (sum <= 21) {   // js evaluate the exp inside the parenthesis and return a boolean value and if it is true then the block exe other wise ignored
        message = "want a new card!"
        let blackjack = true;
    }
    else if (sum === 21) {
        message = "Wohoo! we've got blackjack!"
        let blackjack = true;
    }

    else {
        message = "we're out!!!"  // re assigning
        let blackjack = true;
        let isAlive = false;
    }
    messageEl.textContent = message
    sumEl.textContent ="Sum: "+ sum;
    cardEl.textContent = "Card: " + firstCard + " & " + secondCard;
}

 
// else if willl be exe if the condition is true while else will always exe if none of thge above is true as no condition





// // = -> assignment operator right to left
// // == -> only check if the value is equal
// // === -> also ckeck for data type with value
// console.log(3 == '3') // true
// console.log(3 === '3') // false




// here js have no idea of what was the result of the conditionals if.e state of the game

// so we can store it in a var where the initial state will be false as there is no blackjac and then we can update it in the conditionals accordingly  i.e blackjack variable
// now we have the record

// console.log("message",message)
// console.log("blackjack", blackjack)
// console.log("isAlive", isAlive)


function newCard() {
    if (isAlive === true && blackjack === false) {
        let card = Math.floor( Math.random()*13 ) + 1;
        sum += card;
        console.log("Drawing a new card from the deck!")
        startGame();
    }
    else {
        console.log("You can't draw a new card!")
    }
}



// avoiding hardcode {fix values avoiding}

function getRandomCard() {
    let num = Math.floor(Math.random() * 13 + 1)
    if (num === 11 || 12 || 13) {
        return 10
    }
    else {
        return num
    }
}

// when you declare a func in js it hosted at top of the file so if i write a func at line 10000000000000 i can access it at line one unlike vars

// generating random numbers

// by Math.random()

// let randomNum = Math.floor(Math.random() * 6 + 1);  // provided by the window / browser  // it gives a random num b\w 0 and 1 (not inclusive of 1 meaning can't be one are not included) 0.000... ---0.999...
// console.log(randomNum) // everytime you refresh the browser will give u a new Num   // but they are psudorandom as there are some principals for it


// it is really hard to generate truly random Numbers
// by multipling it to 6 our num will be inrange of 0.000... --- 5.999...   and it is b\c it has same starting 0 but it goes to 6 so we can multiply it to max value to get max value right ..


// anpther methor = Math.d on math obj
// Math.floor()  take some input and then give some processed output 

// let florr = Math.floor(345678)
// console.log(florr)
// let florr1 = Math.floor(3.45678)
// console.log(florr1)

// floor give us the integral part of the input num i.e fromm 12.99999 it will give 12


// Math.floor(Math.random() * 6)  -> ll it possible values are whole num upto 5 as it removes the decial
// Math.floor(Math.random() * 6) + 1 naytural num upto six