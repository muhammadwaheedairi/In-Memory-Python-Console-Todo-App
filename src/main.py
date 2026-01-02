from typing import Optional

# Handle imports when running as a script vs as a module
try:
    # When running as part of the package
    from .managers.task_manager import TaskManager
    from .interfaces.console import ConsoleInterface
    from .models.task import Task
except ImportError:
    # When running as a script
    import sys
    import os
    # Add src directory to path to allow imports
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))

    from managers.task_manager import TaskManager
    from interfaces.console import ConsoleInterface
    from models.task import Task


class TodoApp:
    """
    Main application class that ties all components together.

    [Task]: T-004
    [From]: specs/todo-app/spec.md §All Functional Requirements, specs/todo-app/plan.md §Main Application
    """

    def __init__(self):
        """
        Initialize the TodoApp with required components.
        """
        self.task_manager = TaskManager()
        self.console = ConsoleInterface()
        self.running = True

        # Command mapping dictionary
        self.commands = {
            'add': self.handle_add,
            'list': self.handle_list,
            'update': self.handle_update,
            'delete': self.handle_delete,
            'complete': self.handle_complete,
            'incomplete': self.handle_incomplete,
            'help': self.handle_help,
            'quit': self.handle_quit,
            'exit': self.handle_quit,
        }

    def run(self) -> None:
        """
        Run the main application loop.
        """
        print("Welcome to the Todo App!")
        print("Type 'help' for available commands or 'quit' to exit.")

        while self.running:
            try:
                user_input = self.console.get_user_input()
                command, args = self.console.parse_command(user_input)

                if command in self.commands:
                    self.commands[command](*args)
                elif command:
                    self.console.display_error(f"Unknown command: {command}")
                    self.console.display_message("Type 'help' for available commands.")
                # If command is empty, just continue the loop
            except KeyboardInterrupt:
                print("\nExiting...")
                self.running = False
            except Exception as e:
                self.console.display_error(f"An error occurred: {str(e)}")

    def handle_add(self, *args) -> None:
        """
        Handle the add command to create a new task.

        Args:
            *args: Arguments for the add command (title, optional description)
        """
        if len(args) < 1:
            self.console.display_error("Usage: add \"title\" [\"description\"]")
            return

        title = args[0]
        description = args[1] if len(args) > 1 else ""

        try:
            task = self.task_manager.add_task(title, description)
            self.console.display_message(f"Task added successfully with ID: {task.id}")
        except ValueError as e:
            self.console.display_error(str(e))

    def handle_list(self, *args) -> None:
        """
        Handle the list command to display all tasks.

        Args:
            *args: Arguments for the list command (none expected)
        """
        tasks = self.task_manager.get_all_tasks()
        self.console.display_tasks(tasks)

    def handle_update(self, *args) -> None:
        """
        Handle the update command to modify an existing task.

        Args:
            *args: Arguments for the update command (id, title, optional description)
        """
        if len(args) < 2:
            self.console.display_error("Usage: update id \"title\" [\"description\"]")
            return

        try:
            task_id = int(args[0])
        except ValueError:
            self.console.display_error("Task ID must be a number")
            return

        title = args[1]
        description = args[2] if len(args) > 2 else ""

        try:
            task = self.task_manager.update_task(task_id, title, description)
            if task:
                self.console.display_message(f"Task {task_id} updated successfully")
            else:
                self.console.display_error(f"Task with ID {task_id} not found")
        except ValueError as e:
            self.console.display_error(str(e))

    def handle_delete(self, *args) -> None:
        """
        Handle the delete command to remove a task.

        Args:
            *args: Arguments for the delete command (id)
        """
        if len(args) < 1:
            self.console.display_error("Usage: delete id")
            return

        try:
            task_id = int(args[0])
        except ValueError:
            self.console.display_error("Task ID must be a number")
            return

        deleted = self.task_manager.delete_task(task_id)
        if deleted:
            self.console.display_message(f"Task {task_id} deleted successfully")
        else:
            self.console.display_error(f"Task with ID {task_id} not found")

    def handle_complete(self, *args) -> None:
        """
        Handle the complete command to mark a task as complete.

        Args:
            *args: Arguments for the complete command (id)
        """
        if len(args) < 1:
            self.console.display_error("Usage: complete id")
            return

        try:
            task_id = int(args[0])
        except ValueError:
            self.console.display_error("Task ID must be a number")
            return

        task = self.task_manager.mark_task_complete(task_id)
        if task:
            self.console.display_message(f"Task {task_id} marked as complete")
        else:
            self.console.display_error(f"Task with ID {task_id} not found")

    def handle_incomplete(self, *args) -> None:
        """
        Handle the incomplete command to mark a task as incomplete.

        Args:
            *args: Arguments for the incomplete command (id)
        """
        if len(args) < 1:
            self.console.display_error("Usage: incomplete id")
            return

        try:
            task_id = int(args[0])
        except ValueError:
            self.console.display_error("Task ID must be a number")
            return

        task = self.task_manager.mark_task_incomplete(task_id)
        if task:
            self.console.display_message(f"Task {task_id} marked as incomplete")
        else:
            self.console.display_error(f"Task with ID {task_id} not found")

    def handle_help(self, *args) -> None:
        """
        Handle the help command to display available commands.

        Args:
            *args: Arguments for the help command (none expected)
        """
        self.console.display_help()

    def handle_quit(self, *args) -> None:
        """
        Handle the quit command to exit the application.

        Args:
            *args: Arguments for the quit command (none expected)
        """
        self.console.display_message("Goodbye!")
        self.running = False


def main():
    """
    Main entry point for the application.
    """
    app = TodoApp()
    app.run()


if __name__ == "__main__":
    main()