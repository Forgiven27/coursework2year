import sqlite3

class DataBase:
    def __init__(self, path):
        self.path = path
        self.connection = sqlite3.Connection(self.path)
        self.cursor = self.connection.cursor()



    def table_names(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
        tables = self.cursor.fetchall()
        return tables

    def specific_zero_cell(self, table_name, column_name):
        self.cursor.execute(f"SELECT {column_name} FROM {table_name}")
        cell = self.cursor.fetchall()

        return cell[0][0]

    def update_cell(self, table_name, column_name, column_key, key_value, new_value):
        self.cursor.execute(f"UPDATE {table_name} SET {column_name} = {new_value} WHERE {column_key} = {key_value}")
        self.connection.commit()

    def specific_byte_cell(self):
        self.connection.text_factory = bytes
        self.cursor.execute(f"SELECT Img FROM Addition")
        cell = self.cursor.fetchall()
        self.connection.text_factory = str
        return cell[0][0]

    def specific_cell(self, table_name, column_name, column_id, id):
        self.cursor.execute(f"SELECT {column_name} FROM {table_name} WHERE {column_id}={id}")
        cell = self.cursor.fetchall()
        return cell

    def rows_columns(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name}")
        a = self.cursor.fetchall()

        return a

    def columns_names(self, table_name):
        self.cursor.execute(f"PRAGMA table_info({table_name})")
        names = [i[1] for i in self.cursor.fetchall()]
        return tuple(names)

    def update_table(self, mass,table_name):
        try:
            self.cursor.execute(f"DELETE FROM {table_name}")
            #self.connection.commit()
            for i in range(len(mass)):
                try:

                    beg = f"INSERT INTO {table_name}{self.columns_names(table_name)} VALUES{mass[i]}"
                    self.cursor.execute(beg)
                except:
                    print(f"Строка {i} не добавлена")
                    print("Name table - ", table_name)
                    print("Names of table - ", self.columns_names(table_name))
                    print("Value - ", mass[i])

                else:
                    print(f"Строка {i} добавлена")
            self.connection.commit()
        except:
            print("Таблица не обновлена")
        else:
            print("Таблица обновлена")
