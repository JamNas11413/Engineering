// // objects:
// //     store data in dept - composite / complex data type
// //     store dat in form of key value pair separated by colon(:)
// //     elemnts separated by semi-colon{semicolon b\w elemnts not at end }

// let course {
//     title: "Depp Learning by MIT"
//     lesson: 16;
//     level: "intermediate";
//     lenght: 63;
//     tags: ["html", "css"]
    
// }

// // we can access to the vlaues and properies by dot notation
// console.log(course.title)
// console.log(course.lenght)

// // and any time we use the dot we are working with objs like the console.log() where the console is an object

// // can also acces to the values by bracket Notation
// console.log(course[title])


// // prac
// let castle = [
//     name: "Centeral London Castle";
//     availible: true;
//     price: $200;
//     fascilities: ["room", "bed", "shower"]
// ]




// METHODS
// make function inside an object inside i.e 
let course {
    lenght: 63;
    tags: ["html", "css"];
    func: function () {    // we wont give it a name it will be an anonymous func
        console.log("im an anonymous func or more specifically method for the object course")
    }  // can be invoke it via the dot notation
}

course.func()  // var name with the ()