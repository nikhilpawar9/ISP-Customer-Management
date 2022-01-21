import React,{useState, useEffect} from 'react'
import Axios from 'axios'
import Tables from './components/Tables';
import Paginate from './components/Paginate';
import "./App.css"
import { BsSearch } from "react-icons/bs";
import { Button } from '@mui/material';
import { Link } from 'react-router-dom';
import deleteCustomer from './components/APIcalls'



const App = () => {



  const [customers, setCustomers] = useState([]);
  const [searchCustomer, setSearchCustomer] = useState("")  // For Searching
  const [arrrangement, setArrangement] = useState("Ascending")    // For Sorting


  const [currentPage, setCurrentPage] = useState(1)         //for pages
  const [customersperPage, setCustomersperPage] = useState(10)        //10 items in table on single page



  const lastcustomerIndex = currentPage * customersperPage;
  const firstcustomerIndex = lastcustomerIndex-customersperPage;
  const currentCustomer = customers.slice(firstcustomerIndex,lastcustomerIndex)

  const deleteCust = async id => {
    await Axios.delete(`http://127.0.0.1:8000/customers/${id}/`).then(res => {
      const cust = customers.filter(customer => id !== customer.id)
      setCustomers(cust)
      
  })
  }




  const Sorting = (tablehead) =>{
    if(arrrangement == "Ascending"){
      const sorted = [...customers].sort((a,b)=>
      (a[tablehead] >b[tablehead]) ? 1 : -1
      )

      setCustomers(sorted);
      setArrangement("Descending")

    }
    if(arrrangement == "Descending"){
      const sorted = [...customers].sort((a,b)=>
      (a[tablehead] <b[tablehead])  ? 1 : -1
      )

      setCustomers(sorted);
      setArrangement("Ascending")

    }
    
}

const changePage = (number) => setCurrentPage(number)

  const fetchCustomers = async () => {
    
      const {data} = await Axios.get('http://127.0.0.1:8000/customers/')

      console.log(data);

      setCustomers(data);
    
}

const previousPage = () => setCurrentPage(currentPage-1);
const nextPage = () => setCurrentPage(currentPage+1);


useEffect(() => {
  fetchCustomers()
}, [])





  return (
    <div>
    
    <div className="form-search mt-3">
      <label htmlFor="">Search</label>
      <input type="search" name="" placeholder='Search' id="" 
      onChange={(e) =>{setSearchCustomer(e.target.value)}} />
      <div className="icon">
      <BsSearch size={22}/>
      </div>
      
      <Link to={`/customers/create/`} target="_blank" className='page-link' >
      <Button>Add Customer</Button>
     </Link>
    
    </div>
  
      <Tables 
        customers={currentCustomer} 
        searchCustomer={searchCustomer} 
        Sorting={Sorting}
        deleteCust={deleteCust}
      />
      <Paginate 
      customersperPage={customersperPage} 
        customersCount={customers.length} 
        changePage={changePage}  
        previousPage={previousPage} 
        nextPage={nextPage} 
      />

    </div>
  )
}

export default App
