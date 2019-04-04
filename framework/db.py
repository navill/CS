import psycopg2 as pg2

class DbManager:
    conn = None
    cursor = None
    def __init__(self):
        DbManager.conn = pg2.connect(database='wsgi_db', user='django',
                            password='PythonMaster')
        DbManager.cursor = DbManager.conn.cursor()

    def __del__(self):
        DbManager.cursor.close()
        DbManager.conn.close()

    def get_queryset(self):
        DbManager.cursor.execute(
        """
        SELECT *
        FROM post;
        """
        )
        query_set = DbManager.cursor.fetchall()
        return query_set

    def retrieve_post(self, id):
        DbManager.cursor.execute(
        """
        SELECT *
        FROM post
        WHERE id=%s
        """, (id,))
        return DbManager.cursor.fetchone()

    def create_post(self, title, content):
        DbManager.cursor.execute(
        """
        SELECT *
        FROM post
        ORDER BY id DESC
        LIMIT 1
        """
        )
        id = DbManager.cursor.fetchone()[0]
        id += 1

        DbManager.cursor.execute(
        """
        INSERT INTO post
        VALUES(%s, %s, %s);
        """, (id, title, content))
        DbManager.conn.commit()

    def update_post(self, id, title, content):
        DbManager.cursor.execute(
        """
        UPDATE post
        SET title= %s, content=%s
        WHERE id=%s;
        """
        , (title, content, id))

    def delete_post(self, id):
        DbManager.cursor.execute(
        """
        DELETE FROM post
        WHERE id=%s;
        """, (id, ))
        DbManager.conn.commit()

db_manager = DbManager()
