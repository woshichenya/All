#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 导入pymysql模块
import pymysql
import redis

MYSQL_PARAMS = {
    'host':'47.93.51.52',
    'port':3306,
    'user':'root',
    'passwd':'LOfs4xdVYw',
    'db':'ceshi',
    'charset':'utf8'
}

REDIS_PARAMS = {
    'host':'127.0.0.1',
    'port':'6379',
    'password': 'wdtx@2018',
    'db': '2'
}

# 连接数据库
def get_db_cursor():
    conn=pymysql.connect(**MYSQL_PARAMS)
    cursor = conn.cursor()
    return {'conn':conn,'cursor':cursor}
    pass

# 断开数据库链接
def bread_db_cursor(conn,cursor):
    cursor.close()
    conn.close()
    pass

# redis连接
def get_redis():
    re=redis.Redis(host=REDIS_PARAMS['host'], port=REDIS_PARAMS['port'],db=REDIS_PARAMS['db'],password=REDIS_PARAMS['password'])
    return re
    pass



# 获取所有用户
def get_all_customer(cursor):
    sql = "select uid from ims_users"
    ret = cursor.execute(sql)
    datasall = cursor.fetchall()
    return datasall
    pass

# 获取所有 uniacid对应用户id
def get_all_uniacid(cursor):
    sql = "select uniacid,uid from ims_uni_account_users where role='owner'"
    ret = cursor.execute(sql)
    datasall = cursor.fetchall()
    return datasall
    pass


# 解析用户id和域名
def resolve_user(user_arr):
    user_list = {}
    for uid in user_arr:
        # 偶数
        if uid[0] % 2 == 0 :
            user_list[uid[0]] = '127.0.0.1:8084'
        else:
            user_list[uid[0]] = '127.0.0.1:8085'
    return user_list
    pass


# 将数据存入 redis
def put_info_to_redis(re,user_list):
    for users in user_list:
        re.hset('customer_url',users,user_list[users])
    pass


# 将 uniacid 存入 redis
def put_uniacid_to_redis(re,uni_uid_arr):
    for uni_uid in uni_uid_arr:
        re.hset('uniacid_uid',uni_uid[0],uni_uid[1])
    pass


# 客户id 绑定用户域名 redis
if __name__ == '__main__':
    # 连接数据库
    db = get_db_cursor()
    
    # 连接redis
    re = get_redis()
    

    # 获取所有用户
    user_arr = get_all_customer(db['cursor'])

    # 解析用户和域名
    user_arr_rs = resolve_user(user_arr)

    # 将数据存入redis
    put_info_to_redis(re,user_arr_rs)


    # 获取 uniacid 对应用户
    uni_uid_arr = get_all_uniacid(db['cursor'])

    # 将 uniacid 存入 redis
    put_uniacid_to_redis(re,uni_uid_arr)

    # 将数据存入redis
    bread_db_cursor(db['conn'],db['cursor'])

    print('处理完成')
    pass

