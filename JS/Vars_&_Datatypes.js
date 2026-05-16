//Variables:
//    container for value which will store in our memory at certain location, we can manipulate the var's value by its name

fName = "jamal Nasar";
console.log(fName);     // for printing to the console in browser
price=89.99;
x=null;          // nul means no value(absent) or null=empty
y= undefined;   // undefined means we don't know whats in it

console.log(x, y);

//name of vars (identifiers) should be meaningfull or nemonic
//boolean
is_follow=true;
is_subscribed=false;
console.log(is_follow,is_subscribed );

//vars(identifiers) name RULES:
//    vars names are case sensitive; a & A are different
//    only letters, digits, underscore(_) and doller sign($) is allowed. {not even sapce}
//    digits shouldn't be the first char of the name of var
//    reserved word can't be a var's name
//        GEN FORMULA:
//            a-z, A-Z, 1-9(can't be first), _ , $, not name of keyword

//formates of writting vars names:
//    1. fullName->camel case----------> SHOULD USE THIS ONE
//    2. fullname->concatenated text
//    3. full-name->kabab case
//    4. full_name->snake case
//    5. FullName->pascal case

fullName="Jamal Qadar"
console.log(fullName);

//VAR, LET $ CONST:
//    VAR:
//        VARIABLES CAN BE RE-DECLARED & UPDATED. A GLOBAL SCOPE VARIABLE.
//    LET:
//       VARS CAN'T BE RE DECLARED BUT CAN BE UPDATED. A BLOCK({}) SCOPE VAR.
//    CONST:
//        VARIABLES CAN'T BE RE DECLARED OR UPDATED. A BLOCK SCOPE VAR.=<> form defining constant
{
var age=4;
var age=20;
var age =60;
console.log(age);       // it will print the age = 60 as it is last update but this is more confusing and can cause errors so we should avoid using using var
// the age is created 3 time in memory(declared)
}
console.log(age); // still 6o as it global
{
let name="jamal kamal";  // we are declaring the var and assigning it to the value
console.log(name);
let agee = 17;
agee=18;   // the same age is assigned now to another value  // age is updated not re created or re declared AND the old value of age 17 is deleted[we didn't used the let{used for declaring}]
console.log("i am years old:",agee);     // space by convention      // without the comma it give error as it think that there is a n operater missing
}
//console.log("i am years old:",agee);    // not defined as it only in the block
{
const name="jamal nasar"
console.log(name);
//name="jamal kamal"  //Uncaught TypeError: Assignment to constant variable

}
name="jamal kamal"
console.log(name);  // jamal kamal // as it acc to block
const NAME="jamal kamal"
console.log(name);  //jamal kamal //  WE SHOULD WRITE THE CONST WITH CAPS FOR EASINESS

// ok...
let a;
console.log(a); // undefined
// so if we declared a var but didn't assign any value to it it will be undefined acc to js

// but...
//const a;
//console.log(a);   // already declared

//const b;
//console.log(b); //  SyntaxError: Missing initializer in const declaration
// we have to assign a value to a const as we declared it.



//DataTypes:
//    two categories:
//        1. primitive datatypes
//            7 in number
//              1. number
let age1=24;        // as we declared it here we can access to it in the console i.e by enterin its name
console.log(typeof age1);    // number
let price1=26.99;
console.log(typeof age1);    // number
// no.s maybe -ve or +ve

//                2. string
let name1="jamal nasar";
console.log(name1 , typeof name);   //jamal nasar string
let kjh="32456"
console.log(kjh , typeof kjh);  //32456 string

//                 3. boolean
let follw = true;
let subs = false;
console.log(follw, subs, "and",typeof follw, typeof subs);   //true false 'and' 'boolean' 'boolean
console.log(true, false);    // true false

let hasDiscount = true
function processOrder() {
    if (hasDiscount) {
        console.log("Discount applied")
        hasDiscount = false
    }
    else {
        console.log(" NO! Discount applied")
    }
}
processOrder() // Discount applied
processOrder() // NO! Discount applied
// as we updated the var 



//                  4. undefined
// by default all vars are undefined upto the time when they have no value
let g;
console.log(g, typeof g);    // undefined 'undefined'

//                      5. null
let f = null;
console.log(f, typeof f);    // null object => it shows obj but its  primitive datatype
// null means absence of an object

//                      6.BigInt
// we try to store big integers
let bi=BigInt("678776767676");
console.log(bi, typeof bi);  // 678776767676n 'bigint'  => the will always be at the end of big integers(indicates big no.s)

//                       7. Symbol
let sym= Symbol("hello..");
console.log(sym, typeof sym);   // Symbol(hello..) 'symbol'    => symbol which is hello..

//        2. non-primitive:
//                --> objects: collection of values/vars about a specific thing i.e, arrays and functions
//                    obj have key nad value pairs

// creating an obj
//we can bot declared by const or let
const std = {
    fullName : "Maryam Jamal",
    age : 16,
    cgpa : 9.3,
    isPass : true,          // the comma after last element is optional as i write but in console its not shown
};
console.log(std, typeof std) ;   // {fullName: 'Marayam Jamal', age: 16, cgpa: 9.3, isPass: true}  'object'

//if i wanna access to acccess to th name of the std i can
console.log(std["fullName"]) ;   // Maryam Jamal or simply: std["fullName"] in console   // if we didn't put the key in quotes it will think of it like some other var in the file
// accessing the value by key

// OR
console.log(std.age)    // 16

// UPDATING VALUES OF AN OBJ VAR
std["age"] = std["age"] + 1;
console.log(std.age);   // 17

// OR COMPLTELY CAHNGING THE VALUE FO A KEY
std["age"] = 21;
console.log(std)    // {fullName: 'Maryam Jamal', age: 21, cgpa: 9.3, isPass: true}

// ?? OKAY SO.. THINK THAT THE OBJ AN CONST AND STILL WE CAN CHANGE IT VARS, HOW?
// IN ORDER TO CHANGE THE OBJ WE HAVE TO CHANGE THE ENTIRE ELEMENTS OF AN OBJ AS BY ONE ELEMENT THE OBJ ISN'T CHANGE IN ORDER TO CHANGE THE ADDRESS OF THE OBJ IN MEMORY
// SO WE CAN CHANGE IN THE KEYS AND VALUES OF THE OBJ BUT CAN'T CHANGE THE OBJ ITSELF AS ITS CONST



//type conversion in js:
//String() -> to string
//Number() -> to no. & NaN if mot possible
//Boolean() -> to bolean
//parseInt() and parseFloat-> convertsstr to number





























