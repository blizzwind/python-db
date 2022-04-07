# python-db
A native database written in python.

### build
- os

### setup
```
# git and python needed
git clone https://github.com/blizzwind/python-db
cd python-db
python main.py
```

### usage
```
# create
~ c db [demo]
~ c db [demo] table [user]
~ c db [demo] table [user] [{id:1, name:'me'}]
# read
~ r db [demo] table [user] [id=1] #read where id:1
# update
~ u db [demo] table [user] [id=1=2] #update where id:1 to id:2
# delete
~ d db [demo] table [user] [name='me'] #delete where name:'me'
```

### file
    .
    ├── __pycache__
    ├── __db__
        └── demo
            └── user.pydb
    ├── main.py
    └── db.py

### custom
customize could be made through editing main.py and db.py files
