import db

db.run()

while True:
    q = input("~ ")
    print(db.exc(q))
