// constructers:b
    // in js a constructer gives you an obj
    // TYPES of constructoror 
        // 1) inbuilt constructors
            // provide objs in differnt  predetermined formates, like date oj, error obj and object for each data type
        // 2) custom contructer:
            // constructer we design on our own to produce obj of our specific need

// at bottom of most webs there is a copyright msg and and date whichis always correct, so how that happens 
// many ways for doing so but easiest one will be to use a date constructer

// dateconstructer give us accourate date when we asked it

//the inbuilt constructer alwahys hgave an upper case 1st letter

// const dateSnapshot = new Date()
// console.log(dateSnapshot, typeof dateSnapshot)  // Mon Feb 09 2026 07:20:19 GMT+0500 (Pakistan Standard Time) 'object'

// getting year just

// const dateSnapshot = new Date()
// console.log(dateSnapshot.getFullYear(), typeof dateSnapshot, dateSnapshot.toString())
// // coppyright msg
// console.log(`Copyright ${dateSnapshot.getFullYear().toString()} all rights reserved.`)

// luxon package can be a helper when working with date and time in js while complex task






// error constructer:
    // error detection -> very useful 

    // when an app fails and you don't know whats happening is a lot more frustrating

    //error constructer gives us the ability to creare our custom error msgs

// function checkUser(User) {
//     console.log(user)
// }
// checkUser()// undefined

// we canm create our own custum msg
// function checkUser(User) {
//     if (User) {
//         console.log(User)
//     }
//     else {
//         console.log(new Error("No usename provided"))
//     }
// }
// checkUser()
// Error: No usename provided

// i can also do it with the throw kw
// function checkUser(User) {
//     if (User) {
//         console.log(User)
//     }
//     else {
//         throw new Error("No usename provided")
//     }
// }
// checkUser() //  Error: No usename provided     {red}


// but whyen the throw kw will exe it will stop any code after it i.e

function checkUser(User) {
    if (User) {
        console.log(User)
    }
    else {
        console.log("i exe")
        throw new Error("No usename provided")
        console.log("i won't exe")
    }
}
// checkUser() //  i exe
            //  Error: No usename provided
// the throw kw end exe of the code after it 


// constructers for the datatypes

// String()
// Number()
// Array()
// Object()
// Boolean()

// each of them has capital first letter and brackets at end

// const person = new Object()
// person.name = "Maryam"
// console.log(person)// {name: 'Maryam'}

// much better to use the object litteral
const person = {}
person.name = "Maryam"
console.log(person)// {name: 'Maryam'}

// you can do the same with all of these