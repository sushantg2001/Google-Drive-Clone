import axios from 'axios';
import AuthService from './AuthService';

function createFile(filename){
    const token = AuthService.getCurrUser()
    let url = 'http://localhost:8000/api/files/'
    axios.post(url,{
        "name":filename
    })
    .then(response=>{
        console.log(response)
    })
    .catch(err=>console.log(err))
}
function getWorkingDir(path,id){
    let url = 'http://localhost:8000/api/files/${id}'
}
const FileSystem = {
    createFile
}

export default FileSystem