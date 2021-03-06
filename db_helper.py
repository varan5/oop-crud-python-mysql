import mysql.connector as connector

class DBHelper:

    def __init__(self):
        self.con = connector.connect(host='localhost',
                                    user='Varan',
                                    password='hidden password',
                                    database='python_crud',
                                    auth_plugin='mysql_native_password')
        # cursor = self.con.cursor()
        # query = 'CREATE TABLE IF NOT EXISTS user(user_id INT PRIMARY KEY, user_name VARCHAR(200), phone VARCHAR(12))'
        # cursor.execute(query)

    def insert_user(self, user_id, user_name, phone):
        query = "INSERT INTO user(user_id, user_name, phone) VALUES({}, '{}', '{}')".format(user_id, user_name, phone)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print('Data inserted successfully !')

    def fetch_all_data(self):
        query = 'SELECT * FROM user'
        cursor = self.con.cursor()
        cursor.execute(query)
        query_result = cursor.fetchall()
        print('Fetching all the data from the database...\n')
        for data in query_result:
            print('Userid: ', data[0])
            print('Username: ', data[1])
            print('Phone: ', data[2])
            print()
            print()
            
    def delete_user(self, user_id):
        query = 'DELETE FROM user WHERE user_id={}'.format(user_id)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print('User with UserId: ', user_id, 'was deleted succesfully')
        
    def update_user(self, user_id, new_user_name, new_phone):
        query = "UPDATE user SET user_name='{}', phone='{}' WHERE user_id={}".format(new_user_name, new_phone, user_id)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print('Data updated succesfully !')


