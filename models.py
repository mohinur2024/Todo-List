from database import get_connection

def add_task(title):
    with get_connection() as conn:
        conn.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
        conn.commit()

def list_tasks():
    with get_connection() as conn:
        return conn.execute("SELECT id, title, done FROM tasks").fetchall()

def mark_done(task_id):
    with get_connection() as conn:
        conn.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
        conn.commit()

def delete_task(task_id):
    with get_connection() as conn:
        conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
