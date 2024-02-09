import pyrebase
from MyDB import MyDB
from User import User


config = {
  "apiKey": "AIzaSyAtlKFYpU1d58_ax9OFojVeme40s4H0IqA",
  "authDomain": "finances-eceff.firebaseapp.com",
  "databaseURL": "https://finances-eceff-default-rtdb.firebaseio.com",
  "projectId": "finances-eceff",
  "storageBucket": "finances-eceff.appspot.com",
  "messagingSenderId": "322348907663",
  "appId": "1:322348907663:web:785f1269fdf84a4c1244fa"
}

#firebase = pyrebase.initialize_app(config)
#database = firebase.database()

#data = {"Name": "Petro", "Phone": "0987642845"}
#database.push(data)

myDb = MyDB(config)
user = User("Ivan", "Ivanov", "sun0237", "12345","5000", "0")
print(user.getName())
user_data = user.to_dict()
myDb.insertValues("-Nq7uPdYs2oDhvUnL9ez", user_data)