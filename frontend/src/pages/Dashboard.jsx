import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import api from "../services/api";

function Dashboard() {
  const navigate = useNavigate();

  const [tasks, setTasks] = useState([]);
  const [error, setError] = useState("");

  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");

  const loadTasks = async () => {
    try {
      const response = await api.get("/api/tasks/");
      setTasks(response.data);
    } catch (err) {
      if (err.response?.status === 401) {
        localStorage.removeItem("access_token");
        navigate("/");
        return;
      }

      setError("Unable to load tasks.");
    }
  };

  useEffect(() => {
    loadTasks();
  }, []);

  const createTask = async (event) => {
    event.preventDefault();

    try {
      await api.post("/api/tasks/", {
        title,
        description,
      });

      setTitle("");
      setDescription("");

      await loadTasks();
    } catch (err) {
      setError(
        err.response?.data?.detail ||
        "Unable to create task."
      );
    }
  };

  const deleteTask = async (taskId) => {
    try {
      await api.delete(`/api/tasks/${taskId}`);
      await loadTasks();
    } catch (err) {
      setError("Unable to delete task.");
    }
  };

  const logout = () => {
    localStorage.removeItem("access_token");
    navigate("/");
  };

  return (
    <div className="dashboard">
      <header>
        <h1>Task Dashboard</h1>

        <button onClick={logout}>
          Logout
        </button>
      </header>

      <section className="card">
        <h2>Create Task</h2>

        <form onSubmit={createTask}>
          <input
            type="text"
            placeholder="Task title"
            value={title}
            onChange={(event) => setTitle(event.target.value)}
            required
          />

          <textarea
            placeholder="Task description"
            value={description}
            onChange={(event) =>
              setDescription(event.target.value)
            }
          />

          <button type="submit">
            Create Task
          </button>
        </form>
      </section>

      {error && (
        <p className="error">
          {error}
        </p>
      )}

      <section className="card">
        <h2>My Tasks</h2>

        {tasks.length === 0 ? (
          <p>No tasks found.</p>
        ) : (
          tasks.map((task) => (
            <div
              className="task"
              key={task.id}
            >
              <div>
                <h3>{task.title}</h3>

                <p>
                  {task.description || "No description"}
                </p>

                <small>
                  Status: {task.status}
                </small>
              </div>

              <button
                onClick={() => deleteTask(task.id)}
              >
                Delete
              </button>
            </div>
          ))
        )}
      </section>
    </div>
  );
}

export default Dashboard;