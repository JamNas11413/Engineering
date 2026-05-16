// Asynchronous JS and APIs:
    // 

// upto now we were storing our data in arrays and objects but apis enables us acces data else where on internet
// apis are bridge b\w frontend and backend


// API:
    // application programming interface 
    // an api is a tool that helps connect your program with someone elses program.
    // waiter is anologist to api, we don't needa no whats happening in ketchen

    // egs:
        // getting data from server
            // the server host an api exposed endpoints we can access for getting data from the server
            // note that the server doesn't give us access to everything, just the things they want us to have 

        // PRE WRITTEN CODE THAT HELP US DO COOL STUFF
            // DOM api(.getEleById)
            // array methods api (.filters, .map)
            // localStorage
            // 3rd party package

        // kind of blackbox -> we don't know whats happening but we do know what will be return
        // for open source we go to github and see how things are happening 
// helps us getting data from a server i.e map API ot just tools that helps us do cool stuff i.e saving data to localStorage



// REQUEST AND RESPONCE CYCLE:
    // REQUEST:  
        // WHENEVER A DEVICE OR CLIENTS ASK FOR SOME RESOURCE i.e data, image, html page, uthentication token, and if i am on youtube then i might have a json array of suggested videos and if  clicked on one of the video then it will request for the video stream  etc
        // unless your server is in the same device or computer as the client which does happens in dev tasks, then it must requires some sort of internet connection it have to send that request out to the server, outside of its own little server or device

    // RESPONCE:
        // REPLY TO THE REQUEST
        // WHEN A SERVER RECIEVE THAT REQUEST IT PROCESS IT AND SEND A RESPONCE BACK
        // if everything goes right the responce will consist of the resource asked for i.e html page or json data
        // and else case an error will be sended
    
    
    // it id happen when we type a url for the 1st time client(browser) asked for the index.html from the server of the website and if everything being ok sever will respond with the resource and with a status code of 200 and status msg is OK
    // if that html file have a request to google fonts then browser will request to the font server and then get responce back 
    // the server might tio interfare with dataBase for the request's data

    // status code(server responce code):         messages                  boolen
            // 3 digits
        // 200 - 299                                OK                      true
        // 403                                      forbiden                false
        // 500                                      internal server error   false
            // anything in range of 500 will be internal server error 
        // 404                                      not found               false



// JSON: ---. lang of data on the web 
    // javaScript object notation b\c it looks like a js objs major diff in them is that in json keys will be in double quotes and values can be any   ordinary js value like numbers (not in double quotes), true etc
    // 
    // json is also valid as a plane text i.e "hi"/true ===> valid json
    // i can chech if it is valid json or not in websites like jsonlint.com ===> imp b\c if i wanna check if it is correct what i wrote


    // i can check for the request and responce that i have made  from a web in network tab there are also alots of filters like fetch/xhr (xhr---> ajax responce which usually return json as in responce )



// URLs AND ENDPOINTs:
    // when we request to an api we use that api's url "the url is essentially an address where your desire resource is located "
    // MAKE UP of URLs:
        // 2 portion:
            // the base url i.e https://scrimba.com/api {fictional}
            // end point specific resource that i wanna get from the API SERVER i.e: /cources, /cources/enrolled/names, /resources/tests?test=typescript (query at end for a test in ts)

    // the responce will gwenrally looks like json but if not then there are some browser plugins which will convert it to  more readable stuff
    // if u prefer so u can search for json formatter browser plugins --> usefull for reading the data




// FETCHING WITH .then()
//     2 ways to write requests 
//         fetch().then()
//             search for dog APi
fetch('https://dog.ceo/api/breeds/image/random')   // full url so both base and endpoint
    .then(responce => responce.json()) // method which will pickup what we got from fetch and make it us availible to us in a param in a callback func  by convention we call the paarm responce

// This initiates a network request to the URL provided.
    // fetch returns a Promise. This means the code doesn't freeze while waiting for the internet to reply; instead, it promises to let you know when the data arrives.
// the json method take the responce and convert it to js object so we can use it our js code


// APIs don't always gives us json data if you  wandering u can read the docs of the apis to know what will it return


// TO SEE WHAT WE GOT IN THERE (TYPE)
    // .then(data => console.log(data)) // data will be holding what we get back from calling the jsom method above on the responce

// to actually do something 
    .then(data => {
        const imageElement = document.createElement("img")
        imageElement.src = data.message
        imageElement.alt = "random dog picture"
        document.getElementById('img-container').appendChild(imageElement)
    })






// PROMISES:
    // promises.js --> file



// HANDLING REJECTED PROMISES:
    //
// fetch('urlofAPi')   
//     .then(responce => responce.json())
//     // ERROR OCURED AND SAYS UNHANDELED PROMISE   in this case if we wanna show a msg etc we can do ...
//     .catch(err => console.log("an error occured babby!"))
//     // it will just log it to console but we can do other stuffs i.e
//     // update the dom warn the user
//     // acces an alternative api
//     // throw new Error("no code will be exe  after the throw")

// // we can also  chain a finally --> it Also take a callback func without pRAM  -> EXE AT END OF THE PROCES WHETER THE PROMISE  RESOLVED OR REJECTED
//         // SO NOTHING TO DO WITH ERROR HANDELLLING 


// try { 
//     const res = fetch('urlofAPi')
//     const data = await responce.json()
// } catch(err) {
//     // the code to exe on error(err)
//     console.log(err)
// }
//  finally {
//     // exe at end of tyhe operation 
//     console.log("operation completed")
// }





// responce.ok
    // ok property on the responce obj
    // another way handeling error
    // it holds a boolen and indicate wheter the http request was seuccesful


    // use for cheaking the responce status
        // i.e an error in the api or endpoint etc

// try { 
//     const res = fetch('urlofAPi')
//     // console.log(responce.ok)
//     // for handelling error
//     if (!responce.ok) {
//         throw new Error("error")
//     }
//     const data = await responce.json()
// } catch(err) {
// }
//  finally {
//     // exe at end of tyhe operation 
//     console.log("operation completed")
// }




// try-catch:
    // catches exception and errors that occur during the exe of the code, including network errors and other unexpected issues

// responce.ok:
    // checks the succes of the http responce status, which might not throw an error but still indicates a failure


// breaking api => catch
// breaking endpoint => responce.ok




// promise constructer


// const promise = new Promise((resolve, reject) => {
//     const sucess = Math.random() 
//     if  (sucess > 0.5) {
//         resolve("operation succesfull")
//     } 
//     else {
//         reject("operation failed!")
//     }
// })

// promise.then(result => console.log(result))
// promise.catch(err => console.log(err))


// setTimeout(() => {
//     console.log("exe is not stopp4ed")
// },2000)

// ("operation succesfull")
//     } 
//     else {
//         reject("operation failed!")
//     }
// })

// promise.then(result => console.log(result))
// promise.catch(err => console.log(err))


// setTimeout(() => {
//     console.log("exe is not stopp4ed")
// },2000)























// astync 3 cats

// callback
// callback hell
// promises
const promise = new Promise((resolve, reject) => {
    const sucess = Math.random() 
    if  (sucess > 0.5) {
        resolve("operation succesfull")
    } 
    else {
        reject("operation failed!")
    }
})

promise.then(result => console.log(result)) // will take a callback    // .tyhen only do the succes case 
promise.catch(err => console.log(err))  // for the fail case we will use the catch

// ===

promise 
    .then(result => console.log(result))
    .then(err => console.log(err))




fetch('urlofAPi')   
    .then(responce => responce.json())
    .catch(err => console.log("an error occured babby!"))

    // fetch return a proise and all promise pretty much follow thw same pattern


// async await
let asyncc = async() => {
    await console.log("i am async!")
}

// try catch inside async await










// methods