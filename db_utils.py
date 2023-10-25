import mysql.connector
from config import USER, PASSWORD, HOST


class DbConnectionError(Exception):
    pass


def connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx


def get_item_list_util():
    try:
        db_name = 'swap_shop'
        db_connection = connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f'Connected to DB: {db_name}')
        query = """SELECT * FROM items;"""
        cur.execute(query)
        result = cur.fetchall()
        cur.close()
    except Exception:
        raise DbConnectionError('Failed to read data from DB')
    finally:
        if db_connection:
            db_connection.close()
            print('DB connection closed')
    print(result)
    return result


def buy_item_util(item):
    try:
        db_name = 'swap_shop'
        db_connection = connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f'Connected to DB: {db_name}')
        query = f"""DELETE FROM items WHERE item_name = '{item}'"""
        cur.execute(query)
        db_connection.commit()
        cur.close()
    except Exception:
        raise DbConnectionError('Failed to read data from DB')
    finally:
        if db_connection:
            db_connection.close()
            print('DB connection closed')


def sell_item_util(item):
    try:
        db_name = 'swap_shop'
        db_connection = connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f'Connected to DB: {db_name}')
        query = f"""INSERT INTO items (item_name) VALUES ('{item}')"""
        cur.execute(query)
        db_connection.commit()
        cur.close()
    except Exception:
        raise DbConnectionError('Failed to read data from DB')
    finally:
        if db_connection:
            db_connection.close()
            print('DB connection closed')

