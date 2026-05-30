const manu = [
    {name: "xyz", price: 123},
    {name: "xyz1", price: 1231},
    {name: "xyz2", price: 1232},
    {name: "xyz3", price: 1233}
]

let cash = 100;
let orderQueue =[]
let orderObj = {}
let id = 0
function addNewPizza(ele) {
    orderQueue.push(ele[0])
    
}

function placeOrder(pizzaName) {            // we canb do this via find method
    for (let i of manu) {
        if (i.name === pizzaName) {
            cash += i.price
            orderQueue.push(i)
            return orderObj = {name: i.name, status: "ordered", id: id++}
        }
    }
}
placeOrder(xyz3)
console.log(cash, orderQueue, orderObj)