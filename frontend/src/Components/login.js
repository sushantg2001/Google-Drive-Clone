import React, { useState } from "react";
import ReactDOM from "react-dom";
import axios from 'axios';
import "../styles/login.css";
import AuthService
 from "../Services/AuthService";

function Login() {
  // React States
  const [errorMessages, setErrorMessages] = useState({});
  const [isSubmitted, setIsSubmitted] = useState(false);

  const errors = {
    uname: "invalid username",
    pass: "invalid password"
  };

  const [uname, setUname] = useState("");
  const [pass, setPass] = useState("");

  const handleSubmit = async(event) => {
    //Prevent page reload
    event.preventDefault();

    AuthService.login(uname,pass)
    setIsSubmitted(true)
    // location.reload()
  };

  // Generate JSX code for error message
  const renderErrorMessage = (name) =>
    name === errorMessages.name && (
      <div className="error">{errorMessages.message}</div>
    );

  // JSX code for login form
  const renderForm = (
    <div className="form">
      <form onSubmit={handleSubmit}>
        <div className="input-container">
          <label>Username </label>
          <input type="text" name="uname" required value={uname} onChange={(e) => setUname(e.target.value)}/>
          {renderErrorMessage("uname")}
        </div>
        <div className="input-container">
          <label>Password </label>
          <input type="password" name="pass" required value={pass} onChange={(e) => setPass(e.target.value)}/>
          {renderErrorMessage("pass")}
        </div>
        <div className="button-container">
          {/* <input type="submit"/>Sign In */}
          <button type="submit" onClick={handleSubmit}>Sign In</button>
        </div>
      </form>
      Create new account <a href="">here</a>
    </div>
  );

  return (
    <div className="app">
      <div className="login-form">
        <div className="title">Drive Sign In</div>
        {renderForm}
      </div>
    </div>
  );
}

export default Login;