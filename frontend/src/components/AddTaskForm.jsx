import React, { useState } from "react";
import "../styles/AddTaskForm.css";

export default function AddTaskForm({ onAddTask }) {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    //Removing Empty..
    if (!title.trim()) return;
    if (!description.trim()) return;

    onAddTask({ title, description });

    // Clearing.....
    setTitle("");
    setDescription("");
  };

  return (
    <div className="add-task-sidebar">
      <h2>Add a Task</h2>
      <form onSubmit={handleSubmit} className="add-task-form">
        <div className="input-group">
          <label htmlFor="title">Title</label>
          <input
            id="title"
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
            placeholder="e.g., Buy books"
          />
        </div>

        <div className="input-group">
          <label htmlFor="description">Description</label>
          <textarea
            id="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            rows="4"
            placeholder="Add details here..."
          />
        </div>

        <button type="submit" className="add-btn">
          Add
        </button>
      </form>
    </div>
  );
}
