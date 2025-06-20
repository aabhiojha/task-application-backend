**Simple To-Do API**
======================

A minimal Django REST Framework–based To-Do API that supports creating, updating, deleting, and listing tasks. Designed with clean function-based views and UUIDs as primary keys.

**Tech Stack**
---------------

* **Django**: 5.2.3
* **Django REST Framework**: 3.16.0
* **Python**: 3.10+
* **Database**: SQLite (default) or PostgreSQL
* **Task IDs**: UUID

**Requirements**
---------------

Install project dependencies:

```bash
pip install -r requirements.txt
```

**Getting Started**
--------------------

1. **Clone the repository**:

```bash
git clone https://github.com/your-username/todo-api.git
cd todo-api
```

2. **Apply migrations**:

```bash
python manage.py migrate
```

3. **Run the development server**:

```bash
python manage.py runserver
```

**API Endpoints**
-----------------

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `tasks/` | List all tasks |
| POST | `tasks/` | Create a new task |
| GET | `tasks/<id>/` | Retrieve a specific task |
| PUT | `tasks/<id>/` | Update a specific task |
| DELETE | `tasks/<id>/` | Delete a specific task |

**Sample JSON Payload**
-----------------------

```json
{
    "title": "Read Django docs",
    "description": "Cover the REST framework section",
    "is_completed": false
}
```

**License**
------------

This project is licensed under the **MIT License**.

**Contributing**
----------------

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to modify or improve.
