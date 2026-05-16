////Loops:
////    used to execute a piece of code again and again
//
//// for loop:
////syntax:
////    for (3 statements: initialization statements; stoping condition; updation statement ) {     // if the stoping condition give us true the loop will execute
////        code to exe;
////    }
//
//for (count=1; count<=100; count++) {
//    console.log(count);
//}
//// the for loop is starting with in the initialization then check the condition if its true then
//// it executes the block of code and then return to the updation and then it chacks the condition
//// again and so on until the condition becomes false
//
////// to find sum of first n no.
////let sum = 0;
////for (let n = 1; n <= 10; n++) {
////    console.log(n,"+",sum ,"= ", sum+n);
////    sum = sum+n;
//////    console.log(sum);
////}
////console.log("loop is ended! ");
////console.log("sum:",sum);
//////console.log(n);   // n is not defined-> we can't access out side of the block as we define it via let if we did it via var we can
//
//////INFINITE LOOP:
////let sum = 0;
////for (let n = 1; true; n++) {    ///THE N IA BLOCK SCOPE MEANING ONLY INSIDD THE LOOP
////    console.log(n,"+",sum ,"= ", sum+n);
////    sum = sum+n;
////}
////MAY BE BROWSER STOP
//
//
//////WE CAN DO ALL STUFF TROUGH FOR LOOP THAT WE CAN DO FROM WHILE, THEY ARE JUST DIFFERENT WAY OF WRITING LOOPS
////
//////While loop:
//////    syntax:
//////        while (condition) {               // will running until the condition is true
////            // do some work
//////        }
////
////let i = 1;       // initialization
////while (i <= 10) {
////    console.log("i =", i);
////    i++;        // updation
////}
//
//////Do-While Loop:
//////    syntax:
//////          do {
////            // some work
//////          } while (condition);
////        // will execute itleast once even if the condition is false as it checks condition at end of an execution
////
////let i = 20;     // initialization
////do {
////    console.log("Hey..");
////    i++;        // updation
////} while (i<5);     // it execute once even when the condition is false and then it stops itself as the condition becomes false at the end of the execution
////
////
////// we put semicolon(;) at end of a statement not a block
////
////let y = 1;
////do {
////    console.log(y);
////    y++;
////} while (y < 10);
//
////For-Of loop and for-in loop =>>helps us to iterate on some special data types
//
////For-Of loop:  //helps us to iterate on str and arrays
////    syntax:
////        for (let val of strVar) {
////            do some work
////        }
//
////let str="Maryam Jamal"
////for (let i of str ) {       // don't needa care about initialization , updation or ending condition these are done by the for of loop itself
////       console.log("i=",i);
////}
//// the "i" is known as iterator and wil get chars of the str above
//
////// doing something with it
////let str="Maryam Jamal"
////let sizeStr=0;
////for (let i of str ) {
////    console.log("i=",i);
////    sizeStr++;      // each time the loop runs will increment the size by 1
////}
////console.log(sizeStr)
//
//////For-In loop:
//////    helps us to iterate on objects(arrays and func{...})
//////        syntax:
//////                for (let key in objVar) {
//////                    // do some work
//////                }
////
////let std = {
////    name: "jamal",
////    age: 17,
////    add: "Swat"
////}
////////for (let i in std) {
////////    console.log(i) // name age add => iterator returns keys
////////}
//////for (let key in std) {
//////    console.log(key) // name age add => keys
//////}
////
////for (let key in std) {
////    console.log("key =",key,"value =",std[key])  // the key isn't in double quotes as it a var not a an actual key   //key = name value = jamal  key = age value = 17  key = add value = Swat
////
////}
//
//
////// print all evel no upto 20
////for (let i = 1; i <= 20; i++ ) {
////    if (i % 2 == 0) {       // as there is a condition(on the base of which we will decide what to do) so we will use conditionals stetements
////        console.log(i)
////    }
////}
//
//
////prac 2. create agame where u start with any random game no. ask the user keep guessing until the user enter correct no.
//let gameNum = 25;
//let prom = prompt("enter no. ");
//do {
//    prom=prompt("enter again");       // the prompt return a str as input in python so we use double equal == / !=
//} while (gameNum != prom);
//console.log("You did it...")



//Strings:
//    sequence of chars used to represent text

//creating
let strVar = "pharmacy app";        // 'pharmacy app'
let strVar1 = 'single quotes';       // 'single quotes'


        // strings have some inbuilt methods(functions) and some properties(variables){i.e length}
console.log(strVar.length);    // 12    => total no. of chars in a str including spaces

        // indices
console.log(strVar[0])   // p

//TEMPLATE LITERALS IN JS:  => special type of str     // we create it using backlets
//    A WAY TO HAVE EMBEDDED EXPRESSIONS IN A STR
let sentence = `this is a special type of str/ template literal`
console.log(sentence, typeof sentence)      // this is a special type of str/ template literal         string
// also can be break into multiple lines i.e
let breakStr = `i am
jamal
who is a programmmer`

// str interpolation:
//    to create str by doing substitution of placeholders
//i.e
let obj = {
    item: "pen",
    price: '10Rs'
}
console.log(`the price of ${obj.item} is ${obj.price}.`)    // the price of pen is 10Rs.    => all becomes one str
// anything inside the braces in str interpolation will evaluated first and then added and becomes part of the str, i.e,
console.log(`exp: ${1+3-5}`)  // exp: -1


////// escape chars:   ----[print()===console.log()]
////#ESCAPE SEQUENCE CHARS
////    # TAB:"\t"  to print tab b/w strings
////print("Hello \tWorld")
////    #NEW LINE: "\n" to end the line
////print("hello \nworld")
////    # "\r" Carriage return   ->move curser to biggining of line and over writes
////print("hello \rworld")     #world
////        # "hello" printed
////        # "\r" moves curser back to start
////        # "world" over writes "hello"
////    # "\b" bakspace   ->remove one char before it
////print("hello \bworld")    #helloworld
////    #"\f" Form feed    ->used to move to next page in printers, in consoles, it may just show as whitespace or an empty box
////print("hello \f world")     #hello  world
////    # "\a" bell/alert sound{beep}  ->doesn't print anything by default, also don't beep b/c modern sys mute it auto
////print("\a")
////    # "\\" backslash  ->1st one as a guard for 2nd and to prind "\"
////print("hello \\word")    #hello \world
////    #"\'" single quote
////print('it\'s mine')   # tell python to ignore the just upcomming char ie.  # '
////    # "\"" double quote
////print("\"quote\"")
////    # "\uxxx"  unicode chars
////print("\u2764")   #heart emoje
////     #"\Uxxxxxxxxxxxxxxxx" long unicode chars
////print("\U0001F605")  #smile emoje
////    #"\---" octal value
////print("\141")    #a
////    #"\x---" hex value
////print("\x61")    #a
//
//
//str = "jamal\nNasar";
//console.log(str.length, str) // 11 b\c the \n is single char     // jamal\nNasar
//console.log("jamal\nNasar");////jamal
                             ///Nasar

// raw str:

const filePath = String.raw`C:\Development\profile\about.html`;

console.log(`The file was uploaded from: ${filePath}`);
//                                                              MDN DOCS----> VVV IMP

//methods=> functions for a specific dats type



//STRING METHODS:
//    these are built in func to manipulate string

// str.length ==> a property of str which will just give its value
// str.toUpperCase() ==> a method of str which do something with the str

//let str = "jamal kamal";
//console.log(str.toUpperCase());     // JAMAL KAMAL      /camel case

// BUT>>>
//let str = "jamal kamal";
//str.toUpperCase();
//console.log(str);       // jamal kamal     WHY it didn't in all caps

////b\c
////it didn't change the original str it create a new one with new value
//let str = "jamal kamal";
//let newStr=str.toUpperCase();
//console.log(str,newStr);        //jamal kamal JAMAL KAMAL

// but if we wanns chnage it
let str = "jamal kamal";
let newStr=str.toUpperCase();
str=newStr;
console.log(str,newStr);        // JAMAL KAMAL JAMAL KAMAL

// THE ORIGINAL STR REMAIN UNCHANGED B\C STRINGS ARE IMMUTABLE IN JS=> SO NO CHANGE POSSIBLE

// toLowerCase method:
let newerStr=str.toLowerCase();
console.log(str,newStr,newerStr);       // JAMAL KAMAL JAMAL KAMAL jamal kamal

//trim method:  --> removes all whitespaces
let newestStr = "    jamal    nasar    ";
console.log(newestStr.trim());     //jamal    nasar      ??// it removes only spaces at start and at end
let last = "    jamal nasar    ";
console.log(last.trim());  //jamal nasa

//str.slice(start index,end) methoad:   returns part of str
let str1="jamal Nasar";
console.log(str1.slice(3,5));   // al   // the last index not included
console.log(str1.slice(3)); // al Nasar // start at the starting index and upto last

//str.concat():      concatination
let str2= "maryam bibi"
console.log(str1.concat(str2))      // jamal Nasarmaryam bibi       // 1st one 1st and 2nd one 2nd
console.log(str2.concat(str1))      // maryam bibijamal Nasar
//we can also concatinate str by "+"
console.log(str1+str2)  // jamal Nasarmaryam bibi
console.log("hello"+123)    //hello123      // js 1st converts the 123 into str then concate it with th str


//replace method:
//str.replace(searchVal,newVal)         // we search for a value and then replace it with the new value
let str3="hello...";
console.log(str3.replace("l","y"));     //heylo...      // only one the 1st one-> replace only once
console.log(str3.replace("lo","p"));    // help...      // js fined their combo

//to replace all: str.replaceAll()=> replace all matching values
console.log(str3.replaceAll("l","y"));      //heyyo...
let str4="hellolololo...";
console.log(str4.replaceAll("lo","p"));     // helpppp...

//str.charAt(idx) method:  => if we wanna return a char at idx
console.log(str4.charAt(0));        // h

//        // immutability of str
//str4[4]=r;
//console.log(str4);        // not possible in str
// so if we wanna bring change in str we have to make another new str by replace method in this case
str4=str4.replace("h","y");
console.log(str4)       // yellolololo..



//PRAC:
//PROMPT THE USER TO ENTER THEIR FULL NAME. GEN A USERNAME FOR THEM BASED ON THE INP. START USERNAME WITH @, FOLLOWED BY THEIR FULL NAME AND ENDING WITH FULL NAME LENGHT.
//I.E NAME=JAMAL KAMAL THEN USER NAME WILL BE @JAMALKAMAL10
let fullName = prompt("enter your full name without spaces:");
let username = "@"+fullName+fullName.length;
console.log(username);








