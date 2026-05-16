//Operators:
//    used to perform some operation on data
//        1. arithmatic: +,-,*,/

let a=5;
let b=4;
console.log("a = ",a, "b = ",b);
console.log("a + b =  ",a+b);
console.log("a - b =  ",a-b);
console.log("a * b =  ",a*b);
console.log("a / b =  ",a/b);

//          2. modulus:
let c = 5;
let d = 2;
console.log("c = ",c, "d = ",d);
console.log("c % d = ", c%d);

//           3. exponentation:
console.log("c ** d = ", c**d);

//               4. increment(++) {increase by one}=> is a UNARY OPERATOR[NEED ONLY ONE VAR]
//A+1 == A++ AND A-1 == A--
// == A=A+1 AND A=A-1
let g = 5;
let h = 3;
console.log("g = ",g, "h = ",h);
g=g+1;
console.log("g=",g)  // 6

a++;  // post increment=> the value will change from the upcoming line not from this line
console.log("g=",g) // 6
// post incre
let a=5;
let b=2;
console.log("a = ",a, "b = ",b);
console.log(a++) //5
console.log(a) //6

++a;  // pre increment => the value will change 1st and from this line before it is used in an exp
console.log("g=",g) // 6
pre incre
let a=5;
let b=2;
console.log("a = ",a, "b = ",b);
console.log(++a) // 6
console.log(a) // 6

console.log("++h = ",++h, "h++ = ",h++)
console.log(h++,  "H++")


//                5. decrement(--) {decreased by one }=> is a UNARY OPERATOR[NEED ONLY ONE VAR]
a=a-1;
console.log("a=",a);  // 6
a--;  // post decrement =>
console.log("a=",a); // 5

post decre
let a=5;
let b=2;
console.log("a = ",a, "b = ",b);
console.log(a--) // 5
console.log(a) // 4

--a;  // pre decrement =>
console.log("a=",a);

pre decre
let a=5;
let b=2;
console.log("a = ",a, "b = ",b);
console.log(--a) // 4
console.log(a) // 4


//            2. assignment operators:
//            = -> value assign from right to left
//            += -> i.e a += 1 == a=a+1
//            -+ -> i.e a -= 1 == a=a-1
//            *= -> i.e a *= 1 == a=a*1
//            **= -> i.e a **= 1 == a=a**1
//            /= -> i.e a /= 1 == a=a/1
//            %= -> i.e a = a % 1 == a %=  1

let f= 4;
let s= 5;

a+=4;
console.log("a+=4",a);
a-=4;
console.log("a-=4",b);
a*=4;
console.log("a*=4",a);
a**=4;
console.log("a**=4",a);
a/=4;
console.log("a/=4",a);


//////COMPARISON OPERATORS:  ==> return boolean
//1. EQUAL TO: ==
//2. NOT EQUAL TO: !=
//3. EQUAL TO AND TYPE: ===  => stricter version
//4. NOT EQUAL TO AND TYPE: !==
<,>,>=,<=

let y=2;
let e=3;
console.log("y==e",y==e) //false
console.log("y!=e",y!=e) // true

let u=4; // number
let i="4"; // str
console.log("u==i",u==i) // true
// so the js implicitly  converts the str to number by default
// SO IF WE DON'T WANT. then:
console.log("u===i",u===i) // false // it also compare the types of them
console.log("u!==i",u!==i) // true

////LOGICAL OPERAToRS: RETURN TRUE OR FALSE
//AND (&&): RETURN TRUE IF BOTH CONDITION ARE TRUE
//OR (||){PIPE SYMBOL}: RETURN TRUE IF 0NE OF THE CONDITIONS IS TRUE
//NOT (!): RETURN TRUE IF NON OF THE CONDITION ARE TRUE

let r=2;
let k=3;
console.log(k>r && r<k); // true
console.log(k>r || r<k); // true
console.log(!(k>r && r<k)); // false

// logical operators
add &&
or ||



//Conditional Statements:
//     to implement a condition in the code
// syntax
//    if (condition) {   // if the condition becomes true in the braces the statements inside the block will execute otherwise will skipped
//        implementing;
//    }
let age =2;
if (age > 18) {
    console.log("you are an adult");
}
else if (age <= 12) {
    console.log("you are a child");
}
else if (age >= 12 && age <= 18) {
    console.log("you are a teen");
}
else {
    console.log("you are not an adult");
}


if (sum <= 21) {   // js evaluate the exp inside the parenthesis and return a boolean value and if it is true then the block exe other wise ignored
    console.log("want anew car!")
}
else if (sum === 21) {
    console.log("Wohoo! we've got blackjack!")
}

else {
    console.log("we're out!!!")
}

// but what if the we pass empty str as a condition
if ("") {
    console.log("empty!!!!")
}
else {
    console.log(" not   empty!!!!")
}
//  not   empty!!!!
// b\c the empty str always return false


if (" ") {  // this time not empty
    console.log("empty!!!!")
}
else {
    console.log(" not   empty!!!!")
}
// empty!!!!
// b\c thre is sometyhing in the condition that can be true in other words  better than else

// //TERNARY OPERATORS: --> WORKS ON 3 OPERANDS
// //OPERANDS:
// //    CONDITION ?TRUE OUTPUT :FALSE OUTPUT   => THE ? AND THE COLON ARE CALLED TERNARY OOPEARTORS

// let age1 = 25;
// //res=age <30 ? "younger" : "young";
// //console.log(res)
// //or
// console.log(age <30 ? "younger" : "young");

// // should use for small condition and for long we should write conditionals

// //switch statements




// //PRAC
// //1. get user to input a number using prompt("enter a no."). check if the no. is a multiple of 5 or not
// let num = prompt("Enter a umber:")

// if (num < 5) {
//     console.log(num, "is lesser than 5.")
// }
// else if (num % 5 == 0) {
//     console.log(num,"is multiple of 5");
// }
// else {
//     console.log(num,"is not multiple.");
// }


// //2. wac which can give grades to stds acc to their marks:
// //99-100-A, 70-89-b, 60 - 69-c, 50 - 59-d, 0 - 49- f

// let marks=prompt("enter you marks: ");
// if (marks >= 90 && marks <= 100) {
//     console.log("you are in A having marks:", marks);
// }
// else if (marks >= 70 && marks <= 89) {
//     console.log("you are in B having marks:", marks);
// }
// else if (marks >= 60 && marks <= 69) {
//     console.log("you are in C having marks:", marks);
// }
// else if (marks >= 50 && marks <= 59) {
//     console.log("you are in D having marks:", marks);
// }
// else {
//     console.log("you are in F having marks:", marks);
// }

