import psycopg2


class PostgreConnector:

    def __init__(self, username, password, database=None):
        """
        On init - create database connection
        :param username: Database username
        :type username: str
        :param password: Database password
        :type password: str
        :param database: Database name
        :type database: str
        """

        self.__connection = psycopg2.connect(
            user=username,
            password=password,
            database=database
        )

    def __enter__(self):
        """On enter to context manager - getting connection cursor"""

        return self.__connection.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """On exit from context manager - commit and close or rollback"""

        if exc_tb is None:

            self.__connection.commit()
            self.__connection.close()

        else:
            self.__connection.rollback()
