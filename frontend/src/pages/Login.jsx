import { useState } from "react";
import { useNavigate } from "react-router-dom";

import api from "../services/api";


function Login() {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);


  const handleSubmit = async (event) => {
    event.preventDefault();

    setError("");
    setLoading(true);

    try {
      console.log("Attempting login...");
      console.log("Email:", email);

      const response = await api.post(
        "/api/auth/login",
        {
          email: email.trim(),
          password: password,
        }
      );

      console.log("Login response:", response.data);

      const token = response.data.access_token;

      if (!token) {
        throw new Error("No access token received");
      }

      localStorage.setItem(
        "access_token",
        token
      );

      navigate("/dashboard");

    } catch (err) {
      console.error("Login error:", err);

      if (err.response) {
        console.error(
          "Status:",
          err.response.status
        );

        console.error(
          "Response:",
          err.response.data
        );

        setError(
          err.response.data?.detail ||
          "Login failed."
        );

      } else if (err.request) {
        console.error(
          "No response received from backend."
        );

        setError(
          "Unable to connect to the backend."
        );

      } else {
        setError(
          err.message ||
          "Login failed."
        );
      }

    } finally {
      setLoading(false);
    }
  };


  return (
    <div className="page">

      <div className="card">

        <h1>
          Cloud-Native DevOps Platform
        </h1>

        <h2>
          Login
        </h2>

        <form onSubmit={handleSubmit}>

          <label>
            Email
          </label>

          <input
            type="email"
            value={email}
            onChange={(event) =>
              setEmail(event.target.value)
            }
            placeholder="Enter your email"
            required
          />


          <label>
            Password
          </label>

          <input
            type="password"
            value={password}
            onChange={(event) =>
              setPassword(event.target.value)
            }
            placeholder="Enter your password"
            required
          />


          {error && (
            <p className="error">
              {error}
            </p>
          )}


          <button
            type="submit"
            disabled={loading}
          >
            {loading
              ? "Logging in..."
              : "Login"}
          </button>

        </form>

      </div>

    </div>
  );
}


export default Login;