import Axios from 'axios'

const url = 'http://127.0.0.1:8000/customers/'

export const addUserDetails = async(customers) => {
    return await Axios.post(url,customers)
}


// export default class APIcalls {




//     static updateCustomer(id , body){
//         return fetch(`http://127.0.0.1:8000/customers/${id}/`,{
//             'method' : 'PUT',
//             headers : {
//                 'Content-Type' :'application/json',
//             },
//             body:JSON.stringify(body)
//         })
//         .then(res => res.json())

//     }

//     static addCustomer(body){
//         return fetch(`http://127.0.0.1:8000/customers/`,{
//             'method' : 'POST',
//             headers : {
//                 'Content-Type': 'application/json',
//             },
//             body : JSON.stringify(body)
//         })
//         .then(res => res.json())
//     }


//     static deleteCustomer(id ){
//         return fetch(`http://127.0.0.1:8000/customers/${id}/`,{
//             'method' : 'DELETE',
//             headers : {
//                 'Content-Type' :'application/json',
//             }
       
//         })
      

//     }
// }
