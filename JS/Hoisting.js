// Hointing:
    // is the behaviour whre vars and functions declaration are moved to the top of their containing scope during the compiltion phase before  code exe.


// what it means is that i can use a func before it definetion as the func declaration moved to top of the scope/block-> in this case is global scope 
let prod=mul(2,8);
console.log(prod);  // 16

function mul(a,b) {
    m = a * b;
    return m;
}


// but

// console.log(myVar)
// let myVar = "this is a varibale"    //  ReferenceError: Cannot access 'myVar' before initialization
// and also the same if it were be const as they bothg behave same when it comes to scope and hoisting


// let and const are hoisted at top but we can't acces it before initializatrion

// if we access a var before his declration i.e
console.log(randomVar)  // ReferenceError: randomVar is not defined
// we get a differ error, so it not that js not know the code exist but wecan't acces it before initialiczation
// and that is b\c the myVar variable exist in temporal dead zone
// means the js know that it is declared and hoisted but it is not availible to access before itis initialized


// SO WE SAY THAT: vars and functions declaration are moved to the top of their containing scope during the compiltion phase before  code exe. BUT NOT THE INITIALIZATION AND INVOKATION
// SO WE ARE JUST HOISTING_> let myVar AND NOT THE INITIALIZATION AND FUNC DEFINETION

// IF WE DO WITH VAR
console.log(myVarVar)
var myVarVar = "this my var var"


// it gives us undefined





// so:
    // while function declaration , const and let are hoisted at top only func declaration can be used before they have been declared lets and const will only be usable after its initialization


    // we can check if a stuff is hoisted or not