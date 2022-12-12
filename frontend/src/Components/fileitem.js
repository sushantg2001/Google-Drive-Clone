import React from "react";
import InsertDriveFileIcon from '@material-ui/icons/InsertDriveFile'
import '../styles/FileItem.css'

const monthNames = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

const FileItem = ({id,caption,timestamp,fileURL,size}) => {
    const date = new Date(timestamp)
    const fileDate = `${date.getFullYear()} ${monthNames[date.getMonth()]} ${date.getDate()}`

    return (
        <div className="fileItem">
            <a href={fileURL} target="_blank" download>
                <div className="fileItem--left">
                    <InsertDriveFileIcon/>
                    <p>{caption}</p>
                </div>
                <div className="fileItem--right">
                    <p>{fileDate}</p>
                    <p>{size}</p>
                </div>
            </a>
        </div>
    )
}
export default FileItem