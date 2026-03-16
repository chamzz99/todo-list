import React from "react";
import "../styles/TaskCard.css";

export default function TaskCard({ task, onMarkDone }) {
  return (
    <div className="task-card">
      <div className="task-content">
        <h3 className="task-title">{task.title}</h3>
        {task.description && <p className="task-desc">{task.description}</p>}
      </div>
      <button
        className="done-btn"
        onClick={() => onMarkDone(task.id)}
        aria-label={`Mark ${task.title} as done`}
      >
        Done
      </button>
    </div>
  );
}
