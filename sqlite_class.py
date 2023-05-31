import sqlite3

class Database():
    conn = sqlite3.connect("sqlite_baza.db")
    cursor = conn.cursor()

    def create_table_users(self):
        self.cursor.execute("create table if not exists Users ( \
                            username varchar(150), \
                            telegram_id int, \
                            phone_number varchar(30) \
                            )")

    def select_users(self, telegram_id):
        self.cursor.execute("select * from Users where telegram_id={}".format(telegram_id))
        return self.cursor.fetchone()

    def insert_users(self, username, telegram_id, phone_number):
        self.cursor.execute("insert into Users values ('{}', {}, '{}')".format(username, telegram_id, phone_number))
        self.conn.commit()

