if __name__ == '__main__':
    print("Please use this as a module.")
    exit(1)

import sqlite3

cursor = sqlite3.connect('db.db')
