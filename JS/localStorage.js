
// console -> key , value pairs data stoge formate
// localStorage.setItem("leds","fgdhjsks nxm") //to set an item 
// localStorage.clear() // to clear all the local database

// application tab in dev tools and in local storage tab
// and if we refresh the page after setting an item it remains


// so we can use it

// if i now remove the setItem statement from the code and re run it or refresh the page the data will still store in local storage === persisitant storage and i can access it via :
console.log(localStorage.getItem("leds"))  //"fgdhjsks nxm" as it is stored

// can only be deleted if i do ==> localStorage.clear()

// you can only store string in the local storage; that's a limitation

// onhce store will remain here untilll manually deleted


// mdn doc => window.localStorage