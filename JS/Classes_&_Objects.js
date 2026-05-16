//Classes & Objects:
    // oBJECT:
        // A JS OBJECT IS AN ENTITY HAVING STATE AND BEHAVIOUR (state/PROPERTIES AND METHODS)=> IT WILL HAVE SIMETHING(PROPERTIES->ATTR/VARS ETC) AND IT WILLL DO SOMETHING(METHODS )
//const std = {
//    name: "jamal",           /// attr/states
//    class: "10th",
//    marks: 86,
//    printMark: function () {        // method/behaviour
//        console.log("marks =",marks)
//    }
//}
//console.log(std);   // {name: 'jamal', class: '10th', marks: 86, printMark: ƒ}      // the marks isn't printeed so, we can use "this" kw
//console.log(std["name"]);   // jamal
////console.log(std.printMark);  // ƒ () {        // method/behaviour
//                                //        console.log("marks =",marks)
//                                //    }
//console.log(std.printMark());       // marks is not defined  // we can solve it by 'this'


const std = {
    name: "jamal",           /// attr/states
    class: "10th",
    marks: 86,
    printMark: function () {        // method/behaviour
        console.log("marks =",this.marks)       // this kw means this obj i.e in this case it means => this.marks====>std.marks(this=std)
    }
}
console.log(std);
console.log(std.printMark());   // marks = 86
//solved



// PROTOTYPES IN JS:
    // js obj have a special property called  prototype.
    //i.e if i make an array:
let arr = ["apple","banana", "mango"];
console.log(arr);       // defined
//                            (3) ['apple', 'banana', 'mango']
//                            0: "apple"
//                            1: "banana"
//                            2: "mango"
//                            length: 3
//                            [[Prototype]]: Array(0)

// above is a prototype too

//so now if i enter arr.push() or other method => wher from the methods are coming as we didn't define it; so they are comming from the prototype(when we create an obj it inherites the properties and methods from their protoype.


//we can crete our owm pt too:
const employ = {
    calcTax() {         // e can define func in obj like this toooooooooooooooooo
        console.log("tax rate is 10%.")
    }
}
//console.log(employ.calcTax());      // tax rate is 10%.
//
//const employ1 = {
//    salary() {
//        console.log("salary is 10%.")
//    }
//
//}

//// we want the calcTax func in employ1 also, so if i want function/properties of one obj in another obj we can write the doner(who have the method) obj as a prototype to our reciever(who wants te method etc) obj, syntax: __proto__ used to set a prototype i.e,
//employ1.__proto__=employ;
//console.log(employ1.calcTax()); // tax rate is 10%.

//prototype may null or a refrence


//but...
// if i write the same func with the same name in the object itself and the same func is in its prototype?
//console.log(employ.calcTax());     .

const employ1 = {
    salary() {
        console.log("salary is 10%.")
    },
    calcTax() {         // this func is alredy in its prototype
        console.log("tax rate is 50%.")
    }
}
employ1.__proto__=employ;
console.log(employ1.calcTax());     // tax rate is 50%.     // the object specific one is executed b\c its more specific to the obj
//hen we are building a project, for that we will use which type of techs etc completely depends upon the type of the project, i.e, in some we need classes while in other not}




//Classes:
    // blue print for my obj (thye obj will have the properties my class have)
    // we create classes when we wanna crete more objs
//    syntax:
            // class MyClass {
    //            constructor() {...}
    //               my method() {..}
//          }

class ToyotaCar {
    start() {           // method
        console.log("started");
    }

    stop() {                /// method
        console.log("stoped");
    }
    brand(brand) {          // property / var
        this.brandName=brand        // means using this class any obj created will have this property
    }
}
//console.log(ToyotaCar);

// CREATING OBJS:
    // let myObj = new MyClass();
let car1 = new ToyotaCar();
console.log(car1);
console.log(car1.start());
console.log(car1.stop());

let car2 = new ToyotaCar();
console.log(car2);
console.log(car2.start());
console.log(car2.stop());

car2.brand("lexus -> Abu's fvt car.")
console.log(car2.brand);    // will give all definetion
console.log(car2);




// CONSTRUCTER:
    // USED TO INITIALIZE AN OBJECT, EG SETTING SOME PROPERTIES AT TIME OF CREATION
    // auto called/invokw by "new"
    // if their is no constructer the js will create by itself

//class ToyotaCar {
//    constructor(brand) {
//        this.brandName=brand;
//        console.log("creting an object of", brand);
//    }
//    start() {
//        console.log("started");
//    }
//
//    stop() {
//        console.log("stoped");
//    }
//
//}
//
//let car1 = new ToyotaCar("lexus");  //creting an object of lexus
//console.log(car1);
//let car2 = new ToyotaCar("fortuner");   //creting an object of fortuner
//console.log(car2);
//// as the object created the constructer is called
//// type of an obj will be class name



//INHERITANCE:
    //3) INHERITANCE:
//         FROM  ONE GENERATION OF CLASS WE PASS SOMETHING TO NEXT GENERATION OF CLASS:
//             CLASS PARRENT -------------> CHILD\NEW CLASS
//          WHEN ONE CLASS(child \ derived) DERIVES THE PROPERTIES(attributes) & METHODS OF ANOTHER CLASS(parent \ base)
// FOR INHERITANCXE WE USE A KW CALLED "EXTENDS"

//class ToyotaCar {
//    constructor(brand) {
//        this.brandName=brand;
//        console.log("creting an object of", brand);
//    }
//    start() {
//        console.log("started");
//    }
//
//    stop() {
//        console.log("stoped");
//    }
//
//}
//
//class ChildToyota extends ToyotaCar {
//
//}
//
//let childcar = new ChildToyota();   // creting an object of undefined  => undefined is for we didn't pass brand name
//console.log(childcar.start())


// multiple classes can inherite properties tec from same class
// if we have same function in parent and in chiled class then the chiled func will invoke and the phenomenon is called method overridding[cover the method of parent class]{the chiled obj method overrides the parent class mtd)




//  SUPER KW:
    // it is used to call the constructer of its parent class to acces the parent's properties and methods.


//class ToyotaCar {
//    constructor(brand) {
//        this.brandName=brand;
//        console.log("creting an object of", brand);
//    }
//    start() {
//        console.log("started");
//    }
//
//    stop() {
//        console.log("stoped");
//    }
//
//}
//
//class ChildToyota extends ToyotaCar {
//    constructor(brand) {
//        this.brandName=brand;
//        console.log("creting an object of", brand);
//    }
//}
//let childcar = new ChildToyota("suzuki");
// if we run the above code:->    Uncaught ReferenceError: Must call super constructor in derived class before accessing 'this' or returning from derived constructor
//    at new ChildToyota

// chiled class -> derived class

// the above error says that if we are creating a constructor in our derived classs it should first call the parent construvcter by using the super

class ToyotaCar {
    constructor(brand) {
        console.log("dady is first");    //to find which constructer was called first
        this.brandName=brand;
        console.log("creting an object of", brand);
    }
    start() {
        console.log("started");
    }

    stop() {
        console.log("stoped");
    }

}

class ChildToyota extends ToyotaCar {
    constructor(brand) {
        console.log("chiled is first"); ////to find which constructer was called first
        super(brand); // to invoke super class constructer  // inherite dat/info/vars/attr (from chiled init's peram the brand will go to the super which will send it to the parent's init)
        this.brandName=brand;
        console.log("creting an object of", brand);
        console.log("exit from chiled");    //to find which constructer was called first
    }
}
let childcar = new ChildToyota("suzuki");   // creting an object of suzuki
//to find which constructer was called first
        // sequence:
                // 1.chiled is first  -> as we created obj
                // 2. dady is first  -> by super() and completed its work and come back to chiled constructer
                // 3. work inside the child constructer -> after competion
                // 4. exit from chiled


//we can also inherite dat/info/vars/attr from parent to chiled using super, we just need to set the perameter(in initializer if parent) name inside the super i.e super(brand) and then we can pass the argument while creating an obj to send to the super class constructer
// similarly for methods : super.method()
//to acces the methods and propertiees of super class we use super

// we can do all stuff we do by classes and obj by func but its a way of better programming to avoid repetetion

















//{
//ERROR HANDELING:
    //
let a = 5;
let b= 6;
//console.log(a+b);
//console.log(a+b);
//console.log(a+b);
//console.log(a+.b);
//console.log(a.c); // we make mistake here as c not defined // stops the xecutionof the remaining correct code
//console.log(.+b);
//console.log.a+b);
//console.log(a+b);
//console.log(a+b);
//console.log(a+b);


//to hande:
    // try-catch blocks
//        try {
    //        [normal code]
//         }catch(err) {            // err is error obj
//            handle here
//         }
//so the above code:
try {
    console.log(a+b);
    console.log(a+b);
    console.log(a+b);
    console.log(a+b);
    console.log(a+c);
    console.log(a+b);
    console.log(a+b);
    console.log(a+b);
    console.log(a+b);
    console.log(a+b);
}catch(err) {
    console.log(err);
}
// the above code will show erroe but also will stop exe, to sove,
console.log(a+b);
    console.log(a+b);
    console.log(a+b);
    console.log(a+b);
    try {                         // only apply where u can think of error
    console.log(a+c);
    }catch (err) {console.log(err);}
    console.log(a+b);
    console.log(a+b);
    console.log(a+b);
    console.log(a+b);
    console.log(a+b);
//}








w]swplwpwp pqa











