////Callbacks:
//
//
////    conclusion:
//            //async await >> promise chain >> callback hell
//
//
//
////{
//
////sync in js
//    // synchronous:
//        // synchrunous means the code runs in a particular sequence of instruction given in the programe.
//        // each instruction wait for the previoud instructionn to complete its execution
//        // one after one , top to bottom left to right
//
//console.log(1);
//console.log(2);
//console.log(3);
//// syncchronus i.e, 1st executed 1st then 2nd statement and then 3rd (all prog we did upto now are synchronous in js)
//
//    // Asynchronous:
//        // Due to snchronous programming sometimes imp instructions get blocked due to some previous instructions, which causes a delay in the UI.
//        // Asynchronous code exe allow us to execute next instruction immediately and doesn't block the flow
//        // if a statemnt take more time to exe the remaining code will run with parrallel and don't wait to complete the exe, and as the time tacker cpde exe completed it will show its output
//
//
//
////// setTimeout(call, time in mS):    // we set time for the func we pass that exe it after the time  // 2Sec === 2000 msec
////function hello() {
////    console.log("Hey! Jamal...");
////}
////setTimeout(hello, 2000);          // callbacks are passed without parenthesis
////
////// we can also:
////setTimeout((hello) => {
////    console.log("Hey! Jamal...");
////}, 4000);
//
//// so it will take its time to exe and in synchronous programming:
////but:
//console.log("before");
//setTimeout((hello) => {
//    console.log("Hey! Jamal...");
//}, 4000);
//console.log("after");   // this tatement will not wait for the above func to exe as it doesn't defends on yhe above funx result, it will exe i paralell with the func and the output of the func will showed after the statement(as it executed after)
///////ouput:
////before
////after
//// Hey! Jamal...    // after 4s
//
//// the above is a synchronous
//
////}
//
////Callbacks:
//    // func passed as an argument to another func
//
////function sum(a,b) {
////    console.log(a+b);
////}
////
////function calcCallback(a,b,sumCallback) {    // in callback we oassed func without parenthesis
////    sum(a,b)
////}
////calcCallback(2,5,sum)
//
//////we can alao:
////function calc(2,4,sum(a,b)=> {           // calback -> complete funx definetion
////    console.log(a+b);
////});
////
//////in Asynchronous
//const hello = () => {
//    console.log("hello!!! ");
//};
//
//setTimeout(hello, 3000);
//
//
//
//
////callback hell:
////     nested callbacks stacked below one another forming a pyramid structure. pyramid of dooms
////     this style of programming become difficult to understand
////function getData(dataId)
////    {
////    console.log("data = ", dataId)
////    }
//// let the the funx take some time to send the dta
//// so we have to set the time
//function getData(dataId)
//    {
//    setTimeout(() => {
//        console.log("data = ", dataId);
//    }, 2000);
//    }
////will do the same work but it will fetch it after 2 sec
//
////but
////if we wanna get the dta for let say 3 entries after 2 sec each
//getData(213);
//getData(2156);
//getData(214);
//////  if geves all it once after 2 sec
////// but we a delay of 2 sec for each id 2nd after 1st and so on..
//// when we want data at a particular delay we use the call back hell
//function getData(data_id, getNext_data)
//    {
//    setTimeout(() => {
//        console.log("data = ", data_id);
//        if (getNext_data) {           // if it exist then call it
//            getNext_data();
//        }
//    }, 2000);
//    }
//
//getData(1223, getData(31234))       // data =  31234  data =  1223
////it doesn't solve the problem: the func call as in argument executed at same time and thus the time cimpleted equall for both
//// and the func call as in argument executed 1st
//
//// so when we have to pass arguments we define an arrow funx
//
//getData(123, () => {
//    getData(31234)
//});
//
////// achieve the delay of time(x) between two fetching
//
////// but if want the fetching of data 4 time then we can:
////console.log('waiting for data 1...');
////getData(123, () => {
////    console.log('waiting for data 2...');
////    getData(31234,() => {
////        console.log('waiting for data 3...');
////        getData(3123, () => {
////        console.log('waiting for data 4...');
////            getData(312)
////        });
////    });
////});
////
////// but the above code is difficult to understand
////
//// THIS IS CALLBACK-HELL
//// WE WILL USE THE CALLBACKS BUT STAY AWAY FROM CALLBACK HELL
//
////// TO SOLVE THE PROBLEM THAT THE CALLBACK HELL HAVE-> WE USE PROMISES
////
////// PROMISES:
////    // PROMISE is for eventuall completion
////
////let promise = new Promise((resolve, reject) => { // resplve & reject == handlers      // resolve == if u run the vcode it means your promise is completed  //  reject == if u run the code it means your promise is completed(fullfiled) but an error will came in exe
////    console.log("i'm a promise...")
////
////})      // i'm a promise...
////
////// we can also print the value of promise (var) which will give the promise details
////
////// a promise can have 3 states:
////    // 1. pending -> waiting pariod
////    // 2. fullfiled -> resolved [work is done / completed]
////    // 3. rejected -> the promise is rejected
////// if we wanna fulfilled/reject our promise
////let promise = new Promise((resolve, reject) => { // resplve & reject == handlers      // resolve == if u run the vcode it means your promise is completed  //  reject == if u run the code it means your promise is completed(fullfiled) but an error will came in exe
////    console.log("i'm a promise...")
//////    resolve("message");      // a func created ny js   we can all it will a value     // if we called it without a value it will show undefined in the arg sec
////    reject("Error occured");        // Callbacks.js:168 Uncaught (in promise) Error occured
////
////})
//
//
function sum(a, b) {
    return a+b;

}
function sub(a, b) {
    return a-b;

}


function calc(sum, sub) {
    return sum;
//    return sub;
}

console.log(calc(2,4))
