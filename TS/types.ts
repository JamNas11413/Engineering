// any js code that we have will be ts too as it is their super set
// type error can creash our app   THE PROBLEM IS SOLVE BY TS

// let myName = "Jamal Qadar"
// // on mouse over it guesed the type of the var by the value
// // to prove
// myName = 4  // Type 'number' is not assignable to type 'string'.   ==> on mouse over


// primitive ts data types
// numbers, string, boolean

// explicitely:
let myName:string = "Jamal Qadar"       // lowercase 1st letter as it is not constructer

let num:number = 2345665432443

let falsey:boolean = false


// we can make our own datatypes too
// CUSTOM TYPES _> using type kw and cap 1st letter

type Food = string
let myFavFood:Food = "alpahm"


// custom types around obj
type Person = {
    name: string
    age: number
    isStudent: boolean                 // in custom obj we do have to separate the elemnt by camma but when we creat our own obj we don't need to to that but we can do it by a camma a swell as a semicolon
    address?: {              // make it optional via the ?  BUT  it will reduce type safety
        street: string
        city: string
        country: string
    }
}

let person : Person = {
    name: "kamal",
    age: 17,
    isStudent: false,
    address: {
        street: "derai",
        city: "swat",
        country: "Pak"
    }
}








// //{
// type Person = {
//     name: string
//     age: number
//     isStudent: boolean                 
//     address: {              
//         street: string
//         city: string
//         country: string
//     }
// }

// // can also

// type Address = {              
//         street: string
//         city: string
//         country: string
//     }

// type Person = {
//     name: string
//     age: number
//     isStudent: boolean                 
//     address: Address
// }
// // }




// typing arrays
let ages:number[] = [12,34,56,27,17]            // we tell ts that ages will be an arrayt of numbers





// litteral typesx 
let myName1 = "jamal"
// ts know its type, we can know via hover   => string

const myName2 = "jamal"
// via hover ==> const myName2: "jamal"

// AS IT IS A CONST MEANING HEAVIBG ONLY ONE VALUE SO ITS TYPE IS THE VALUE IT HAVE
// VALUE TYPE === LITERAL TYPE

const myName2:"jamal" = "jamal"




// UNIONS:
    // only allows to be one otf them

type UserRole = "guest" | "member" | "admin"        // | -> single pipe char can be pronounce as || (or)

let user1 : UserRole = "member"

// we can aslo use unions with generic gypes i.e

let valiues: string | number




// TYPE NARROWING:
    // when we dont know what will be the tupe of our func ts tells us us that narrow down the type 
    // more...




// BE EXPLICIT WHENEVR U CAN IN TS 



// funcs that doesn't return anything
    // called void func 
    // and other known as fruitfull func {in python hhhhhh}

function logOut():void {           // we can be exploicitely tell it that it gonna be void 
    console.log("this is void func as it doesn't return anything!")
}

logOut()

// if the func return something then we don't needa tell it there we just use the return kw and can tell the type i.e


function logOuty(a, b):string | number | undefined {        // it will return one of them string | number | undefined       
    return a + b
}

logOuty(2,4)
logOutt("gfhjdk", "ghdjk")




// VOID IS A TS SPECIFIC TYPE AND THERE ARE OTHER TOO i.e any


// any type 
    //if u make something any u are assentially turning off ts to check for that value's type

let valx =  1
// on hover: let valx: number
// it will show error if reassign it to a str, run a str method etc 

let valy:any = "fcghj"
valy = 1        // no error as it is via any
valy.map()



// we shouldn't use it 
// we can use it if we converted a js file to ts and suddenly hundred of error pop up and we don't wanna fix that now so we can just make it any and no errors ===> temperorilly      HHHHHHHHHHHhhhh





// UTILITY TYPE:
    // we might use a type only once so their creation van be time consuming we can take help from the built in utility types
    // 
    // in ts, there are a buch of types; like a func they take other types in as perameter and return a new type, with some changes made to it
    //buolt-in to ts, perform commanly needed modification to existing types
    // use generic synatx using angle barackets (<>)

// eg 
type Pizza1 = {
    id: number
    name: string
    price: number
}
// now i wanna make the properties optional i can amnnually write the type again and make eah property optional(?) 
// but we can use a utility class called partial


// 1. PARTIAL
type updatedPizza1 = Partial<Pizza1>


// there are many other i can search for their docs 

// 2. Omit 
    // takes in a type AND  a string (or union of strings) property name(s), and return a new type with those properties removed  
// single string
type updatedPizza2 = Omit<Pizza1,"id">

// union string

type updatedPizza3 = Omit<Pizza1,"id" | "name">  // will omit all the provided 


// there are many other i can search for their docs 





// GENERICS:
//  // A POwERFULL TOOL THAT ALLOW US TO ADD FLEXIBITY TO EXISTING FUNCTIONS, TYPES, ETC.
    // act like a func perameter(a placeholder for a real value which then wee use inside the func) but for types (placeholder for a type)
    // use angle brackets syntax(<>)


const gamescore = [12,34,56,78,5554,32,21,23,45,356]
const favThings = ["pizza", "burger", "fries", "coke", "pepsi"]
const voter = [{"name": "jam", "age": 17}, {"name": "kam", "age": 18}, {"name": "sam", "age": 19}]

// we can make a func that return the first element of an array but we want it to work for any type of array not just number array so we can use generics

function getFirstElement<T>(arr:T[]):T {   // the array can be of anytype so we don;t know the type      // T is a convention but we can use any letter // it is a placeholder for the type that we will provide when we call the func // we can also use multiple generics i.e <T, U, V> etc // we can also use it in the return type as well as the parameter type
    return arr[0]
}

getFirstElement(gamescore)       // on hover: const gamescore: number[]
getFirstElement(favThings)      // on hover: const favThings: string[]
getFirstElement(voter)          // on hover: const voter: { name: string; age: number; }[]

// we can also use multiple generics i.e    
function getFirstElement2<T, U>(arr:T[], defaultValue:U):T | U {    // U is another generic type that we can use for the default value // it will return either T or U depending on whether the array is empty or not
    return arr[0] || defaultValue
}

getFirstElement2(gamescore, 0)       // on hover: const gamescore: number[]
getFirstElement2(favThings, "nothing")      // on hover: const favThings: string[]
getFirstElement2(voter, {name: "no one", age: 0})          // on hover: const voter: { name: string; age: number; }[]   





