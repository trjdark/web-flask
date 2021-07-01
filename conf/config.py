# 数据库配置
import pymysql
DB_CONFIG = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': '123456',
    'charset': 'utf8',
    'db': 'Trj_chart',
}

class SQLManager(object):
    # 初始化
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.connect()
    # 连接数据库
    def connect(self):
        self.conn = pymysql.connect(
            host = DB_CONFIG['host'],
            port = DB_CONFIG['port'],
            user = DB_CONFIG['user'],
            passwd = DB_CONFIG ['passwd'],
            db = DB_CONFIG['db'],
            charset = DB_CONFIG['charset']
        )
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 关闭数据库
    def close(self):
        self.cursor.close()
        self.conn.close()
    # 查询单条数据
    def get_one(self, sql, args=None):
        self.cursor.execute(sql, args)
        result = self.cursor.fetchone()
        return result
