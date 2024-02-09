import pyrebase
class MyDB:
    def __init__(self, firebaseConfig):
        self.firebase = pyrebase.initialize_app(firebaseConfig)
        self.database = self.firebase.database()


    def insertValues(self, table_name, data):
        try:
            # Check if the record already exists based on some criteria (e.g., email)
            existing_records = self.database.child(table_name).order_by_child("email").equal_to(data.get("email")).get()

            if not existing_records.each():
                # If no matching records found, insert the new data
                self.database.child(table_name).push(data)
                print("Data inserted successfully!")
            else:
                print("Record with the same email already exists. Not inserting.")

        except Exception as e:
            print("Error inserting data:", e)
    '''
    def insertValues(self, table_name, data):
        try:
            self.database.child(table_name).push(data)
            print("Data inserted successfully!")
        except Exception as e:
            print("Error inserting data:", e)
    '''
    def updateValues(self, table_name, key, data):
        try:
            self.database.child(table_name).child(key).update(data)
            print("Data updated successfully!")
        except Exception as e:
            print("Error updating data:", e)

    def selectValues(self, table_name):
        try:
            data = self.database.child(table_name).get().val()
            if data:
                print("Selected data from", table_name, ":", data)
            else:
                print("No data found in", table_name)
        except Exception as e:
            print("Error selecting data:", e)

    def create_table(self, table_name):
        try:
            self.database.child(table_name).set({})
            print("Table", table_name, "created successfully!")
        except Exception as e:
            print("Error creating table:", e)