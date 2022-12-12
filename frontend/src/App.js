import './App.css';
// import FileCard from './Components/filecard';
import ShowFiles from './Components/showfiles';
import SideBar from './Components/SideBar';
import SideIcons from './Components/SideIcons';
import Header from './Components/Header'

function App() {
  return (
    <div className="App">
      <Header/>
      <div className='app_main'>
        <SideBar/>
        <ShowFiles/>
        <SideIcons/>
      </div>
    </div>
  );
}

export default App;
