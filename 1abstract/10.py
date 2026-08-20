from abc import ABC, abstractmethod

class Database(ABC):

    @abstractmethod
    def connect(self):
        pass

class MySQLDatabase(Database):

    def connect(self):
        print("Connecting to MySQL Database")


class PostgreSQLDatabase(Database):

    def connect(self):
        print("Connecting to PostgreSQL Database")

mysql = MySQLDatabase()
postgresql = PostgreSQLDatabase()

mysql.connect()
postgresql.connect()