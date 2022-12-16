import React ,{useState, useEffect} from 'react'

import FileCard from './filecard'
import FileItem from './fileitem'
import '../styles/FilesView.css'
import AuthService from '../Services/AuthService'
import axios from 'axios';

function getFiles(){
    let url = 'http://localhost:8000/api/utility/get_entities?folder=0' //shared files api link
    const [files, setFiles] = useState([])
    const token = localStorage.getItem("user")

    axios.get(url,{
        headers: { Authorization: `Token ${token}` }
    })
    .then(response=>{
        setFiles(response.data.Folder)
    })
    // console.log(files)
    return files
}

const ShowSharedFiles = () => {
    
    const files = getFiles()
    useEffect(() => {
        //get file data - id, data; data - title, timestamp, fileurl, filesize
        // setFiles()
        const token = AuthService.getCurrUser()
        console.log(token)
    },[])

    // console.log(files)
    return (
        <div className='showfiles'>
            <div className='showfiles_row'>
                <h2>shared with me</h2>
                {
                    files.slice(0,5).map((id) => (
                        <FileCard name={id.name}/>
                    ))
                }
            </div>
            <div className='showfiles_titles'>
                <div className='showfiles_titles--left'>
                    <p>Name</p>
                </div>
                <div className='showfiles_titles--right'>
                    <p>Last modified</p>
                    <p>File size</p>
                </div>
            </div>
            {/* <div> */}
                {
                    files.map((id,index) => (
                        <FileItem id={id} caption={id.name} timestamp={id.updated}/>
                    ))
                }
            {/* </div> */}
        </div>
    )
}
export default ShowSharedFiles