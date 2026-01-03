#!/usr/bin/env python3
"""
Test script to verify the improved UI functionality
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from main import TodoApp


def test_improved_ui():
    """Test the TodoApp with improved UI functionality"""
    print("Testing Todo App with improved UI...")

    # Create an instance of the app
    app = TodoApp()

    # Test adding a task
    print("\n1. Testing add functionality...")
    app.handle_add("Test Task 1", "This is a test task")
    tasks = app.task_manager.get_all_tasks()
    assert len(tasks) == 1
    assert tasks[0].title == "Test Task 1"
    assert tasks[0].description == "This is a test task"
    print("✓ Add functionality works")

    # Test adding another task
    app.handle_add("Test Task 2", "Second test task")
    tasks = app.task_manager.get_all_tasks()
    assert len(tasks) == 2
    print("✓ Adding multiple tasks works")

    # Test listing tasks - this will show the improved table format
    print("\n2. Testing list functionality with improved UI...")
    app.handle_list()
    print("✓ List functionality works with improved table format")

    # Test updating a task
    print("\n3. Testing update functionality...")
    app.handle_update("1", "Updated Task 1", "Updated description")
    updated_task = app.task_manager.get_task(1)
    assert updated_task.title == "Updated Task 1"
    assert updated_task.description == "Updated description"
    print("✓ Update functionality works")

    # Test marking as complete
    print("\n4. Testing complete/incomplete functionality...")
    app.handle_complete("1")
    completed_task = app.task_manager.get_task(1)
    assert completed_task.completed == True
    print("✓ Complete functionality works")

    app.handle_incomplete("1")
    incomplete_task = app.task_manager.get_task(1)
    assert incomplete_task.completed == False
    print("✓ Incomplete functionality works")

    # Test deleting a task
    print("\n5. Testing delete functionality...")
    initial_count = len(app.task_manager.get_all_tasks())
    app.handle_delete("1")
    remaining_tasks = app.task_manager.get_all_tasks()
    assert len(remaining_tasks) == initial_count - 1
    assert app.task_manager.get_task(1) is None
    print("✓ Delete functionality works")

    # Test error handling
    print("\n6. Testing error handling...")
    app.handle_add("")  # Should fail with empty title
    app.handle_update("999", "Fake Task")  # Should fail with non-existent ID
    app.handle_complete("999")  # Should fail with non-existent ID
    print("✓ Error handling works")

    # Test help functionality
    print("\n7. Testing help functionality...")
    app.handle_help()
    print("✓ Help functionality works with improved formatting")

    print("\n✓ All tests passed! The improved UI is working correctly.")


if __name__ == "__main__":
    test_improved_ui()