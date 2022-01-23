import React,{useState} from 'react';
import Axios from 'axios'
import { useNavigate } from 'react-router-dom';
import { addCustomer } from '../components/APIcalls';

const Create = () => {

  const navigate = useNavigate()



  const [customer, setCustomer] = useState({
    name:"",
    email:"",
    primary_mobile:"",
    // cust_photo:"",
  });
  const {name,email,primary_mobile,cust_photo} = customer;



  const onSubmit = (e) => {
    e.preventDefault();
    setCustomer({...customer})
    addCustomer(customer).then(data=>{
      if(data.error){
        setCustomer({...customer})
      }

      else{
        setCustomer({
          ...customer,
          name:"",
          email:"",
          primary_mobile:"",
          // cust_photo:"",
        })
      }
    })
    
    
    
   
    console.log(customer)
    
  }

  const handleChange = name => event => {
    const value = name === "cust_photo" ? event.target.files[0] : event.target.value; 
    setCustomer({...customer, [name]:value});
  };

  

  return (
    <div className='mt-5'>
    <form action=""
    onSubmit={e => onSubmit(e)}
    >

    <label htmlFor=""> Name:  </label>
    <input 
    type="text" 
    name="name" 
    id="" 
    value={name} 
    onChange={handleChange('name')}
    required

    />
    <label htmlFor=""> Email:  </label>
    <input 
    type="email" 
    name="email" 
    id="" 
    value={email}
    onChange={ handleChange('email')}
    />
    <label htmlFor=""> Phone:  </label>
    <input 
    type="tel" 
    name="primary_mobile" 
    id="" 
    value={primary_mobile}
    onChange={handleChange('primary_mobile')}

    />
   {/*<label htmlFor=""> Customer Photo:  
    <input 
    type="file" 
    name="cust_photo" 
    accept="image"
    id="" 

    onChange={handleChange('cust_photo')}
  />
  </label> */}
    <button   type="submit">Submit</button>
    </form>
    
    </div>

  );
};

export default Create;
