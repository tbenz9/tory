import sqlite3


def add_network_to_database(dict):
    connection = sqlite3.connect("connection.db")

    cursor = connection.cursor()
    
    cursor.execute("""DROP TABLE network;""")
    
    sql_command = """
    CREATE TABLE network (
    id INTEGER PRIMARY KEY,
    name STRING,
    mac_address STRING, 
    ip_address STRING,
    speed FLOAT,
    link BOOLEAN);"""
   

    cursor.execute(sql_command)
    
    for name in dict:
        format_str = """INSERT INTO network (id, name, mac_address, ip_address, speed, link) VALUES (NULL, "{thisname}", "{mac_address}", "{ip_address}", "{speed}", "{link}");"""

        sql_command = format_str.format(thisname = name, mac_address = dict[name]["mac_address"], ip_address = dict[name]["ip_address"], speed = dict[name]["speed"], link = dict[name]["link"])

        cursor.execute(sql_command)
    
    connection.commit()

    connection.close()

    
def get_network_from_database():

    connection = sqlite3.connect("connection.db")

    cursor = connection.cursor()
    
    cursor.execute("""SELECT * FROM network""")
    result = cursor.fetchall()
    for name in result:
        print name

    connection.close()
