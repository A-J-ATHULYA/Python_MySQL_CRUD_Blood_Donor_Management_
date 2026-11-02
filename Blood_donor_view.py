
import mysql.connector
import datetime

class BloodDonorManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Athulya@30",
            database = "blood_db"
        )

    print("Connected Successfully...")

    def get_object(self, id=None):
        try:
            self.cursor = self.connection.cursor()
            query = "select * from donor where id = %s"
            values = (id,)
            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            print(e)


    def post(self, **kwargs):
        try:
            self.cursor = self.connection.cursor()
            query = "insert into donor(name, blood_group, phone, city, last_donation) values(%s, %s, %s, %s, %s)"
            values = [v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.connection.commit()
            print("Donor added successfully....")
        except Exception as e:
            print(e)
    def get(self):
        try:
            self.cursor = self.connection.cursor()
            query = "select * from donor"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            # print(records)
            # for data in records:
            #     print(data)
            return(records)
        except Exception as e:
            return []

    def retrieve(self, id=None):
        try:
            # self.cursor = self.connection.cursor()
            # query = "select * from donor where id = %s"
            # values = (id,)
            # self.cursor.execute(query, values)
            # record = self.cursor.fetchone()
            record = self.get_object(id)
            print(record)
        except Exception as e:
            print(e)

    def delete(self, id=None):
        try:
            # self.cursor = self.connection.cursor()
            # query = "select * from donor where id = %s"
            # values = (id,)
            # self.cursor.execute(query, values)
            # record = self.cursor.fetchone()
            record = self.get_object(id)
            values = (id,)

            if record != None:
                query = "delete from donor where id = %s"
                self.cursor.execute(query, values)
                self.connection.commit()
                print("Donor deleted successfully...")
            else:
                print("Donor not found...")
        except Exception as e:
            print(e)

    def put(self, id=None, **kwargs):
        try:
            record = self.get_object(id=id) # check whether the record exists
            if record != None: #if a record if found, record will not be None
                # So the update operation continues
                self.cursor = self.connection.cursor()
                placeholder = "" # Creates an empty string, this variable will
                # used to construct the Set part of the SQL query.
                for k in kwargs.keys():  # (keys only that is name city .........)
                    placeholder += k + "=%s, "  # (K + "=%s," MEANS key =value, ----> name = anu, )
                placeholder = placeholder.rstrip(", ") # rstrip removes last comma
                query = f"update donor set {placeholder} where id = %s" # formatted string
                values = [v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query, values)
                self.connection.commit()
                print("Donor updated successfully...")
            else:
                print("Donor not found..!")
        except Exception as e:
            print(e)


#
donor_instance = BloodDonorManager()
# # donor_instance.post(name="Aju", blood_group="B-", city="Aluva", phone="1204567770", last_donation=datetime.datetime.today())
# donor_instance.get()
# print("----------------------------------------------")
# donor_instance.retrieve(1)
# print("----------------------------------------------")
# donor_instance.delete(2)
# donor_instance.get()
# print("---------------------After deletion-------------------------")
# donor_instance.get()
# print("-------------------------updation---------------------")
# donor_instance.put(2, name="Farhan")
#
# donor_instance.retrieve(2)
#
# donor_instance.put(2, phone=9999992228)
#
donor_instance.put(3, phone=99990092228)
donor_instance.retrieve(3)
