import React, { useState, useEffect } from "react";
import Axios from "axios";
import { useParams, useNavigate } from "react-router-dom";
import { BsFillArrowLeftSquareFill } from "react-icons/bs";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemText from "@mui/material/ListItemText";
import Divider from "@mui/material/Divider";

import "./details.css";

const Details = ({ match }) => {
  const [details, setDetails] = useState([]);

  const { id } = useParams();

  const fetchitems = async () => {
    const { data } = await Axios.get(`http://127.0.0.1:8000/customers/${id}/`);
    console.log(data[id]);

    setDetails(data);
  };

  useEffect(() => {
    fetchitems();
  }, []);

  const navigate = useNavigate();

  const style = {
    width: "100%",
    maxWidth: 360,
    bgcolor: "background.paper",
  };

  return (
    <div className="details">
      <div className="btn">
        <BsFillArrowLeftSquareFill
          onClick={() => navigate("/customers")}
          style={{ cursor: "pointer" }}
          size={50}
        />
      </div>

      <div className="d-flex tablem container justify-content-center">
        <List
          sx={style}
          className="ourList"
          component="nav"
          aria-label="mailbox folders"
        >
          <ListItem button>
            <ListItemText secondary={details.name} primary="Name" />
          </ListItem>
          <Divider light />
          <ListItem button divider>
            <ListItemText secondary={details.email} primary="Email" />
          </ListItem>
          <Divider light />
          <ListItem button>
            <ListItemText
              secondary={details.primary_mobile}
              primary="Primary Mobile"
            />
          </ListItem>
          <Divider light />
          <ListItem button>
            <ListItemText
              secondary={details.alternate_mobile}
              primary="Alternate Mobile"
            />
          </ListItem>
          <Divider light />
          <ListItem button>
            <ListItemText secondary={details.address} primary="Address" />
          </ListItem>
          <Divider light />
          <ListItem button>
            <ListItemText secondary={details.address} primary="Address" />
            <img src={details.cust_photo} alt="sd" />
            <img src={details.cust_photo} alt="" />

          </ListItem>
          <Divider light />
          <ListItem button>
            <ListItemText secondary={details.city} primary="City" />
          </ListItem>
          <Divider light />
          <ListItem button>
            <ListItemText secondary={details.state} primary="State" />
          </ListItem>
          <Divider light />
          <ListItem button>
            <ListItemText secondary={details.zipcode} primary="Zip" />
          </ListItem>
          <Divider light />
          <ListItem button>
            <ListItemText secondary={details.connection_type} primary="Connection Type" />
          </ListItem>
          <Divider light />
          <ListItem button>
            <ListItemText secondary={details.state} primary="State" />
          </ListItem>
          <Divider light />
          <ListItem button>
            <ListItemText secondary={details.state} primary="State" />
          </ListItem>
          <Divider light />
          <ListItem button>
            <ListItemText secondary={details.state} primary="State" />
          </ListItem>
          <Divider light />
          <ListItem button>
            <ListItemText secondary={details.state} primary="State" />
          </ListItem>
        </List>
      </div>
    </div>
  );
};

export default Details;
