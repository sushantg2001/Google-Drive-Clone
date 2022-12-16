import React from 'react'
import '../styles/SideBar.css'
import ArrowRightIcon from '@material-ui/icons/ArrowRight';
import InsertDriveFileIcon from '@material-ui/icons/InsertDriveFile';
import PeopleAltIcon from '@material-ui/icons/PeopleAlt';
import NewFile from './NewFile';

const SidebarItem = ({ arrow, icon, label }) => {
    return (
        <div className='sidebarItem'>
            <div className="sidebarItem__arrow">
                {arrow && (<ArrowRightIcon />)}
            </div>
            
            <div className='sidebarItem__main'>
                {icon}
                <p>{label}</p>
            </div>
        </div>

    )
}

function SideBar(){
    return (
        <div className='sidebar'>
            <NewFile />

            <div className="sidebar__itemsContainer">
                <SidebarItem icon={(<InsertDriveFileIcon />)} label={'My Drive'} />
                <SidebarItem icon={(<PeopleAltIcon />)} label={'Shared with me'}/>
                <hr/>
            </div>

        </div>
    )
}
export default SideBar