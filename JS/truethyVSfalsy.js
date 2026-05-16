// const credit = 0;
// if (credit > 0) {
//     console.log("lets play...")
// }
// else {
//     console.log("creduts gone...")
// }

// if conditio n becomes false and thus else executed 
// AND now 
// const credit = 12;
// if (credit > 0) {
//     console.log("lets play...")
// }
// else {
//     console.log("creduts gone...")
// }

// if will exe b\c condtion will be true meaning   if(true) -> b\c logical ops returns true or false 


// BUT
// const credit = 12;

// if (credit) {
//     console.log("lets play...")
// }
// else {
//     console.log("creduts gone...")
// }

// still if will br return true b\c it value is not false ( 0 ) and having something means true ( 1 )

// BUT BUT
if ("str") {
    console.log("lets play...")
}
else {
    console.log("creduts gone...")
}
// still if will exe as the conditoion has something meaning true ( 1 )

// BUT BUT BUT
if ("") {
    console.log("lets play...")
}
else {
    console.log("creduts gone...")
}
// THIS TIME ELSE WILL exe as it is empty === false ( 0 )

// something === true // SOMETHING IS BETTER THAN NOTHING.



// SO FALSY VALUES OTHER THAN WHOSE WILL ALL TRUE

// flasy vals
// 0
// ""
// null -> is how developer signilize emptyness  i.e str = null
// undefined -> is how js signilize emptyness i.e undefined in console
// NaN -> not a number i.e parseInt("hello") -> NaN -> an error when you are expecting numbers and the value isn't number

// ALL OTHER VALS ARE TRUTHY VALUES

// TRUTHY VALS
// " "
// "0"
// []
// {}
// function(){} 


// we can check whether an expresioon /  value is truthy or falsy

console.log(Boolean(""));  // false