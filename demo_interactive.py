#!/usr/bin/env python3
"""
Demo script to show how to run the interactive menu version
"""
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from main import TodoApp

def demo():
    """Demonstrate the interactive menu functionality"""
    print("This demonstrates how the interactive menu works.")
    print("The application will start with an interactive menu.")
    print("\nTo try it yourself, simply run:")
    print("  python3 run.py")
    print("\nOr:")
    print("  python3 -c \"import sys; sys.path.append('./src'); from main import main; main()\"")

    # Create a sample app to show the interface elements
    app = TodoApp()

    print("\n" + "="*50)
    print("DEMONSTRATION OF MODERN CLI FEATURES")
    print("="*50)

    # Show the header
    app.console.display_header()

    # Show an example task list
    from models.task import Task
    task1 = Task(1, "Sample Task", "This is a sample task", False)
    task2 = Task(2, "Completed Task", "This task is completed", True)

    app.console.display_tasks([task1, task2])

    print("\nThe interactive menu provides:")
    print("✓ Rich-formatted tables with color-coded status indicators")
    print("✓ Interactive selection using Questionary")
    print("✓ Styled panels and headers")
    print("✓ Clear screen between actions")
    print("✓ Confirmation prompts for destructive actions")
    print("\nAll original functionality is preserved!")

if __name__ == "__main__":
    demo()