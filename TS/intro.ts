// TypeScript:
//     super set of js that constraint to your code and so help u write softwares wioth fewer bugs

// why:
//     confidence
//     productivity
//     industory standerd



// Errors in dsevelopment means less error in deployment

// ts main focus -> fixing possible runtime errors {specifically runtime type error} 
//     it won't protect us againist logical errrors 


type Pizza = {
    id: number
    name: string
    price: number
}

type Order = {
    id: number
    pizza: Pizza
    status: "ordered" | "completed"
}
const manu:Pizza[] = [
    {id: 1, name: "xyz", price: 123},
    {id: 2, name: "xyz1", price: 1231},
    {id: 3, name: "xyz2", price: 1232},
    {id: 4, name: "xyz3", price: 1233}
]

let cash:number = 100;
let orderQueue:Order[] =[]
let orderObj = {}
let id:number = 0


function addNewPizza(ele:Pizza):void {
    manu.push(ele)
    
}

function placeOrder(pizzaName:string):void {            // we can do this via find method
    for (let i of manu) {
        if (i.name === pizzaName) {
            cash += i.price
            orderQueue.push(i)         
            let orderObj:Order = {name: i.name, price: i.price, status: "ordered", id: id++}

        }
    }
}

placeOrder("xyz3")
console.log(cash, orderQueue, orderObj)