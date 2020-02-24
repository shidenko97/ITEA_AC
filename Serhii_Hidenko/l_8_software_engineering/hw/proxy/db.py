from Serhii_Hidenko.l_8_software_engineering.hw.proxy.abstract_db import (
    AbstractDb,
)


class Db(AbstractDb):
    def execute_query(self, query, params=None):
        pass  # Here must be query to db

    def connect(self):
        pass  # Here must be connect to db

    def disconnect(self):
        pass  # Here must be disconnect from db
