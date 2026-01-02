from typing import List, Optional

# Handle imports when running as a script vs as a module
try:
    # When running as part of the package
    from ..models.task import Task
except ImportError:
    # When running as a script
    import sys
    import os
    # Add src directory to path to allow imports
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    from models.task import Task


class ConsoleInterface:
    """
    Handles user input/output operations for the todo application.

    [Task]: T-003
    [From]: specs/todo-app/spec.md §User Interface Commands, specs/todo-app/plan.md §Console Interface
    """

    def __init__(self):
        """
        Initialize the ConsoleInterface.
        """
        pass

    def display_tasks(self, tasks: List[Task]) -> None:
        """
        Display all tasks in a formatted way.

        Args:
            tasks (List[Task]): List of tasks to display
        """
        if not tasks:
            print("No tasks found.")
            return

        print("\nYour Tasks:")
        print("-" * 50)
        for task in tasks:
            status = "✓" if task.completed else "○"
            print(f"[{status}] {task.id}. {task.title}")
            if task.description:
                print(f"      Description: {task.description}")
            print(f"      Status: {task.get_status_text()}")
            print()

    def display_task(self, task: Task) -> None:
        """
        Display a single task with detailed information.

        Args:
            task (Task): Task to display
        """
        status = "✓" if task.completed else "○"
        print(f"\n[{status}] {task.id}. {task.title}")
        if task.description:
            print(f"Description: {task.description}")
        print(f"Status: {task.get_status_text()}")
        print(f"Created: {task.created.strftime('%Y-%m-%d %H:%M:%S')}")

    def display_message(self, message: str) -> None:
        """
        Display a simple message to the user.

        Args:
            message (str): Message to display
        """
        print(message)

    def display_error(self, error: str) -> None:
        """
        Display an error message to the user.

        Args:
            error (str): Error message to display
        """
        print(f"Error: {error}")

    def display_help(self) -> None:
        """
        Display help information with available commands.
        """
        help_text = """
Available Commands:
  add "title" "description"    - Add a new task
  list                        - List all tasks
  update id "title" "description" - Update a task
  delete id                   - Delete a task
  complete id                 - Mark task as complete
  incomplete id               - Mark task as incomplete
  help                        - Show this help message
  quit                        - Exit the application

Examples:
  add "Buy groceries" "Milk, bread, eggs"
  update 1 "Buy groceries" "Milk, bread, eggs, fruits"
  complete 1
        """
        print(help_text)

    def get_user_input(self, prompt: str = "> ") -> str:
        """
        Get input from the user.

        Args:
            prompt (str): Prompt to display to the user

        Returns:
            str: User input
        """
        return input(prompt)

    def parse_command(self, user_input: str) -> tuple:
        """
        Parse user command and extract arguments.

        Args:
            user_input (str): Raw user input

        Returns:
            tuple: (command, args) where command is the command string and args is a list of arguments
        """
        # Simple parsing that handles quoted strings
        parts = []
        current_part = ""
        in_quotes = False
        i = 0

        while i < len(user_input):
            char = user_input[i]

            if char == '"':
                in_quotes = not in_quotes
            elif char == ' ' and not in_quotes:
                if current_part:
                    parts.append(current_part)
                    current_part = ""
            else:
                current_part += char

            i += 1

        # Add the last part if it exists
        if current_part:
            parts.append(current_part)

        if not parts:
            return "", []

        command = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []

        return command, args