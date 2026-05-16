setTimeout(() => {
    console.log(greenLight)
}, 3000);

// how long will it take to execute this code..................3 sec;  hmmm answer is a litle more complicated

// how js works under the hood: call stacks, event loops etc

// "js is a single-threded, non-blocking language"
// means
    // js runtime envirnment i.e V8 Engine {as js runs in browsers, v8 in chromium etc}

    // the js runtime env give us the heap-> heap handels memory allocation so we don't have to 
    // the js runtime env also give us the callstack ->as js is single threded lang the call stack can only exe one peice if code at a time in its single thread

    // js exe from to[ to bottom, left to right one line at a time 

    // but lets say we have some code in staements like log etc and then we have a settimout func with a delay of 5 s 
    // but we know that the code after it won't wait for it 5s and will exe brfore it 
    // here we met an another idea that js single threaded but non-blocking lang 

    //but if it is single threaded then how does it manage two tasks at one in paralel
    // b\c it get some helping friends from the browser to help it do so
    // i.e webapis, task queue, event loop    => thse are not part of the js they are provided by th browsers tpo give it async power

    // so being single threaded we can still multitask
    // type of things js can do a syncronisly are: 
        // settimeout, set interval, fetching data across network, and promises




// PROCESS:
    // LET SAY WE HAVE AN EXE READY CODE THAT CONSIST OF:
    // COCNSOLE.LOG("1ST")
    // setTimeout(()=>{)
    //     COCNSOLE.LOG("2ND")}, 6000)
    // COCNSOLE.LOG("3RD")
    // OUTPUT:
    // 1St
    // 3RD
    // 2ND 

    // OK SAY 
        // 1STLY THE 1ST STATEMNET WILL MOVE THE CALLSTACK {MUCH LIKE AN ARRAY TO WHICH WE CAN PUSH AND POP VALUES} AND EXE AND REMOVED
        // THEN THE SETTIMEOUT IS -PASSED TO CALLSTACK WHICH PASSES IT TO TO WEBAPI AND THE TIMER FOR IT STARTS
        // LASTYLY THE 3RD STAEMENT MOVE TO CALLSTACK EXE AND REMOVED
        // NOW AFTER 6S OUR SETIMEOUT IS PASSED FROM WEBAPI GTO TASKQUEUE
        // HERE COMES THE EVENT LOOP IT JOB IS TO KEEP AN EYE ON THE CALLSTACK AND THE QUEUE AND WHEN THE CALLSTACK IS EMPPTY IT WILL GRAB A TASK FROM THE TOP OF THE QUEUE TO TO CALLSTACK AND THERE IT EXE AND STACKEMPTIES 
        
        

// webAPIs:
//         provided by the browser
//         not pat of JS
//         have functionality for things like:
//             dom manipulation
//             data request
//             timers(setInterval,setTimeout)
//             and more




// BUT
    // imagine a situation in which there is a func after the settimeout and the func take more time to exe in tjis case the timer will wi=ait for it in queue and the event loop will get it to the callstack after the completion of exe

    // so it means it took more time than the provided i.e 6s
    // hence:
    //      when we give timer to a func that will be the min time taken by the func to exe 



// the event loop take a task from the top of the queue so if ther are many timers in the queue eventloop will take the top one then 2nd top and  so on


        // THIS IS ACTUALLY A GOOD THINMG A S WE WANT OUTPUTS IN NUMBER/ARRANGEMENT
const start = performance.now() // return a high resolution time stamp in ms

setTimeout(() => {
    console.log("Hello World!")
    const end = performance.now()
    console.log(`exe time ${end - start}ms`)
}, 3000);
//exe time 3001.2999999970198ms  -> more than 3 s



// so our initial question 
setTimeout(() => {
    console.log(greenLight)
}, 3000);

// how long will it take to execute this code

// ANS:
    // a min of 3000ms 
    // more depending on whats in the task queue and call stack