import time
import pymysql
#获取数据库链接  获取游标
def get_conn():
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="123456", database="xtxy", charset="utf8")
    if conn == None:
        print("数据库链接失败")
    else:
        print("数据库链接成功")
    cursor = conn.cursor()
    return conn,cursor


#  释放资源
def close(conn,cursor):
    cursor.close();
    conn.close();


# 查询数据库数据
def query(sql,*args):
    conn,cursor = get_conn()
    cursor.execute(sql,args)
    res = cursor.fetchall()
    return res


def get_left1():
    sql = 'SELECT ds,confirm,suspect,heal,dead FROM history'
    res = query(sql)
    print(res)
    return res

def get_left2():
    sql = "SELECT ds,confirm_add,suspect_add FROM history"
    res = query(sql)
    print(res)
    return res

def get_right1():
    sql = 'SELECT city,confirm FROM ' \
          '(select city,confirm from details  ' \
          'where update_time=(select update_time from details order by update_time desc limit 1) ' \
          'and province not in ("湖北","北京","上海","天津","重庆","香港") ' \
          'union all ' \
          'select province as city,sum(confirm) as confirm from details  ' \
          'where update_time=(select update_time from details order by update_time desc limit 1) ' \
          'and province in ("北京","上海","天津","重庆","香港") group by province) as a ' \
          'ORDER BY confirm DESC LIMIT 5'
    res = query(sql)
    print(res)
    return res

def get_right2():
    sql = "SELECT ds,confirm_add,suspect_add FROM history"
    res = query(sql)
    print(res)
    return res

def get_center2():
    sql = "select province,sum(confirm) from details where update_time =(SELECT update_time FROM details ORDER BY update_time DESC LIMIT 1) GROUP BY province"
    res = query(sql)
    #print(res)
    return res

# 获取center
def get_center1():
    sql = "select sum(confirm),(select suspect from history order by ds  desc limit 1),sum(heal),sum(dead) from details where update_time=(select update_time from details order by update_time desc limit 1)"
    res = query(sql)
    print(res[0])
    return res[0]

#获取系统时间
def get_sys_time():
    # 当前 时间
    dt = time.strftime("%Y-%m-%d %X")
    return dt




