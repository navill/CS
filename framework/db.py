from mysql.connector import MySQLConnection
from configparser import ConfigParser

class SingletonError(Exception):
    pass

class DBManager:
    dbmanager=None

    @classmethod
    def get_instance(cls):
        return cls.dbmanager
    
    @staticmethod
    def get_conf(filename='conf.ini'):
        parser=ConfigParser()
        parser.read(filename)
        conf={}
        if parser.has_section('mysql'):
            items=parser.items('mysql')
            for key, value in items:
                conf[key]=value
            return conf
        return None

    def __init__(self):
        if DBManager.dbmanager:
            raise SingletonError("There is already another DBManager instance")

        conf=DBManager.get_conf()
        self.conn=MySQLConnection(**conf)

    def init(self):
        DBManager.dbmanager=self
        
    def __del__(self):
        self.conn.close()

    def get_queryset(self):
        cursor=self.conn.cursor()
        cursor.execute(
        """
        SELECT *
        FROM post;
        """
        )
        query_set = cursor.fetchall()
        cursor.close()

        return query_set

    def retrieve_post(self, id):
        cursor=self.conn.cursor()
        cursor.execute(
        """
        SELECT *
        FROM post
        WHERE id=%s
        """, (id,))
        record=cursor.fetchone()
        cursor.close()
        
        return record

    def create_post(self, title, content):
        cursor=self.conn.cursor()
        cursor.execute(
        """
        INSERT INTO post 
        (title, content)
        VALUES(%s, %s);
        """, (title, content))
        self.conn.commit()
        cursor.close()

    def update_post(self, id, title, content):
        cursor=self.conn.cursor()
        cursor.execute(
        """
        UPDATE post
        SET title= %s, content=%s
        WHERE id=%s;
        """
        , (title, content, str(id)))
        self.conn.commit()
        cursor.close()

    def delete_post(self, id):
        cursor=self.conn.cursor()
        cursor.execute(
        """
        DELETE FROM post
        WHERE id=%s;
        """, (str(id), ))
        self.conn.commit()
        cursor.close()

db_manager = DBManager()
db_manager.init()
