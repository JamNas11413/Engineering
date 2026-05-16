// increment(++) {increase by one}=> is a UNARY OPERATOR[NEED ONLY ONE VAR]

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
// pre incre
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