from Serhii_Hidenko.l_8_software_engineering.hw.proxy.abstract_db import AbstractDb
from Serhii_Hidenko.l_8_software_engineering.hw.proxy.db import Db


class CachedDb(AbstractDb):

    def __init__(self):

        self.__real_class = Db()
        self.__query_cache = {}

    def execute_query(self, query, params=None):

        if self.__is_query_cached(query, params):
            return self.__cached_query(query, params)

        return self.__real_class.execute_query(query, params)

    def connect(self):
        pass  # Here must be connect to db

    def disconnect(self):
        pass  # Here must be disconnect from db

    def __is_query_cached(self, query, params):
        return True if self.__cached_query(query, params) is not None else False

    def __cached_query(self, query, params):
        return self.__query_cache[hash((query, params))]
