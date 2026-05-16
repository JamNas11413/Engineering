//Arrays:      -> I.E USED TO STORE INFO ABOUT AN ITEM AT AMAZON
//    a data structer
//        collection of items
//        storing multiple values in same var
//        stores info in a linear way(one after one at indices)
// can also have different data types but generally it is preffered to make of same kind
// creating:
let marks = [23,45,67,8,9,3,4,6,77,90];
console.log(marks);     // (10) [23, 45, 67, 8, 9, 3, 4, 6, 77, 90]     // the 10 is size of the array
//arrays have length property:
console.log(marks.length);          // 10
console.log(typeof marks)       // object   //arrays are objects -> non primitive(advance)  //we treat it  a little different from obj
// arrays is an object that have key value pairs but instead of key we have indices


//indices
fourth=marks[4];
console.log(fourth); // 9
console.log(marks[100]);        // undefined

//arrays are mutable
marks[4]=90;
console.log(marks, marks[4]);  // (10) [23, 45, 67, 8, 90, 3, 4, 6, 77, 90]  90

//Looping Over an array:
for (let score in marks) {
    console.log(score,"-", marks[score])
}
//0 - 23
//1 - 45
//2 - 67
//3 - 8
//4 - 90
//5 - 3
//6 - 4
//8 - 77
//9 - 90

// iterables => items on which we can iterate like str, arrays, objects etc


let cities = ["london", "NYC", "bankcok", "lahore","Peshawar"];
for (let city of cities) {
    console.log(city.toUpperCase());
}

//prac:
let marksStd = [85,97,44,37,76,60]
i = 0;   //at every cycle it will be increased by one
sum =  0;
for (let markStu of marksStd) {
    sum += markStu;
    i++;
}
console.log(sum / 6)

i=0;
let prices = [250,645,300,900,50];          // 10% of 250 = 25 so after offer price becomes 250-25==225
for (let price of prices) {
    price = price * (10/100);
    prices[i] -= price;
    i++;
}
console.log(prices);        // (5) [225, 580.5, 270, 810, 45]


//METHODS:
//    TWO TYPES:
//        1. CHANGE THE ARRAY-> pop(), push(),unshift(), shift(), splice()
//        2.  RETURN NEW ARRAY->toString(),concat(), slice()

// PUSH():                  // push in programming means add
prices.push(452)        // will add to end
console.log(prices);        //(6)[225, 580.5, 270, 810, 45, 452]
//adding multiple:
console.log(prices.push(154,154,156,258)) /// return idx of added elemnt
console.log(prices);        // (10) [225, 580.5, 270, 810, 45, 452, 154, 154, 156, 258]    // added sequentially


//pop()                            // pop in programming means delete
p=prices.pop()                     // as it return something so i can assign it to some var     // delete from the end
console.log(p,prices);        // 258 (9) [225, 580.5, 270, 810, 45, 452, 154, 154, 156]       // deleted last one

// POP AND PUSH CHANGE IN ORIGINAL ARray
// toString() +> to converts an array into str
console.log(prices.toString())      // 225,580.5,270,810,45,452,154,154,156
console.log(prices);        // (9) [225, 580.5, 270, 810, 45, 452, 154, 154, 156]
//HENCE:
 //   toString() METHOD CREATE A NEW ARRAY and don't change in original one

// // concat(): to concatenate multiple arrays and returns / create new arrays
//console.log(marks.concat(prices));      // (19) [23, 45, 67, 8, 90, 3, 4, 6, 77, 90, 225, 580.5, 270, 810, 45, 452, 154, 154, 156]  //concat 1st marks then prices as we entered
//console.log(marks);         //(10) [23, 45, 67, 8, 90, 3, 4, 6, 77, 90]
//console.log(prices);        //(9) [225, 580.5, 270, 810, 45, 452, 154, 154, 156]
////hence:
//// return new array
//
//  // unshift:  add to start
//marks.unshift("START");
//console.log(marks);     // (11) ['START', 23, 45, 67, 8, 90, 3, 4, 6, 77, 90]
////hence:
//    // it change in originals
//
// // shift(): delete fron start
//marks.shift();
//console.log(marks);     // (10) [23, 45, 67, 8, 90, 3, 4, 6, 77, 90]
////hence:
//    // it change in originals
//
//
//// slice():   returns a piece of the array
////slice(startIdx, endIdx)
//
//// NOT CHANGE IN ORIGINAL ARRAY
//console.log(marks.slice(2,7)); // ending idx non exclusive  // (5) [67, 8, 90, 3, 4]
//console.log(marks.slice()); // (10) [23, 45, 67, 8, 90, 3, 4, 6, 77, 90]        // entire array
//// can also be use for making copy of our array
//console.log(marks.slice(1));    // (9) [45, 67, 8, 90, 3, 4, 6, 77, 90] // 1 to end
////console.log(marks.slice(,7));   /// SyntaxError: Unexpected token ','
//
//
//// splice():
////    change in original array(add, remove, replace)
////        splice(startIdx, delCount, newEle)
//
//marks.splice(2,2,101,102)       // start from idx 2 then remove 2 elements starting from idx2 (including idx 2) then add the remaining all elements starting from the 2 idx
//console.log(marks)      // (10) [23, 45, 101, 102, 90, 3, 4, 6, 77, 90]     // deleted 2 and 3 which are 67 and 8 and replaces them by 101 and 102
//
//// adding only at an idx
//marks.splice(2,0,123,258)    // adding 123 and 258
//console.log(marks)  // (12) [23, 45, 123, 258, 101, 102, 90, 3, 4, 6, 77, 90]
//// size increased by the no. of elements we added
//// adding started from idx 2 and the old idx two element move idx 4
//
////deleting element whoes idxes we know
//marks.splice(2,2)
//console.log(marks)  // (10) [23, 45, 101, 102, 90, 3, 4, 6, 77, 90]
//
////replacing an element i.e i wanna replace the 101 idx 2 by 57
//marks.splice(2,1,57)
//console.log(marks)  // (10) [23, 45, 57, 102, 90, 3, 4, 6, 77, 90]
//
////CAN ALSO ACT LIKE SLICE BUT CHANGES THE ARRAY
//marks.splice(2)
//console.log(marks)  //(2) 23, 45]
//// WHEN U DIDIN'T PASS THE NO. OF ELEMENT TO DELETE IT WILL UNDERSTAND IT AS START FROM THE GIVEN IDX AND DELETE ALL THE OTHERS
//
////MPT
//marks.splice()
//console.log(marks)      // (2) 23, 45]      // NO CHANGE IN OUR ARRAY
//
//
////PRAC:
//let comp=["google", "mete", "uber", "mediLink","IBM","Netflix"]
//comp.shift()
//console.log(comp)   //(5) ['mete', 'uber', 'mediLink', 'IBM', 'Netflix']
//console.log(comp.splice(1,1,"OTA")) // ['uber'] // return the element which is removed
//console.log(comp)   // (5) ['mete', 'OTA', 'mediLink', 'IBM', 'Netflix']
//console.log(comp.push("amazon")) //6   // return the element which is
////console.log(comp)   // ['mete', 'OTA', 'mediLink', 'IBM', 'Netflix', 'amazon']