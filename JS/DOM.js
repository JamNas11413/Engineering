//DOM(Document Object Model):


//window object:
//    the window obj represents an open window in a brwser. it is browser's obj (not javascript's) & automatically created by browser.
//      it is a global obj with lots of properties & methods.
// all our code lies inside window obj
console.log(window);
console.log("hello");
window.console.log("hello");        //all(many many) of code lies inside it we don't needa write it b\c the browser knows it
window.alert("window......")


//DOM(Document Object Model):
//    when a web page is loaded, the browser creates a document object model(dom) of the page
//all the html can be accessed inside js, all the html elemnts converts into object in js AND the object are called document(availible in window obj)

//in console
//we can :
//window            // will show entire window object
//window.document   // will show the html of the doc        // we can also write the "window.document" as "document" only as window is a global obj
//console.dir(window.document)  //to see the properties of the doc

//console.log() vs console.dir()
// console.log() => will print the stuff on the screen as an element
//console.dir() => print the properties and methods of the special obj i.e document
    // the console.log() treats our dom elemnts special like in a doc we have our dom elements like h1 p etc so we will directly print them with it
    // console.log(document);    => will print our html code , so to print doc we will not use console.log() and will use console.dir() for printing our object
    // the console.dir() is also part of window obj=>window.console.dir(obj)

//  SO WE CAN ACCES OUR HTML INSIDE OUR JS -> INSIDE WINDOW OBJ THER IS AN ANOTHER OBJ NAMED DOCUMENT AND THE DOCUMENT IS BASICALLY A MODEL(REPRESENTATION OF OUR HTML CODE) =====> AND THIS IS CALLED DOM.
// DOM BECAME MODEL OF HTML AND WE NAMED IT DOCUMENT=> LOOK LIKE A TREE LIKE STRUCTURE: AND EVERY BOX IS CALLED NODE(SRC="DOM.HTML"-> IMG OF THE HEIRARCHY)
//when a web page is loaded, the browser creates a document object model(dom) of the page

//HOW TO KNOW THAT IN THE DOC NODE WE HAVE OUR HTML(ACCESS TO HTML IN JS)
console.dir(window.document.body);  // from window we want document which from we want only body tag        // but it will not print the html of body instead it will print the properties and methods of the body, if we wanna html of the body we can:
console.log(document.body); // will show html of the body
console.dir(window.document.body.childNodes);   // list of tag inside the body tag


//we use dom to change in the web dynamically at run time i.e enabeling dark modeby click ona btn
//like
document.body.style.background = "blue";    // will enable blue mode for the body // so i changed style of html inside js
document.body.childNodes[1].innerText = "changed";        // at position 1 in child node is h1 // innerText=> text inside
////so all the changes we want dynamically(dynamic changes=dynamic manipulation) in web page is done by dom through user's input


//DOM Manipulation:
//    to change in dom 1stly we should know where we wanna bring change and for thatw ehave to acces the elements (selecting elemnts)

// {
// IF I INCLUDE MY SCRIPT TAG INSIDE THE HEAD TAG INSTEAD OF AT THE END OF BDY TAG AND NOW:
// when we write the script tag in the head we saying that load script before our body
//console.log(document.body)  // null // means mpt nothing in the body    // it is because when we load our script before body then we can't access to DOM
//thats why we write the script tag at end in body tag
// }

//ways to access to elemnts:
//1. selcting with id:
    // give id(unique name) to each elemnt in html
    // syntax:
        // document.getElementById("myid");         // if the id elemnt doesn't existwegrt null

let head = document.getElementById("heading1");   // return value
console.log(head);  //     <h1 id="heading1">DOM DEMO</h1>

//id in code is shown by "#" => #id ==> h1#heading==>  h1 is tag and heading is id the # is symbol for id

//2. selcting with class:
    // to put multiple html elents in same category we give them a class,
    // syntax:
        // document.getElementsByClassName("my =Class);         // if not exist we get empty collection

let text = document.getElementsByClassName("text"); // also return html collection(similer to array-> have index, lenght)
console.log(text);

//3. selecting with tag:
let ele = document.getElementsByTagName("p")        // also return html collection
console.log(ele);
console.dir(ele);

// LEVEL UP OUR METHOD OF SELECTION:
//QUERY SELECTOR:
    // SYNTAX:
        // document.querySelector("myId"/"myClass"/"tag");  // return 1st element  // if all then returns nodes list

let elem = document.querySelector("p"); // return 1st element matching to what we passed in tags
console.log(elem);
// if we want all
let elemAll = document.querySelectorAll("p");       // if we wanna sll the elements // query selector returns nodes list
console.log(elemAll);
let elem1 = document.querySelector("#heading1");    // # to rep that this is id
console.log(elem1);
let elem2 = document.querySelector(".text");    // . rep the class
console.log(elem2);


// PROPERTIES:-> to access elements and change value

// tagName: returns tag from element nodes(id, class name etc)/to print tag name of an element we use tagName
console.log(elem1.tagName)   // h1

// innerText: returns the text content of the element and all its children
let div = document.querySelector("#div");
console.dir(div);
console.log(div.innerText)

// innerHTML: returns the plain text of HTML content in the element
let div = document.querySelector("#div");
console.dir(divh);
console.log(div.innerHTML)      // html in str form

// the above are for getting value
// for setting value

//in console
//div.innerText="kdfvnj";   -> will replace the list by the str i setted
// div.innerHTML = "<div>inner div</div>";  // it creates a new div at runtime

// for new heading in html h2
let newHeading2 = document.querySelector("h2");
// in console
//newHeading2.innerText="jamkamkam";        // changing text
//newHeading2.innerHTML="<i>new eading</i>"     // change in html


// textContent:
    //return textual content even for hidden elements
    // innerText but it also for hidden elements
// let h2 visibility = hidden in html=><h2 style="visibility: hidden">new heading</h2>
//as it hidden now:
//in console if we innerText
//newHeading2.innerText     // '' -> null
//but
//newHeading2.textContent   //'new heading'













// // {
//
//            // parent nodes:outrmost tag i.e, body tag etc
//            // children nodes: tags inside outer most tag i.e, h1 p div etc; children can be parents for its descendance.
//            // descendance: tags inside the child node i.e img, p inside a div
//            // sibling nodes: nodes at same level in a tree like structure i.e div and script in body
//
//        // the nodes have aproperty: firstChild:
//                                        // means tag just inside/1st tag inside it/leftmost in sibling nodes
//                                        // fisrtChil() property returns 1st child of a parent tag
//console.log(document.body.firstChild);  // text //????
//    // basically in our DOM tree have 3 types of nodes creating:
//             // text nodes -> not as such use but it will 1st node inside a parent
//             //comment nodes
//             // element nodes -> use in development
//let firstNode = document.querySelector("body").children;
//console.log(firstNode)
//
////                                    lastNode:
//                                        //means tag at end inside a parent/last tag inside it/righttmost in sibling nodes(diagrame)
//                                        // lastChild() property returns last child of parent node
//
////nodes+elemnt h/w=> mdm docs
//// }




////PRAC:
//let head2 = document.querySelector("h2");
//console.log(head2.innerText)
//head2.innerText=head2+" from apna college";
//console.log(head2.innerText)
//// acces the elemnt and then what you wanna change , through which prop
//
//let boxes = document.querySelector(".box");
//boxes = boxes + "mdvm ";
//console.log(boxes.innerText)


//attributes:
    // html tags can have attr(extra info)
    // anything we write in opening tag i.e lang="en , src =.js, link="dfghjbhfj etc


//getAttribute(attr)  // to get attr value
let div = document.querySelector("div")
console.log(div);

console.log(div.getAttribute("id")) // box

let par = document.querySelector("p")
console.log(par)

console.log(par.getAttribute("id"))
// similar for any var i.e class etc to get its value


// setAttribute(attr,value):    // to set attr value
par.setAttribute("id","paragraph")
console.log(par.getAttribute("id")) //changed


// to change in style
//node.style
div.style.backgroundColor="blue";
div.style.fontSize="20px";
//in css => background-color but in js=> backgroundColor(the space removed and in camel case), way of writing css in js


//access + change = above
//insert=below;

//insert elments:
    // adding elemnts evvolves:
        // create
        // add
//create
//document.createElement("div")
let btn = document.createElement("button");
console.log(btn)
//but to show on page we have to add it in dom

//ways of addition/insertion:
//node.append(el);
    // adds at the end of node(inside), yhe node means at end of a parent tag as an last chiled
div.append(btn)

//node.prepend(el);
    // add at the startoff node(inside)
div.prepend(btn)

//node.before(el):
    // adds before the node (outside)
div.before(btn)


//node.after(ele):
    // adds after the node (outside)




//deletion:
//node.remove()
div.remove()


//H/W => appendChild(0 and removeChild())=> mdm docs

















