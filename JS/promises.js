// PROMISES:
   // PROMISE is for eventuall completion

// let promise = new Promise((resolve, reject) => {             // resolve & reject == handlers      // resolve == if u run the code it means your promise is completed  //  reject == if u run the code it means your promise is completed(fullfiled) but an error will came in exe
//    console.log("i'm a promise...")

// })      // i'm a promise...

// we can also print the value of promise (var) which will give the promise details


// a promise can have 3 states:
   // 1. pending -> waiting pariod i.e .fetch()  
        // from here it can take transition to one of the following
   // 2. fullfiled/resolved -> resolved [work is done / completed as promised]
   // 3. rejected -> the promise is not completed as promised   IN CASE OF FETCH A REJECTED PROMISE WILL MEAN A NETWORK ERROR OR SOMETHING SIMILER

// if we wanna fulfilled/reject our promise
let promise = new Promise((resolve, reject) => {          
    console.log("i'm a promise...")
    resolve("message");      // a func created by js   we can call it with a value     // if we called it without a value it will show undefined in the arg sec
    reject("Error occured");        // Callbacks.js:168 Uncaught (in promise) Error occured

})


function sum(a, b) {
    return a+b;

}
function sub(a, b) {
    return a-b;

}


function calc(a,b,sum, sub) {
    sum(a,b);
    sub(a,b);
}

calc(2,4,sum,sub);


// use of promises:
// a promise can be resolve or reject 
// so if it is one of them then what we wanna do 

// we do that with the .then() and .catch()
// .then() => for resolve
// .catch() =>  for an error in exe / rejection


// promise.then((res)=>(...))      // will exe as the promisse become fulllfilled
// promise.catch((err)=> (...))    /// will exe as the promise reject

// const getPromise=() => {
//     return new Promise((resizeBy,rej) => {
//         console.log("i am a promise");
//         resolve("done succesfully");   // we wanna resolve it
        
//     });
// };

// let promise1 = getPromise();
// promise1.then(()=>{
//     console.log("it is  done babby...");
// })


const getPromise=() => {
    return new Promise((resizeBy,rej) => {
        console.log("ima promise");
           // we wanna reject it        // promise rejection or fullfilling done by users
        reject("an error occured")
    });
};

let promise1 = getPromise();            // it will never exe as the promise is rejected 
promise1.then((result)=>{
    console.log("it is  done babby...");
})

// to catch the error
promise1.catch((error)=>{
    console.log("an error occured babby..,", error)   // error is the msg that we passed at time of rejection i.e at line 220
})


// PROMISE CHAIN
function asyncFunc() {
    return new Promise((resolve, reject) => {
        setTimeout(()=>{
            console.log("data...");
            resolve("success");
        }, 4000)
    });
}

let p1 = asyncFun();
p1.then((res)=>{
    console.log(res)
})



