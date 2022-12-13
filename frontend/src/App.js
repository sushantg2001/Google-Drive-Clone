import React from 'react';
import axios from 'axios';

import './App.css';
// import FileCard from './Components/filecard';
import ShowFiles from './Components/showfiles';
import SideBar from './Components/SideBar';
import SideIcons from './Components/SideIcons';
import Header from './Components/Header'
import Login from './Components/login';

class App extends React.Component{
  state = {
    details: []
  }
  componentDidMount(){
    let data;

    axios.get('http://localhost:8000')
    .then(res=>{
      data = res.data;
      this.setState({
        details: data
      })
      // console.log('hi')
      // console.log(data)
    })
    .catch(err => {})
  }

  render(){
    return (
      <Login/>
      // <div className="App">
      //   <Header/>
      //   <div className='app_main'>
      //     <SideBar/>
      //     <ShowFiles/>
      //     <SideIcons/>
      //   </div>
      // </div>
    );
  }
}

export default App;
