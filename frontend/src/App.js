import React from 'react';
import axios from 'axios';

import './App.css';
// import FileCard from './Components/filecard';
import ShowFiles from './Components/showfiles';
import SideBar from './Components/SideBar';
import SideIcons from './Components/SideIcons';
import Header from './Components/Header'
import Login from './Components/login';
import {BrowserRouter as Router,Route} from 'react-router-dom'
import PrivateRoute from './Components/privateroute'
import AuthService from './Services/AuthService';

const Drive = () =>{
  return (
    <div className="App">
        <Header/>
        <div className='app_main'>
          <SideBar/>
          <ShowFiles/>
          <SideIcons/>
        </div>
      </div>
  )
}
class App extends React.Component{
  state = {
    details: []
  }
  
  componentDidMount(){
    let data;
  }

  render(){
    return (
      <div>
        {AuthService.getCurrUser() ? <Drive/> : <Login/>}
        {/* <Drive/> */}
        {/* <Router>
          <Route path="/login" component={Login}/>
          <PrivateRoute path="/" component={drive}/>
        </Router> */}
      </div>
      
    );
  }
}

export default App;
