import React, { useState } from "react";
import ReactDOM from "react-dom";
import axios from 'axios';
import Login from "../Components/login";

function login(username,password) {
    let url = 'http://localhost:8000/auth-token/'
    axios.post(url,{
        "username":username,
        "password": password
    })
    .then(response=>{
        console.log(response.data.token)
        localStorage.setItem("user",response.data.token)
    })
    .catch(err=>console.log(err))
}

function logout(){
    // localStorage.removeItem("user")
    // location.reload()
}

function getCurrUser(){
    const token = localStorage.getItem("user")
    if (token === null) {
        return false
    }
    return token
}
function getUserName(){
    const token = getCurrUser()
    const url = "http://localhost:8000/api/users/me/"
    console.log(token)

    const config = {
        headers: { Authorization: `Token ${token}` }
    };

    axios.get(url,null,config)
    .then(response=>{
        console.log(response)
        // return response
    }).catch(err=>console.log(err))
}
function newUser(){
    //
}

const AuthService = {
    login,
    logout,
    getCurrUser,
    getUserName,
    newUser
}
export default AuthService