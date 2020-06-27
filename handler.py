import json

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123"
)

cur = mydb.cursor()

cur.execute("SHOW DATABASES")
alldb=cur.fetchall()
cur.execute("use student")
print("this works")
def hello(event, context):
    body = {
        "message1" : "he1"
    }
    id="123"
    return {
        "statusCode": 200,
        "body": json.dumps(id)
    }

def hello_post(event, context):
    body={
        "message": event['pathParameters']['num1']
    }
    d1=json.loads(event['body'])

    return {
        "statusCode":200,
        "body": json.dumps(d1)
    }

def get_all(event,context):
    sql = "select * from student_info"

    # val = (u_name,)
    cur.execute(sql)
    data=cur.fetchall()
    return {
        "statusCode":200,
        "body": json.dumps(data)
    }

def get_one(event,context):
    sql = "select * from student_info where name=%s"
    u_name=event['pathParameters']['u_name']
    val = (u_name,)
    cur.execute(sql,val)
    data=cur.fetchall()
    return {
        "statusCode":200,
        "body": json.dumps(data)
    }

def add_record(event,context):
    d1=json.loads(event['body'])
    roll=d1['u_id']
    name=d1['u_name']
    
    sql="insert into student_info values(%s, %s) "
    val=(roll,name)
    cur.execute(sql,val)
    # mysql.connection.commit()
    cur.execute("select * from student_info")
    data=cur.fetchall() 
    return {
        "statusCode":200,
        "body": json.dumps(data)
    }

def modify(event,context):
    d1=json.loads(event['body'])
    id=d1['u_id']
    name=d1['u_name']
    # return '%s' % name
    sql = "select * from student_info where roll_no=%s"
    val=(id,)
    cur.execute(sql,val)
    # cur.execute("select * from student_info")
    # cur.execute( ("select * from student_info where roll_no=%s"), (id) )
    data=cur.fetchall()
    
    r1=cur.rowcount
    # return {
    #         "statusCode":200,
    #         "body": json.dumps(r1)
    #     }
    # return jsonify(r1)

    if r1==0:
        return {
            "statusCode":200,
            "body": json.dumps("id not exist")
        }
    #     # return jsonify('id not exists')

    sql="update student_info set name=%s where roll_no=%s"
    val=(name,id,)

    cur.execute(sql,val)
    # mysql.connection.commit()
    cur.execute("select * from student_info")

    data=cur.fetchall()
    return {
        "statusCode":200,
        "body": json.dumps(data)
    }

def delete(event,context):
    id=event['pathParameters']['u_id']
    sql = "select * from student_info where roll_no=%s"
    val = (id,)
    cur.execute(sql, val)
    d1=cur.fetchall()
    r1 = cur.rowcount

    # return jsonify(r1)
    if r1 == 0:
        return {
            "statusCode":200,
            "body": json.dumps("id not exist")
        }
        # return jsonify('id not exists')
    sql="delete from student_info where roll_no=%s"
    val=(id,)
    cur.execute(sql,val)
    # mysql.connection.commit()
    cur.execute("select * from student_info")
    data=cur.fetchall()
    return {
        "statusCode":200,
        "body": json.dumps(data)
    }








    # body = {
    #     "message": "Go1 Serverless v1.0! Your function executed successfully!",
    #     "input": event
    # }

    # response = {
    #     "statusCode": 200,
    #     "body": json.dumps(body)
    # }
    # print(mydb)
    # res1="hello"
    # return response

    # # Use this code if you don't use the http event with the LAMBDA-PROXY
    # # integration
    # """
    # return {
    #     "message": "Go Serverless v1.0! Your function executed successfully!",
    #     "event": event
    # }
    # """
