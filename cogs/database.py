import mysql.connector

database = mysql.connector.connect (
    host='127.0.0.1',
    user='root',
    passwd='root',
    database='amped'
)

database.autocommit(True)

write_cursor = database.cursor()
read_cursor = database.cursor(buffered=True)


class UserMySQLcommands:
    @staticmethod
    def create_account(id: str):
        pass

    @staticmethod
    def getbalance(id: str):
        pass

    @staticmethod
    def tip_balance(id: str, balance: float):
        pass

class ServerMySQLcommands:
    @staticmethod
    def get_server_prefix(server_id: str):
        pass


class GlobalDataMySQLcommands:
    @staticmethod 
    def get_leaderboard():
        pass

    @staticmethod
    def get_total_economy_stats():
        pass

    