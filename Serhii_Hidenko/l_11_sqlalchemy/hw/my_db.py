from sqlalchemy_utils import create_database, database_exists


class MyDb:

    def __init__(
            self,
            username: str = "",
            password: str = "",
            database: str = "",
            hostname: str = "",
            port: str = ""):
        """
        Create object and initiate connection url
        :param username: Username for connection to DB
        :type username: str
        :param password: Passord of user for connection to DB
        :type password: str
        :param database: Database to connection
        :type database: str
        :param hostname: Hostname to connection
        :type hostname: str
        :param port: Port to connection
        :type port: str
        """

        self.__connection_url = f"postgresql://{username}:{password}@" \
                                f"{hostname}:{port}/{database}"

    def create_db(self):
        """Create db by connection url if not exists"""

        if not database_exists(url=self.__connection_url):
            create_database(url=self.__connection_url)

    @property
    def connection_url(self) -> str:
        """Getter for connection url"""

        return self.__connection_url

    @staticmethod
    def create_tables(base=None, engine=None, metadata=None):
        """Function for creating initiated tables in db"""

        if not metadata:
            base.metadata.create_all(engine)
        else:
            metadata.create_all(engine)
