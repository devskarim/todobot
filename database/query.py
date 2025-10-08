from .connection import get_connect


def create_table():
    sql = """
    CREATE TABLE IF NOT EXISTS user_task(
        id BIGSERIAL PRIMARY KEY, 
        chat_id BIGINT, 
        task VARCHAR(300) NOT NULL, 
        level VARCHAR(100),
        descrip TEXT
    )
    """ 
    return sql


with get_connect() as db:
    with db.cursor() as dbc:
        dbc.execute(create_table())
    db.commit()


def save_user_task(chat_id, task, level, descrip=None):
    try:
        with get_connect() as db:
            with db.cursor() as dbc:
                dbc.execute("""
                    INSERT INTO user_task (chat_id, task, level, descrip)
                    VALUES (%s, %s, %s, %s)
                """, (chat_id, task, level, descrip))
            db.commit()
    except Exception as e:
        print("Err:", e)


def user_task_from_chat_id(chat_id):
    try:
        with get_connect() as db:
            with db.cursor() as dbc:
                dbc.execute("""
                    SELECT task, level, descrip 
                    FROM user_task
                    WHERE chat_id = %s
                """, (chat_id,))
                tasks = dbc.fetchall()  
                return tasks
    except Exception as e:
        print("Err:", e)
        return []
