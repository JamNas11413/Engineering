// Events:
    // the change in the state of an object is known as an event.
    // events are fired to notify code of "intresting changes" that may affect code execution

//    see mdm-> what i need


// i can also search for the event i want ie mouse events and it will show me complete list from wher i can choose;

//EVENT HANDLING IN JS:
//node.event = () => {
//    //handle hereeeeeeeeeeeee
//}

let btn1 = document.querySelector("#btn1")
btn1.onclick = () => {
    console.log('clicked')
}

//let box = document.querySelector("div")
//box.onmouseover=() => {
//    console.log('youre on div!!!!')
//}


// in ordinary case the inline has bigger priority but in case of events the .js file will have priority over inline if im handeling in both places the same thing

// multiple handlers overwrtites the 1st one i.e, if i define handler for the same thing the last one will over writes the before one and last one will exe


// EVENT OBJECT:
    // it is a special obj that has details about the event.
    // all event handler have access to the  event object's properties and methods.
//    generally denoted by e, evt or any other nam as it is a var
// syntax:
//    // node.event = (e) => {
//        // handle here
//        }
let box = document.querySelector("div")
//box.onmouseover=(evt) => {
//    console.log(evt);
//    console.log(evt.type);
//    console.log(evt.target);
//    console.log(evt.clientX, evt.clientY); // position
//    console.log('youre on div!!!!')
//}


//two ways of handeling:
//    1. inline handeling  -> drawback=> code became bulky
//    2. through // node.event = (e) => {    -> drawback=> only one func can define to handle event at once
        //        // handle here
        //        }
//3:
//so:
//event listeners:
    // listyen and weait for event and as it come it execute its job
//    syntax
//        node.addEventListener(event,callback)     // callback=>funx(f)====> handler

// above same work in evt listeners:

box.addEventListener("click", () => {
    console.log("rourrrrrrrrr on div");
})
box.addEventListener("click", () => {
    console.log("rourrrrrrrrr on div ----2");
})
// through event listener we can do multiple jobs at a single event

//accessing event obj
box.addEventListener("click", (evt) => {
    console.log("rourrrrrrrrr on div");
    console.log(evt);   // accessing event obj
    console.log(evt.type);
})


//we can also remove event listener from an element
//syntax:
    // node.removeEventListener(event,callback)     // the  callback refrence should be same to remove

//box.addEventListener("click", () => {
//    console.log("rourrrrrrrrr on div-----1");
//})
//box.addEventListener("click", () => {
//    console.log("rourrrrrrrrr on div ----2");
//})
//box.addEventListener("click", () => {
//    console.log("rourrrrrrrrr on div-----3");
//})
//box.addEventListener("click", () => {
//    console.log("rourrrrrrrrr on div ----4");
//})
// as soon as we clicked all will trigered
// so if i wanna remove the 3rd one
//box.removeEventListener("click", () => {
//    console.log("rourrrrrrrrr on div-----3");
//})  // will not remove (and they are same) b/c they are differnt in memory:
//    // every func created take space in memory as func 1 take differnt space from func 2 even when they do same job

//so to solve/remove:
//we will pass the same cllback func-> same means store in memory at same palce(same refrence) i.e a var can be accesed from every where but it store at a single place
//so to remove we have to store the call back fuc of the in a var
box.addEventListener("click", () => {
    console.log("rourrrrrrrrr on div-----1");
})
box.addEventListener("click", () => {
    console.log("rourrrrrrrrr on div ----2");
})
let callb = () => {
    console.log("rourrrrrrrrr on div-----3");
}
box.addEventListener("click", callb)
box.addEventListener("click", () => {
    console.log("rourrrrrrrrr on div ----4");
})

box.removeEventListener("click",callb)
// removed



