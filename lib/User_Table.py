import sqlite3


def create_users_table(cls):
    sql = '''
        CREATE TABLE IF NOT EXISTS Users 
		(
            user_id INTEGER PRIMARY KEY
			username TEXT
		)
    '''


def create_clothes_table(cls):
    sql = """
		CREATE TABLE IF NOT EXSISTS clothes
		(
			id INTEGER PRIMARY KEY
			name TEXT
			type TEXT
			color TEXT
			pattern TEXT
			style TEXT
			size TEXT
			user_id INTEGER
				FOREIGN KEY(user_id) REFERENCES users(id)
		)
	"""


class Users:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username


class Clothes:
    def __init__(self, item_id, name, type, color, pattern, style, size, user_id):
        self.item_id = item_id
        self.name = name
        self.type = type
        self.color = color
        self.pattern = pattern
        self.style = style
        self.size = size
        self.user_id = user_id


class Closet:
    pass
