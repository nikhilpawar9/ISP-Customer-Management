export const addCustomer = (customer) => {





    return fetch("http://127.0.0.1:8000/customers/",{
      method: "POST",
      headers: {
        accept: 'application/json',
        'Content-Type': 'application/json'
      },
      body:JSON.stringify({...customer}),
    })
      .then(response => {
        return response.json();
      })
      .catch(err => console.log(err));
  };