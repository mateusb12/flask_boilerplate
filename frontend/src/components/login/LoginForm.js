import React, { useState } from "react";
import './LoginForm.css';
import {useService} from "../../api/axios";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);

  const { usePost } = useService();
  const { mutate: loginUser } = usePost("login", "/auth/login");

  const handleLogin = (e) => {
    e.preventDefault();
    setError(null);

    const loginData = {
      login: username,
      password: password,
    };

    loginUser(loginData, {
      onSuccess: (response) => {
        alert(`Hello, ${response.data.username}! You have successfully logged in.`);
        // You can also save the access_token if needed
        console.log(response.data.tokens.access_token);
      },
      onError: (err) => {
        setError("Login failed. Please check your credentials.");
      },
    });
  };

  return (
    <div className="login-container">
      <h1>Hello World - Login</h1>
      <form onSubmit={handleLogin} className="login-form">
        <div className="form-group">
          <label htmlFor="username">Username:</label>
          <input
            id="username"
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="password">Password:</label>
          <input
            id="password"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        {error && <p className="error-message">{error}</p>}
        <button type="submit">Login</button>
      </form>
    </div>
  );
}

export default Login;