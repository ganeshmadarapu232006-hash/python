from abc import ABC, abstractmethod

class Database(ABC):

    @abstractmethod
    def connect(self):
        pass
class MySQL(Database):

    def connect(self):
        print("Connected to MySQL Database")

class PostgreSQL(Database):

    def connect(self):
        print("Connected to PostgreSQL Database")

class MongoDB(Database):

    def connect(self):
        print("Connected to MongoDB Database")

databases = [
    MySQL(),
    PostgreSQL(),
    MongoDB()
]

for database in databases:
    database.connect()