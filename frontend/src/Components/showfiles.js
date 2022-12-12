import React ,{useState, useEffect} from 'react'

import FileCard from './filecard'
import FileItem from './fileitem'
import '../styles/FilesView.css'

const ShowFiles = () => {
    // const [files, setFiles] = useState([])
    const files = [
        {
            id:1,
            item:{
                timestamp: Date.now(),
                caption:"file1",
                fileURL:"",
                size:2
            }
        },
        {
            item:{
                timestamp: Date.now(),
                caption:"file2",
                fileURL:"",
                size:2
            }
        }
    ]
    useEffect(() => {
        //get file data - id, data; data - title, timestamp, fileurl, filesize
        // setFiles()
    },[])

    console.log(files)
    return (
        <div className='showfiles'>
            <div className='showfiles_row'>
                {
                    files.slice(0,5).map(({id,item}) => (
                        <FileCard name={item.caption}/>
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
                    files.map(({id, item}) => (
                        <FileItem id={id} caption={item.caption} timestamp={item.timestamp} fileURL={item.fileURL} size={item.size}/>
                    ))
                }
            {/* </div> */}
        </div>
    )
}
export default ShowFiles