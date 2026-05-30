console.log("hello typescript");
// TS can't be run by browser so we first compile it to JS by typescript compiler   {to do so : type "npx tsc filename.ts" in terminal}
// implicit types
let hello = "hello world";
// hello = 42; // Error: Type 'number' is not assignable to type 'string'

// explicit types
let count: number = 10;
count = 20; // valid
// count = "twenty"; // Error: Type 'string' is not assignable to type 'number'

// union types
let mixed: string | number = "hello";
mixed = 42; // valid
// mixed = true; // Error: Type 'boolean' is not assignable to type 'string | number'  

// built-in func
// Boolean
// Number
// String
// Tuple->express an array with fix number of elements whose type is known but don't needa be the same
type stringAndNumber = [string , number];
let tup: stringAndNumber = [ "jamal", 10];  /// valid
let xtup: stringAndNumber = ["jamal", "maryam"] // Type 'string' is not assignable to type 'number'.
// Array
// Enum-> in c£ and java an enum is a eway of giving more friendly nameto set of numeric values. it allow to define a set of named constts using it can make it easier to document your intent or create a set of distinct cases.
enum Continents {   // by default if u don't specify any thing the 1st thing in enum will be 0, following by 1 and so on, as they are self inctrementing values {this behaviour is helpful when we want distinct values in the same Enum}
    northAmerica,
    africa,
    asia,
    southAmerica,
    Europe,
    Austrailia,
    intarctica
}
// usage 
var region = Continents.africa;//1
// Unknown 
// Any 
// Void 
// Null 
// Undefined



// interfaces
interface User {        // convenrtiionally start by cap latter
    name: string;
    id: number;
}

// obj of the interface
const user: User  = {
    name: "ijaz",
    id: 24
    // invalid: xyz // an error as it is not in User interface
}

// Composing types -> union of types
type WindowStates = "open"| "closed" | "mod-open";
// const window1: WindowStates = "idk"  // ewrror not assignable -> error shows by howering

type oddNumToTen = 1 | 3 | 5 | 7 | 9;  // odd to ten can only be one of these
const val: oddNumToTen = 3; // valid
// const val1: oddNumToTen = 6; // in-valid

// union provode a way to handle different dypes too
const getlenght = (peram: string | string[] | any[]) => {  // string[] => means array of str        // any[] => array of anything
    return peram.length;
}
getlenght("jamal nasar khan ")  //
// same for other types

// but 
// getlenght(7)  // Argument of type 'number' is not assignable to parameter of type 'string | any[] | string[]'.
