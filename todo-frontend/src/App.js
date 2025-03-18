import React, { useState, useEffect } from "react";

const API_URL = "http://localhost:5000/tasks"; // Update if needed

function App() {
    const [tasks, setTasks] = useState([]);
    const [task, setTask] = useState("");

    useEffect(() => {
        fetchTasks();
    }, []);

    // Fetch tasks from the backend
    async function fetchTasks() {
        try {
            const response = await fetch(API_URL);
            const data = await response.json();
            setTasks(data);
        } catch (error) {
            console.error("Error fetching tasks:", error);
        }
    }

    // Add a new task
    async function addTask() {
        if (!task.trim()) return;
        try {
            await fetch(API_URL, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ title: task })
            });
            setTask("");
            fetchTasks();
        } catch (error) {
            console.error("Error adding task:", error);
        }
    }

    // Delete a task
    async function deleteTask(id) {
        try {
            await fetch(`${API_URL}/${id}`, { method: "DELETE" });
            fetchTasks();
        } catch (error) {
            console.error("Error deleting task:", error);
        }
    }

    return (
        <div style={{ textAlign: "center", fontFamily: "Arial" }}>
            <h1>To-Do List</h1>
            <input
                type="text"
                value={task}
                onChange={(e) => setTask(e.target.value)}
                placeholder="Enter a task"
            />
            <button onClick={addTask}>Add Task</button>
            <ul>
                {tasks.map((t) => (
                    <li key={t.id} style={{ marginBottom: "10px" }}>
                        {t.title}
                        <button onClick={() => deleteTask(t.id)} style={{ marginLeft: "10px" }}>❌</button>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default App;

