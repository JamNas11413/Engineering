 
// // setTimeout(call, time in mS):    // we set time for the func we pass that exe it after the time  // 2Sec === 2000 msec
// function hello() {
//    console.log("Hey! Jamal...");
// }
// setTimeout(hello, 2000);          // callbacks are passed without parenthesis and if we passed with parentghesis it will be auto matically invked and will not wait for settimeout delay

// // we can also:
// setTimeout((hello) => {
//    console.log("Hey! Jamal...");
// }, 4000);

// // so it will take its time to exe and in synchronous programming:
// //but:
// console.log("before");
// setTimeout((hello) => {
//    console.log("Hey! Jamal...");
// }, 4000);
// console.log("after");   // this tatement will not wait for the above func to exe as it doesn't defends on yhe above funx result, it will exe i paralell with the func and the output of the func will showed after the statement(as it executed after)
// ///ouput:
// //before
// //after
// // Hey! Jamal...    // after 4s

// // the above is a synchronous



// const redLight = "redLight";
// const greenLight = "greenLight";

// console.log(redLight)

// setTimeout(() => {
//     console.log(greenLight)
// }, 3000);   // anonymous func invoke auto 



// SO FAR WE HAVE BEEN GIVING SETTIMEOUT THE CODE THAT WE WNNA EXECUTR {NOT OPTIONAL} AND THE DELAY WIHCH IS OPTIONAL AND BYDEFAULT IT WILL BE 0
// but we can pass it more info, ANYTHING MORE WE ADD TOT HIS LIST WILL BE PASSED TO THIS FUNC AS ARGUMENT

// function displayLight(light) {
//    console.log(light)
// }

// setTimeout(displayLight, 2000, "green")  // argument should be in quotes to represent str value

// more than one peram

function displayLight(light1, light2) {
   console.log(light1 + light2);
}
const timeoutFunc = setTimeout(displayLight, 2000, "green", "red")  // anything we add after the two vals wioll be argument irespective of its no.



// we can also interup the settimeout method and stop it before it executes

const btn = document.getElementById("btn")

btn.addEventListener("click", function(){
   clearTimeout(timeoutFunc)
   console.log("cancelled...")
})