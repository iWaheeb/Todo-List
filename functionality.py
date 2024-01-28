import sqlite3

from database import Database


class Operations:
    def add_task(ui):
        try:
            task = ui.input_line.text()
            ui.tasks_list.addItem(task)
            ui.input_line.setText("")
            Operations.save(ui)
        except:
            print("An error occurred in add_task function")

    def delete_task(ui):
        selected = ui.tasks_list.currentRow()
        ui.tasks_list.takeItem(selected)
        Operations.save(ui)

    def clear_list(ui):
        ui.tasks_list.clear()
        Operations.save(ui)

    def save(ui):
        try:
            # Clear the database
            Database.delete_all_rows()

            # Add new tasks to the database
            for i in range(ui.tasks_list.count()):
                new_task = ui.tasks_list.item(i)
                Database.insert(new_task.text())

        except:
            print("An error occurred in save function")


    def retrieve_tasks(ui):
        try:
            tasks = Database.retrieve_rows()

            for task in tasks:
                ui.tasks_list.addItem(task[0])

        except:
            print("An error occurred in retrieve_tasks function")
