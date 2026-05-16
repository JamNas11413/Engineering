// let num = 1234567890098
// console.log(num) // 1234567890098
// num = 1_234_567_890_098
// console.log(num) // 1234567890098
// console.log( typeof num)  // Number


// // they don't interfare with the num it just make the num easy for us / prog to read


// const maxJsInt = 9_007_199_254_740_991
// the above is the maximum saved integer value of a var
// means its the heighest num that can be accuately represented and used in calcs

// IT DOESN'T MEAN WE CAN'T HAVE BIGGER NUMBERS I.E 
// let BigMaxJsInt = 9_007_199_25let num = 1234567890098
// console.log(num) // 1234567890098
// num = 1_234_567_890_098
// console.log(num) // 1234567890098
// console.log( typeof num)  // Number


// // they don't interfare with the num it just make the num easy for us / prog to read


// const maxJsInt = 9_007_199_254_740_991 * 4
// // console.log(BigMaxJsInt)

// // 36028797018963964

// // but this number isnot  saved we can't be sure about it i.e
// let mul = maxJsInt *2
// console.log(mul)  //we can't be sure aboyut it 

// Numeric literals with absolute values equal to 2^53 or greater are too large to be represented accurately as integers.

// and for numbers bigger than that
// JS GIVES US BigInt(): big integer

// ways of creating BigInt:

// 1) -> n at end 
// let num1 = 9_007_199_254_740_991_324_425_123-987n //end at n
// console.log(typeof num1)  // bigInt

// 2)-> to use the BigInt() constructer
let num2 = BigInt(9_007_199_254_740_991_324_425_123-987)
console.log(typeof num2)  //bigint


// how are bigInt differ from the normal numbers
// we cant do basic math
// console.log(num2 - 1) //TypeError: Cannot mix BigInt and other types, use explicit conversions
console.log(Math.sqrt(num2))  // TypeError: Cannot convert a BigInt value to a number


// so there is alot that we can do with nimbers but cant do with bignints

// use cases of the bigInt:
// 1) cryptography
// 2) working with large numbers like in astronomy
// 3) precise calculations in finance apps
// 3) interacting with databases that use large numbers as identifiers


