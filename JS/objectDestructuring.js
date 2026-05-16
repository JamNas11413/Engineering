// Object Destructuring:
    // extract properties from objects
    // it enables us to extract properties from objects into distinct vars

// const favSeries= {
//     title: "Breaking Bad",
//     year: 2015,
//     genre: "Crime Drama",
//     star: "Walter White / heisenberg"
// }

// // const title = favSeries.title
// // const yearRelease = favSeries.year
// // const genere = favSeries.genre
// // const star = favSeries.star

// // console.log(`My favorite series is ${title} starring ${star}. it is a ${genere} and released in ${yearRelease}.`)
// // it time / and memory unfriendlyt and mpore buggy

// // so i can

// const {title, year, genre, star} = favSeries  // list of keys store in  alist and name of the obj is assigned


// console.log(`My favorite series is ${title} starring ${star}. it is a ${genre} and released in ${year}.`)



// const favSeries= {
//     title: "Breaking Bad",
//     year: 2015,
//     genre: "Crime Drama",
//     star: "Walter White / heisenberg"
// }

// // const title = favSeries.title
// // const yearRelease = favSeries.year
// // const genere = favSeries.genre
// // const star = favSeries.star

// // console.log(`My favorite series is ${title} starring ${star}. it is a ${genere} and released in ${yearRelease}.`)
// // it time / and memory unfriendlyt and mpore buggy

// // so i can

// const {title, year, genre, star} = favSeries  // list of keys store in  alist and name of the obj is assigned


// console.log(`My favorite series is ${title} starring ${star}.it is a ${genre} and released in ${year}.`)




// challenge
const dreamHoliday = {
    distination: "Berlin",
    activitty: "beach and ilands",
    accomudation: "fancy resturant",
    companion: "Maryam"
}

const {distination, activitty, accomudation, companion} = dreamHoliday;

console.log(`
    I would like to go to ${distination} and sit there on ${activitty} rest in a ${accomudation} with mhy girl ${companion}.
    `)