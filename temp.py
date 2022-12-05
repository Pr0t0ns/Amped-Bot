import mysql.connector

class UserMySQLcommands:
    @staticmethod
    def create_account(userid: str):
        try:
            write_cursor.execute(f'INSERT INTO `amped`.`users`(`DiscordID`,`UID`,`balance`,`Devbadge`,`OGbadge`) VALUES ("{userid}", 0.0, 1, 1);')
            database.commit()
            return "Success"
        except Exception as err:
            print(err)
            return "Account already Exists!"
    @staticmethod
    def getbalance(userid: str):
        pass

    @staticmethod
    def tip_balance(userid: str, balance: float):
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

    
if __name__ == "__main__":
    database = mysql.connector.connect (
        host='127.0.0.1',
        user='root',
        passwd='root',
        database='amped'
    )
    print("connected to MySQL database")
    write_cursor = database.cursor()
    read_cursor = database.cursor(buffered=True)