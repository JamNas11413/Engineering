//Functions:
//    block of code that performs a task, can be invoke(call) whenever needed
        // take some input process it and give some output

//Func definetion:
//    syntax:
//        function functionName(peri1.peri2,...) {
//            // do some work
//        }

//funcall:
//    functionName(arg1,arg2,...)

function myFunction() {
    console.log("Hey!!!!");
}

myFunction();
myFunction();

//function decrease redundancy(repetetion of same task)
// if we have some physics formula to code we can define a func for it

//with perameters:
function hello(name) {          // var for the arguments in func definetion are called perimeters
    console.log("welcome there "+name);
}

hello("jamal"); //welcome there jamal    // value passed in func call called arguments

// NaN error=> not a number error

function sum(a,b) {
    console.log(sum=a+b);
}
sum(2,5)

//so these are func which do something
// if func take some inp it can also return some value

function sum(a,b) {
    s=a+b;
    console.log("before return");
    return s;         // the return keyword can only return single value, the value can be a str, an array having multiple values inside but only one var will be return
    console.log("this is an unreachable code, it will not execute b\c  the pointer already returned to from where its called");        // the stements after return will not execute, so not to write after return
}
let value=sum(2,5); // the value of sum will return to from where it is been called
console.log(value);
// the returning means that we can manipulate it latter i.e we can pase this to a func
// a function can return a value and do something



function sum(a,b) {
// the perimeters a and b acts like function's local var => only can manipulate inside the func block/have scope of func block
    console.log(sum=a+b);
    console.log(a)      // 2=> can be accessed
}
sum(2,5)
//console.log(a)      //  not defined       // b\c its not accessible from here as its local to the func

// perameter -> vars inside the definetion / place holder for the args  VS arguments => actual value of the perameters that we pass during call

// ARROW FUNCTION:
//    A WAY OF WRITING FUNC IN A CONPACT WAY
//        syntax:
////            (peram1,perameter2,..) => {                           // the parenthesis shows that will get some input and then after arrow it will manipulated and can also return something        // => -> sign of arrow func
//                    // do something
//                }
//            const funcName=(peram1,perameter2,..) => {              // we can assign it to a var; we can const that will do the specific job
//                // do something
//                }
let hello = () => {         // with out perameter
    console.log("hello");
}
hello();
//ordinary
// MULTIPLICATION FUNC :
function mul(a,b) {
    m = a * b;
    return m;
}
let prod=mul(2,8);
console.log(prod);



//arrow func

//(x,y) => {
//    console.log(x*y);
//}
// will not execute to execute we have to store it in a var
let mull=(x,y) => {       // the mull var becomes function now and store the entire definetion
    console.log(x*y);
//    return x*y;
}
// ***
//console.log(mull);         // will give its definetion like a normal var i.e x=5 and print x will give 5 but in this mull a complete func definetion is stored
//mull(9,2);     // this is call
console.log(mull());        // before the return        // will give undefined as the the func doesn't returning any thing
//console.log(mull(9,2));    // for the return

//{if a func is returning something it means that we can store the func in var and can do something with it(fruitful func->do and return something to manipulate), and if a func isn't returning something it means that we can't store it in a var and if do it will give undefined(void func->just do something)}

mull = 5;       //we can update the func name as when define by let
console.log(mull);

// THE ARROW FUNC SHOULD USE FOR SMALL TASK

// and if we have a singe line of code in a func we can also eliminate the curly brackets, i.e,
let hello1 = () => console.log("hello");    // but it is prefered to use curly brackets
hello1();














// imp


// we can use thye output of a func  by returning it(trough return kw) i.e 
let player1Time = 102;
let player2Time = 107;

function getFastRaceTime() {
    if (player1Time > player2Time) {
        return player1Time
    }
    else if (player1Time < player2Time) {
        return player2Time
    }
    else {
        return player1Time
    }
}


// now i can use/manipulate what ever the func will return
let fastRace = getFastRaceTime()
console.log(fastRace)







prac:
let count = 0;
function checkVowel(str) {
    for(let i of str) {
        if (i === "a" || i=== "e" || i===  "i" || i=== "o" || i=== "u") {       // we can also add capo vowel to check also for
            count++;
        }
    }
    return count;
}
console.log(checkVowel("jamal naser"))
 in arrow
let count = 0;
let checkVowel = (str) => {
        for(let i of str) {
        if (i === "a" || i=== "e" || i===  "i" || i=== "o" || i=== "u") {
            count++;
        }
    }
    return count
}
console.log(checkVowel("jamal naser"))


// FUNCTIONS SPECIFIC FOR AN OBJECT ARE METHODS(we call by the doth notation,I.E, ARR.FOREACH()) AND FUNC are block of code those which performa specific code

// for each();
// forEach loop in array:
//    this is a method of arrays
//    loop specifically for arrays
//    syntax:
//        arr.forEach(callbackfunc)

// CALLBACKFUNC: HERE, IT IS A FUNC TO EXECUTE FOR EACH ELEMENT IN THE ARRAY
// IN JS FUNC CAN PASS LIKE PERAMETER AND CAN ALSO RETURN THE VALUE OF THE FUNCTION PASSED I.E,
// A CALLBACK IS A FUNCTION PASSED AS AN ARGUMENT TO ANOTHER FUNC
//I.E,
function abc(){
    console.log("hello");
}
function myFunc(abc){    //ABC IS CALLBACKFUNC   // i passed the func as perameter and also returned its value  SO IN JS THE FUNC CAN MANIPULATED LIKE ORDINARY VARS
    return abc;
}

let arr = [2,4,5,6,6,7,8];
arr.forEach(function printVal(val) {        ////val==== value at each idx; the for each loop will pass each item in array one after one to the func
    console.log(val);
    }
)

//generally we do in arrow
let arr = [2,4,5,6,6,7,8];
arr.forEach(val => {
    console.log(val);
});

// the for each loop have 3 optional perameters:
let arr = [2,4,5,6,6,7,8];
arr.forEach((val,idx,arr) => {      // 1st=item(value at a specific index), 2nd=index, 3rd=array        // you can name the prameter whatever u want but 1st will be item and so on
//    console.log(val,idx,arr);
});

// Heigher order funx/method:
//    func that either take another func as their perameter or return another func as output i.e, the for each is an heigher order method


let arrNum = [12,45,3,4,5,6,7,89,9,0,765467263746872673467646];     // square of the last one=5.859401318681244e+47=>s.n==>a*10^b or aEb or aE+b so i think ======>5.35*10^47
//arrNum.forEach(item => {
//    console.log(item ** 2);
//});

//. the above can also written as
let arrrNum = item => {
    return item ** 2;
}
arrNum.forEach(arrrNum);        // we passed the var having all the definetion


//ARRAYS METHODS:

// map():->similer to forEach it just return a new array
    // create a new array with the results of some operation. the value its callback returns are used to form new new array
//        syntax:
//            arr.map(callBackFnx(val,idx,arr))
//                or
//                let newArr= arr.map(val => {
//                    return xyz;
//                 })
//console.log(arr.map(arrrNum));  // arrrNum contain all callback and peram
//OR
let num = [23,5,67,8,9,0,9876,54,32]
let newArr=num.map((val => val/2));
console.log(newArr);
// the forEach don't return a value just do something and the map return a new array with value of its callback

//filter():
//    create a new array of element that give true to the condition /filter. i.e,  all even no.
//        syntax:
//            let new array = arr.filter((val)=>{
//                return val % 2 === 0          // all the elements who can return true to the condition will store in the newArr otherwise not stored
//            })

let newArr1 = num.filter(val => val > 10);
console.log(newArr1)


// reduce():
//    performs some operation and reduces the array to a single value. it returns that single value.
//syntax:
//sum:
let singleVal=num.reduce((result,current) => {
    return result+current;
})
console.log(singleVal);
// take two elements from array the 1st one become result and the 2nd one become current, so when add the added value goes into the result and current value become the one at 3rd idx, so add res and cur and resultant value goes into the res and so on

// largest no.
let largeVal=num.reduce((result,current) => {
    return result > current ? result : current;         // apply conditional to check the condition
})
console.log(largeVal);
// take 2 values 1st => result and 2nd becomes current, now the condition ...

//prac?
let mark = [23,91,98,56,10,39,97,80];
let marksAbove90 = mark.filter(val => val > 90);
console.log(marksAbove90);

let n = prompt("enter n:");
let arr = [];
i = 0;
while (i<n){
    arr.push(i++)}
console.log(arr)

let sum = mark.reduce((previous,curr) => {      // multiplying no. from one to n are called factorial of no. n
    return previous*curr;
});
console.log(sum);














