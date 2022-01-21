import React from 'react'
import { Link } from 'react-router-dom'


const Dashboard = () => {
    return (
        <div>
            <h1>Dashboard</h1>

            <Link to="/customers">Customers</Link>
        </div>
    )
}

export default Dashboard
