// https://www.geeksforgeeks.org/javascript/explain-scope-and-scope-chain-in-javascript/

// Scope

//     Scope in JavaScript determines the accessibility of variables and functions at various parts of one's code or program.
//     In other words, Scope will help us to determine a given part of a code or a program, what variables or functions one can access, and what variables or functions one cannot access.
//     Within a scope itself, a variable a function, or a method could be accessed. Outside the specified scope of a variable or function, the data cannot be accessed.
//     There are three types of scopes available in JavaScript:
//           Global Scope, Local / Function Scope, and Block Scope. 



// Global Scope:

//     Variables or functions (or methods) that are declared under a global namespace (like area or location) are determined as Global Scope. 
//     It means that all the variables that have global scope can be easily accessed from anywhere within the code or a program.

// Block Scope:

//     Block Scope is related to the variables or functions which are declared using let and const since var does not have block scope.
//     Block Scope tells us that variables that are declared inside a block { }, can be accessed within that block only, not outside of that block.

// Local or Function Scope:
    // Variables that are declared inside a function or a method have Local or Function Scope.
    // It means those variables or functions which are declared inside the function or a method can be accessed within that function only.  