// Async-Await:
    // keywords that make asyncronise programming easier
    // async func always returns a promise 

    // syntax
        // async function myFunc() (...)
        // we can make any func async 
    
async function hello() {
    comsole.log("hello!...");
};

hello();   /// will give a promise

// await pauses the exe of its surrounding async func until th epromise is setted.
// promise pending === await will wait and stop all exe in surrounding

function api() {
    return new Promise((resolve, reject) => {
        setTimeout( ()=> {
            console.log("weather data")
        resolve(200)}, 2000)
    })
}
// await api();  // error -> only valid in async func

async function getweatherdata() {
    await api();  //1st call -> as it will stop all exe after it
    await api();   // 2nd call and so on...
}




// we use both then and catch as well as Async await  depends on the situation


// as we have to put the async await code in a func an dthen call it , we can also avoid the unneccesssary call
// by IIFEs
//  IIFEs:
    // immediately invoked function expression
    // it is called immediatelty as we define it 

// (func () {          // func(definetion) without name enclosed in braces and another brtaces fo its exe    /// the func definetion can be any type normal. arrow, async 
//     //-
// })();  // the last perenthesis shows that it is executed here at here

(async function () {
    console.log("this is effie")
})();  // will exe as we run it without call 

// BUT WE CAN'T USE IT GAIN, FOR THAT WE HAVE TO COPY PASTE IT => MEAN STHAT IT EXE ONLY ONCE
// WE WANNA EXE A FUNC IMMMEDIATELY ONLY ONCE SO WE USE IT


// mdn docs

// prac
function api1() {
    return new Promise((resolve, reject) => {
        console.log("pending");
        resolve(200)
    })
}

async function getapi1() {
    await api1();
    await api1();
    await api1();
    await api1();
    await api1();
    await api1();
    await api1();
    await api1();
}