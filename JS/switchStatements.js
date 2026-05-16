// Switch Statements:
    // select one of many code blocks to execute

// vending machine:

// price list
    // coffe : $2
    // sandwitch; $5
    // salad $4
    // lemon cake $3

function selectItem(item) {
    let price = 0; // initialize it to zero

    switch(item) {
        case "coffe":   // coparison happens b\w the item is strict cpoparison i.e item === "coffe" {both type and value}
            return price = 2
            break    // if the case executeds we wanna break it and no other will loocked out
        case "sandwitch":
            return price = 5;
            break
        case "salad":
            return price = 4;
            break
        case "lemon cake":
            return price = 3;
            break
        default:  // will exe if non of the casses satisfied // the default can be any where not necessary to be at end but should be at end for convenience
        // we don't have the break at the last case: wheter its a case or a default statement b\c after this the it will break by default as it is end 
            return `sorry we dont sell ${item}!`
    }
}
console.log(selectItem("biscuits"))