from sqlalchemy_utils import create_database, database_exists
from sqlalchemy import create_engine


class MyDb:

    def __init__(
            self,
            username: str = "",
            password: str = "",
            database: str = "",
            hostname: str = "",
            port: str = ""
    ):
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
        self.__engine = create_engine(self.connection_url)

    def create_db(self):
        """Create db by connection url if not exists"""

        if not database_exists(url=self.__connection_url):
            create_database(url=self.__connection_url)

    def create_tables(self, base=None, metadata=None):
        """Function for creating initiated tables in db"""

        if not metadata:
            base.metadata.create_all(self.__engine)
        else:
            metadata.create_all(self.__engine)

    @property
    def connection_url(self) -> str:
        """Getter for connection url"""

        return self.__connection_url

    @classmethod
    def create(
            cls,
            username: str = "",
            password: str = "",
            database: str = "",
            hostname: str = "",
            port: str = ""
    ):
        """
        Initiate and create db if not exists
        :return: Created DB
        :rtype: MyDb
        """

        db_ = cls(
            username=username,
            password=password,
            hostname=hostname,
            database=database,
            port=port
        )
        db_.create_db()

        return db_
