import React, { useState, useEffect } from "react";
import AddTaskForm from "./components/AddTaskForm";
import TaskCard from "./components/TaskCard";
import { api } from "./services/api";
import "./App.css";

function App() {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);

  //fetch tasks from the FastAPI backend
  const loadTasks = async () => {
    try {
      const data = await api.getTasks();
      setTasks(data);
    } catch (error) {
      console.error("Failed to load tasks:", error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadTasks();
  }, []);

  const handleAddTask = async (taskData) => {
    try {
      await api.createTask(taskData);
      loadTasks();
    } catch (error) {
      console.error("Failed to create task:", error);
    }
  };

  const handleMarkDone = async (taskId) => {
    try {
      await api.markTaskDone(taskId);
      loadTasks();
    } catch (error) {
      console.error("Failed to mark task as done:", error);
    }
  };

  return (
    <div className="app-container">
      <div className="left-panel">
        <AddTaskForm onAddTask={handleAddTask} />
      </div>

      <div className="right-panel">
        {loading ? (
          <p className="status-message">Loading tasks...</p>
        ) : tasks.length === 0 ? (
          <p className="status-message">
            No pending tasks. You're all caught up!
          </p>
        ) : (
          <div className="task-list">
            {tasks.map((task) => (
              <TaskCard key={task.id} task={task} onMarkDone={handleMarkDone} />
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
