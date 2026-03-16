const API_BASE_URL = "http://localhost:8000";

export const api = {
  async getTasks() {
    const response = await fetch(`${API_BASE_URL}/tasks`);
    if (!response.ok) {
      throw new Error("Failed to fetch tasks");
    }
    return response.json();
  },

  async createTask(taskData) {
    const response = await fetch(`${API_BASE_URL}/tasks`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(taskData),
    });

    if (!response.ok) {
      throw new Error("Failed to create task");
    }
    return response.json();
  },

  async markTaskDone(taskId) {
    const response = await fetch(`${API_BASE_URL}/tasks/${taskId}/done`, {
      method: "PATCH",
    });

    if (!response.ok) {
      throw new Error("Failed to update task");
    }
    return response.json();
  },
};
