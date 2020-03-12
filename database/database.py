import sqlite3


class ConnectDB:
    """Подключение к базе данных."""

    datebase = 'base.db'
    connection = sqlite3.connect(datebase)
    cursor = connection.cursor()


class Cursor(ConnectDB):
    """Класс для запросов в базу данных."""

    def make_query(self, query):
        """Метод для отправки запросов."""

        return self.cursor.execute(query)

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

    table = 'commands'

    def get_command_list(self):
        """Метод для получения записей из таблицы Commands."""

        return self.get_all_records(self.table)

    def create_command(self, question, answer):
        """Метод для создания записи в таблице Commands."""

        return self.create_record(self.table, question, answer)


class PhraseManager(Cursor):
    """Класс для работы с таблицей Phrases."""

    table = 'phrases'

    def get_phrase_list(self):
        """Метод для получения записей из таблицы Phrases."""

        return self.get_all_records(self.table)