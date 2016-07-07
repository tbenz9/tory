import sqlite3

# adds a network dict to the database
def add_network_to_database(dict):
    connection = sqlite3.connect("connection.db")

    cursor = connection.cursor()
    
    sql_command = """
    CREATE TABLE IF NOT EXISTS network (
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



# adds a cpu dict to the database
def add_cpu_to_database(dict):
    connection = sqlite3.connect("connection.db")

    cursor = connection.cursor()

    sql_command = """
    CREATE TABLE IF NOT EXISTS cpu (
    id INTEGER PRIMARY KEY,
    num_cpus INTEGER,
    num_cores_per_cpu INTEGER,
    num_threads_per_core INTEGER,
    cpu_model STRING,
    cpu_model_name STRING,
    cpu_speed STRING,
    serial_number STRING); 
    """

    cursor.execute(sql_command)

    format_str = """INSERT INTO cpu (id, num_cpus, num_cores_per_cpu, num_threads_per_core, cpu_model, cpu_model_name, cpu_speed, serial_number)
    VALUES (NULL, "{num_cpus}", "{num_cors_per_cpu}", "{num_threds_per_core}", "{cpu_model}", "{cpu_model_name}", "{cpu_speed}", "{serial_number}");"""

    sql_command = format_str.format(num_cpus =  dict['num_cpus'], num_cors_per_cpu = dict["num_cors_per_cpu"], num_threds_per_core = dict["num_threds_per_core"], cpu_model = dict["cpu_model"], cpu_model_name = dict["cpu_model_name"], cpu_speed = dict["cpu_speed"], serial_number = dict["serial_number"])

    cursor.execute(sql_command)

    connection.commit()

    connection.close()


#adds a ram dict to the database
def add_ram_to_database(dict):
    connection = sqlite3.connect("connection.db")

    cursor = connection.cursor()

    sql_command = """
    CREATE TABLE IF NOT EXISTS ram (
    id INTEGER PRIMARY KEY,
    total_ram INTEGER,
    free_ram INTEGER,
    swap_space INTEGER,
    os_version STRING,
    kernel_version STRING,
    hostname  STRING)
    """

    cursor.execute(sql_command)

    format_str = """INSERT INTO ram (id,total_ram, free_ram, swap_space, os_version, kernel_version, hostname) 
    VALUES (NULL, "{total_ram}", "{free_ram}", "{swap_space}", "{os_version}", "{kernel_version}", "{hostname}");"""

    sql_command  = format_str.format(total_ram = dict["total_ram"], free_ram = dict["free_ram"], swap_space = dict["swap_space"], os_version = dict["os_version"], kernel_version = dict["kernel_version"], hostname = dict["hostname"]);

    cursor.execute(sql_command)

    connection.commit()

    connection.close()


#gets the table from the database    
def get_from_database(which):

    connection = sqlite3.connect("connection.db")

    cursor = connection.cursor()
    
    format_str = ("""SELECT * FROM "{type}" """)

    sql_command = format_str.format(type=which)
    
    cursor.execute(sql_command)
    result = cursor.fetchall()
    for name in result:
        print name

    connection.close()
