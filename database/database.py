import sqlite3


class ConnectDB:
    """Подключение к базе данных."""

    database = 'base.db'
    connection = sqlite3.connect(database)
    cursor = connection.cursor()


class Cursor(ConnectDB):
    """Класс для запросов в базу данных."""

    def make_query(self, query):
        """Метод для отправки запросов."""

        return self.cursor.execute(query)

    def create_table(self, table, values):
        """Метод для создания таблицы, если ее не существует."""

        query = f"""SELECT name FROM sqlite_master
                    WHERE type='table'
                    AND name='{table}'"""
        if self.make_query(query).fetchone() is None:
            query = f"CREATE TABLE {table} ({values})"
            self.make_query(query)

    def get_all_records(self, table):
        """Метод для получения всех записей."""

        query = f"SELECT * FROM {table}"
        return self.make_query(query).fetchall()

    def create_record(self, table, question, answer):
        """Метод для создания записи."""

        query = f"INSERT INTO {table} VALUES ('{question}', '{answer}')"
        self.make_query(query)
        self.connection.commit()


class CommandManager(Cursor):
    """Класс для работы с таблицей Commands."""

    table = "commands"
    values = "question text, answer text"

    def get_command_list(self):
        """Метод для получения записей из таблицы Commands."""

        # создается таблица, если ее не существует
        self.create_table(self.table, self.values)

        return self.get_all_records(self.table)

    def create_command(self, question, answer):
        """Метод для создания записи в таблице Commands."""

        return self.create_record(self.table, question, answer)
