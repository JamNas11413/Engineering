// FETCH API:
    // the fetch api provides an interface for fetching (sending/recieving) resources.
    // it uses request and responce objects
    // the fetch() method is used to fetch a resource (data).



// syntax:
    // let promise = fetch(URL.option)  //fetch is async method & return promise 


    // we can search for free public api 
    // every api has some documentation in which instructyion to use is written
    // base url => start url 

const url = "linklihbjdvnjdbvjkdsnbcjdksjnbcxjdkscbnvjdskn";

let promise = fetch(url);
console.log(promice);


// we will do the above work using async await for that we have to create  func

const dataAPI = async () => {
    let responce = await fetch(url);
    console.log(responce);      // it will show  alittle delay due to a-sync prog   // responce  ehich is a promise is an object
    console.log(responce.status);
    let usableData = await responce.json();  // as it also async so we will await om it too
    console.log(usableData);
    console.log(usableData[0]); // can also
}
 // it doesn't reload the page and show info at runtime

//  if we didn't pass any option then the default option will be "get"

// it gives the responce in json formate


// terms:
    // AJAX is asynchronize JS & XML
        // in early days network request uses XML(data were come in xml formate)
    
    // JSON is js object notation
        // looks like js object{not an actual js object}
        // can also called AJAJ -> asynchronise js and json  {xmle replaced by json}
// so we get data in json formate 
// we have to convert it to js object in order to use 
// FOR THAT WE USE A METHOD CALLED json()-> an asynchronize method and return a promise 

// json() method: return a 2nd promice that resolves with the reult of parsing the responce body text as JSON. input as JSON,output is js object


// 19-25



// responce and request
    // request:
        // have some http verbs
        // mdn docs -> http request methods
    // respoce status:
        // mdn doc -> http responce status codes                                 // server side errors start with 5
// http responce header also contain detail about the reponces, such as content typeof,status codevetc {we cab see it in headers in console}