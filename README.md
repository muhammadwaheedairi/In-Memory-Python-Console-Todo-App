# In-Memory Python Console Todo App

A simple, in-memory todo application that runs in the console. This application allows you to manage your tasks with basic CRUD operations.

## Features

- Add tasks with title and description
- List all tasks with status indicators
- Update task details
- Delete tasks by ID
- Mark tasks as complete/incomplete
- Console-based interface

## Requirements

- Python 3.13+
- UV package manager (optional, for virtual environment management)

## Setup

1. Clone or download this repository
2. Navigate to the project directory
3. Run the application directly with Python:

```bash
python src/main.py
```

## Usage

Once the application is running, you can use the following commands:

### Available Commands

- `add "title" "description"` - Add a new task
- `list` - List all tasks
- `update id "title" "description"` - Update a task
- `delete id` - Delete a task
- `complete id` - Mark task as complete
- `incomplete id` - Mark task as incomplete
- `help` - Show available commands
- `quit` or `exit` - Exit the application

### Examples

```bash
# Add a new task
add "Buy groceries" "Milk, bread, eggs"

# List all tasks
list

# Update a task (ID 1)
update 1 "Buy groceries" "Milk, bread, eggs, fruits"

# Mark a task as complete (ID 1)
complete 1

# Delete a task (ID 1)
delete 1
```

## Project Structure

```
src/
├── models/
│   ├── __init__.py
│   └── task.py          # Task data model
├── managers/
│   ├── __init__.py
│   └── task_manager.py  # Task business logic
├── interfaces/
│   ├── __init__.py
│   └── console.py       # Console interface
├── __init__.py
└── main.py              # Main application entry point
```

## Implementation Details

- All data is stored in memory only (no persistent storage)
- Console-based interface only
- Built with Python standard library only (no external dependencies)
- Follows object-oriented design principles

## Specifications

This application was built following the Spec-Driven Development approach:

- Specification: `specs/todo-app/spec.md`
- Implementation Plan: `specs/todo-app/plan.md`
- Implementation Tasks: `specs/todo-app/tasks.md`
- Project Constitution: `.specify/memory/constitution.md`

## Task IDs

All code includes references to the task IDs from the implementation plan:

- T-001: Task Model
- T-002: Task Manager
- T-003: Console Interface
- T-004: Main Application