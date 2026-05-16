// FUNC EXPRESSION:
    // STORING FUNC IN VARS



//Arrow func

// as  arrow funcis func expression so we have to store it in var

// they are anonymous func


// const getSpendAlerty = (amount) => {
//     return `amount spemnd ${amount}`
// }


// console.log(getSpendAlerty(435673))

// we can also do it like

// const getSpendAlertyst = amount => `amount spemnd ${amount}`    // when  we have one peram we don't needa the barackets but should be put as to be easy in reading
// console.log(getSpendAlerty(435673))




// WHEN TO USE BARACKETS:
    // 1 PERAM: BRACKETS ARE NOT NEEDED    // // const getSpendAlertyst = amount => `amount spemnd ${amount}`
    // 0 OR 2 OR MORE PERAM: BRACKETS ARE NEEDED   // const someFunc = (fdgshj,dtghj) => {
    // EXCEPTION IS ONE WHEN U HAVE 1 PERAM YOU CAN OMIT THE BRACKETS



// WHEN TO USE {} + RETURN KW:
    // RETURN PONE LINE OF CODE WITHOUT RETURN KW AND CURLY BRACES // const getSpendAlertyst = amount => `amount spemnd ${amount}`
    // MORE  COMPLEX LOGIC REQUIEES THE RETURN KW AND CURLY BRACE 


// const someFunc = (fdgshj,dtghj) => {
//     if (fghdjk) {
//         return "gvchjxk"
//     }
// }






// prac

// least amount of code
// const speedAlert = speed => `u are gpig at ${speed}`
// console.log(speedAlert(2345))

// refactoring to complex
// const speedAlert = (speed,maxLimit) => {
//     if (speed > maxLimit) {
//         return "you are speedy"
//     }
// }

// console.log(speedAlert(2345,456))
// console.log(speedAlert(456,2345)) // undefined b\c the func it not executing so nothing returns 

// we can

// const speedAlert = (speed,maxLimit) => {
//     if (speed > maxLimit) {
//         return "you are speedy"
//     }
//     else {
//         return ""
//     }
// }

// console.log(speedAlert(2345,456))
// console.log(speedAlert(456,2345))



// const distanceTraveledInMiles = [234,567,890,1234,567];

// const distanceTraveledInKM = distanceTraveledInMiles.map( distance => Math.round(distance * 1.6))
// console.log(distanceTraveledInKM)








// DEFAULT PERAMETERS

// function prod(a,b) {
//     return a * b;
// }
// console.log(prod(4)) // NaN, because we didn't passed the 2nd param

// sol:

// function prod(a = 1,b = 1) {
//     return a * b;
// }
// console.log(prod(4)) // 4
// if we pass args then we will verrides the default  param




// Rest PARAMETERS
    // catching the resy of the args

// function prod(a = 1,b = 1) {
//     return a * b;
// }
// console.log(prod(4,2,3))  // two param and three args  // the 3rd one is ignored

// when we don't know the number of args we use the rest param
// function prod(ops, ...rest) {  // i can call watever to the rest param i.e ...numbers etc
//     if (prod) {
//         // console.log(...rest)  // 4 2 3 4 5 6 6 7 78 8 8 8 8 8  => val assign to it
//         // console.log(rest)  // (14) [4, 2, 3, 4, 5, 6, 6, 7, 78, 8, 8, 8, 8, 8] => val return by it  IN ARRAY
//         // we can iterate over the array
//         let total = 1;
//         rest.forEach((num,total) => {
//             return total *= num;
//         } )
//     }
// }
// console.log(prod(prod, 4,2,3,4,5,6,6,7,78,8,8,8,8,8))

// the rest param must be at last 1st should be the explicite param in func definetion
// we can have only one rest param




// CALLBACKS
//  js -> funcs are 1st class citizen mena sthey have the sam ecapabilities as other datatypes
        // means func can be assign to vaiables => func expression 
        // func can also be passed as args to other func 
                // setTimeOut
                // map, foreach
                //set interval
                // eventlistener
                //    in all of thse case we used it

    // funcs that are passed to other func called callbacks

function noifyUser(notifyType) {
    return notifyType()
}

const emailNoitify = () => { return "emeil notification"}
const smsNotify = () => {return "sms notification"}

console.log(noifyUser(emailNoitify))
console.log(noifyUser(smsNotify))
// working