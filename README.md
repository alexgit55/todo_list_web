# To‑Do List Web

A lightweight **web-based To‑Do List Manager** built with **Python** and **Streamlit**. Add tasks, mark them as complete, and keep your list persisted between runs.

## Features

- Simple web UI (Streamlit)
- Add new tasks quickly
- Mark tasks as completed
- Saves tasks to a local text file for persistence

## Project Structure

- `main.py` — Streamlit app entry point
- `todoitem.py` — To‑do item model
- `todolist.py` — To‑do list logic + persistence
- `todo_list.txt` — local storage for tasks
- `requirements.txt` — Python dependencies

## Requirements

- Python 3.x
- Packages listed in `requirements.txt` (includes Streamlit)

## Setup (Windows / PyCharm-friendly)

1. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Run the App

From the project folder:
   ```bash
   streamlit run main.py
   ```

Streamlit will print a local URL (usually `http://localhost:8501`)—open it in your browser.

## Data Persistence

Tasks are stored locally in `todo_list.txt`.  
If you want a fresh start, stop the app and clear/delete that file.

## Troubleshooting

- **`streamlit` not found**: make sure your virtual environment is activated and dependencies are installed.
- **App not updating**: Streamlit auto-runs, but you can refresh the page or restart the server if needed.

## Roadmap Ideas

- Edit tasks
- Due dates / priorities
- Filter (all / active / completed)
- Persist completed tasks separately
- Export/import tasks

## License

Add a license if you plan to share publicly (e.g., MIT).