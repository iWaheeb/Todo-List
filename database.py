import sqlite3


class Database:
    @staticmethod
    def retrieve_rows():
        query = """SELECT * FROM todo_list"""
        rows = Database.execute_query(query, True)
        return rows

    @staticmethod
    def execute_query(query, return_result):
        conn = sqlite3.connect("todoList.db")
        c = conn.cursor()
        c.execute(query)
        if return_result:
            rows = c.fetchall()
            Database.end_connection(conn)
            return rows
        Database.end_connection(conn)

    @staticmethod
    def end_connection(conn):
        conn.commit()
        conn.close()


    @staticmethod
    def create_table():
        query = """CREATE TABLE if not exists todo_list(
                    task text)"""
        Database.execute_query(query, False)

    @staticmethod
    def delete_all_rows():
        query = """DELETE FROM todo_list;"""
        Database.execute_query(query, False)

    @staticmethod
    def insert(data):
        query = f"""INSERT INTO todo_list (task)
                        VALUES('{data}');"""
        Database.execute_query(query, False)
