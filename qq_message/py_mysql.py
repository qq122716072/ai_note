import pymysql
import uuid
import time
import datetime

# 特殊字符集
apecial_characters_list = ('🐯', '🇨🇳', '🇩🇪', '🦇', '🎸', '🏀', '🐰', '👿', '🤪', '🐳', '💕')

qq_message_director = 'E:/software/qq/qq/data/process/ML  ApacheCN - 副本.txt'
# qq_message_director = 'E:/software/qq/qq/data/process/hsweb企业后台基础框架.txt'
group_id = 'hsweb企业后台基础框架'
group_name = 'hsweb企业后台基础框架'

db = pymysql.connect(host = "localhost", user = "root", password = "root", db = "qq_message", port = 3306)
cur = db.cursor()


# 插入
sql_insert_qq_account = 'insert into qq_account (id, qq_id, qq_nick_name) values (%s, %s, %s)'
sql_insert_group_account = 'insert into group_account (id, group_id, group_name) values (%s, %s, %s)'
sql_insert_qq_group_relationship = 'insert into qq_group_relationship (id, qq_id, group_id) values (%s, %s, %s)'
sql_insert_qq_group_message_relationship = 'insert into qq_group_message_relationship (id, qq_id, group_id, message_id) values (%s, %s, %s, %s)'
sql_insert_message = 'insert into message (id, message_id, message_receive_date, message_context) values (%s, %s, %s, %s)'


# start = time.clock()
start = datetime.datetime.now()
with open(qq_message_director, 'r', encoding='utf-8', ) as f:

    try:
        cur.execute(sql_insert_group_account, (''.join(str(uuid.uuid4()).split('-')), group_id, group_name))
        for line in f:
            # 如果昵称里面有空格不处理
            arr = line.strip().split(' ')
            if len(arr) != 4:
                print(arr)
                continue
            date, time, qq_nick_name_and_qq_id, message_context = line.strip().split(' ')
            flag = 0
            for e in apecial_characters_list:
                if message_context.find(e) >= 0:
                    print("消息存在特殊字符:" + message_context)
                    flag = 1
                    break
            if (flag == 1):
                flag = 0
                continue
            # 处理qq_id不是(),而是<>
            qq_nick_name = ''
            qq_id = ''
            if qq_nick_name_and_qq_id.find('<') >= 0 and qq_nick_name_and_qq_id.find('>') >= 0:
                qq_nick_name, qq_id = qq_nick_name_and_qq_id.split('<')
                qq_id, _ = qq_id.strip().split('>')
            if qq_nick_name_and_qq_id.find('(') >= 0 and qq_nick_name_and_qq_id.find(')') >= 0:
                if qq_nick_name_and_qq_id.find('(') > 0 or qq_nick_name_and_qq_id.find(')') > 0:
                    print('昵称包含()符号:' + qq_nick_name_and_qq_id)
                    continue
                else:
                    qq_nick_name, qq_id = qq_nick_name_and_qq_id.split('(')
                    qq_id, _ = qq_id.strip().split(')')
            message_reveice_data = date + ' ' + time
            if len(qq_nick_name) == 0:
                qq_nick_name = '-'
            print(qq_id + '-' + qq_nick_name)
            for e in apecial_characters_list:
                if qq_nick_name.find(e) >= 0:
                    print("qq昵称存在特殊字符:" + qq_nick_name)
                    flag = 1
                    break
            if (flag == 1):
                flag = 0
                continue
            cur.execute(sql_insert_qq_account, (''.join(str(uuid.uuid4()).split('-')), qq_id, qq_nick_name))
            cur.execute(sql_insert_qq_group_relationship, (''.join(str(uuid.uuid4()).split('-')), qq_id, group_id))
            message_id = ''.join(str(uuid.uuid4()).split('-'))
            print(qq_id + '-' + group_id + '-' + message_id + '-' + message_context)

            cur.execute(sql_insert_message, (''.join(str(uuid.uuid4()).split('-')), message_id, message_reveice_data, message_context))
            cur.execute(sql_insert_qq_group_message_relationship, (''.join(str(uuid.uuid4()).split('-')), qq_id, group_id, message_id))
            db.commit()

    except Exception as e:
        print(111)
        print(e)
        db.rollback()
    finally:
        db.close()
f.close()

# end = time.clock()
end = datetime.datetime.now()
print(end - start)


# 查询
# sql = 'select * from qq_account'
# try:
#     cur.execute(sql)
#     result = cur.fetchall()
#     print('id', 'qq_id')
#     for row in result:
#         id = row[0]
#         qq_id = row[1]
#         print(id, qq_id)
# except Exception as e:
#     raise e
# finally:
#     db.close()

# def getUUID():
#     return ''.join(str(uuid.uuid4()).split('-'))