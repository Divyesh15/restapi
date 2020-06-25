from flask import *
from flask_mysqldb import MySQL
from flask_cors import *
# from functools import update_wrapper
app = Flask(__name__)
# app.config['CORS_ALLOW_HEADERS']="Access-Control-Allow-Origin"

# app.config['CORS_HEADERS'] = 'Content-Type'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123'
app.config['MYSQL_DB'] = 'student'

mysql = MySQL(app)


# def crossdomain(origin=None, methods=None, headers=None, max_age=21600,
#                 attach_to_all=True, automatic_options=True):
#     """Decorator function that allows crossdomain requests.
#       Courtesy of
#       https://blog.skyred.fi/articles/better-crossdomain-snippet-for-flask.html
#     """
#     if methods is not None:
#         methods = ', '.join(sorted(x.upper() for x in methods))
#     # use str instead of basestring if using Python 3.x
#     if headers is not None and not isinstance(headers, basestring):
#         headers = ', '.join(x.upper() for x in headers)
#     # use str instead of basestring if using Python 3.x
#     if not isinstance(origin, basestring):
#         origin = ', '.join(origin)
#     if isinstance(max_age, timedelta):
#         max_age = max_age.total_seconds()
#
#     def get_methods():
#         """ Determines which methods are allowed
#         """
#         if methods is not None:
#             return methods
#
#         options_resp = current_app.make_default_options_response()
#         return options_resp.headers['allow']
#
#     def decorator(f):
#         """The decorator function
#         """
#         def wrapped_function(*args, **kwargs):
#             """Caries out the actual cross domain code
#             """
#             if automatic_options and request.method == 'OPTIONS':
#                 resp = current_app.make_default_options_response()
#             else:
#                 resp = make_response(f(*args, **kwargs))
#             if not attach_to_all and request.method != 'OPTIONS':
#                 return resp
#
#             h = resp.headers
#             h['Access-Control-Allow-Origin'] = origin
#             h['Access-Control-Allow-Methods'] = get_methods()
#             h['Access-Control-Max-Age'] = str(max_age)
#             h['Access-Control-Allow-Credentials'] = 'true'
#             h['Access-Control-Allow-Headers'] = \
#                 "Origin, X-Requested-With, Content-Type, Accept, Authorization"
#             if headers is not None:
#                 h['Access-Control-Allow-Headers'] = headers
#             return resp
#
#         f.provide_automatic_options = False
#         return update_wrapper(wrapped_function, f)
#     return decorator








tasks = [
    {
        'user_id': 'u1',
        'user_name': 'user name 1'

    }
]
# CORS(app, resources={r"/*": {"origins": "*"}})
# CORS()
CORS(app, resources={r"/user": {"origin": "http://localhost:3000"}})
# app.config['CORS_HEADERS'] = 'Content-Type'

# app.config['CORS_HEADERS'] = 'Content-Type'

# CORS(app, resources={r"/user": {"origins": "http://localhost:3000"}})
# cors=CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
#
# @app.after_request
# def after_request(response):
#   response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
#   # response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#   # response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
#   response.headers.add('Access-Control-Allow-Credentials', 'true')
#   return response
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response


@app.route('/',methods=['GET'])
# @cross_origin()
def hello_world():
    # cur = mysql.connection.cursor()
    # cur.execute("show databases")
    # data=cur.fetchall()
    # return jsonify(data)
    val='hello'
    return jsonify(val)
@app.route('/all', methods=['GET'])
# @cross_origin()
def fetch1():
    cur = mysql.connection.cursor()
    # cur.execute("use student")
    sql = "select * from student_info"

    # val = (u_name,)
    cur.execute(sql)
    data=cur.fetchall()

    return jsonify(data)


@app.route('/user/<u_name>', methods=['GET'])
# @cross_origin()
def fetch(u_name):
    cur = mysql.connection.cursor()
    # cur.execute("use student")
    sql = "select * from student_info where name=%s"

    val = (u_name,)
    cur.execute(sql,val)
    data=cur.fetchall()

    return jsonify(data)

    # task = [task for task in tasks if task['user_id'] == u_name]
    # if len(task) == 0:
    #     return 'user Not Found'
    # return jsonify(task[0])

    # if u_name in record:
    #     return jsonify(record[u_name])
    # else:
    #     return 'User Not Found'

#
@app.route('/user', methods=['POST','OPTIONS'])
# @cross_origin(allow_headers=['Content-Type'])
# @cross_origin(origin='http://localhost:3000',headers=['Access-Control-Allow-Origin'])
# @cross_origin()
# @crossdomain(origin='*')
def add():
    if not request.json:
        return jsonify('Please provide record')
    # return "success"
    cur = mysql.connection.cursor()

    roll=request.json['user_id']
    name=request.json['user_name']
    sql="insert into student_info values(%s, %s) "
    val=(roll,name)
    cur.execute(sql,val)
    # mysql.connection.commit()
    cur.execute("select * from student_info")
    data=cur.fetchall()
    # resp = Flask.Response("hello")
    # resp.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
    # return resp
    # response = Flask.jsonify(data)
    # response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
    # return response

    # return jsonify(data)
    return jsonify('Success')


    # r1 = {
    #     'user_id': request.json['user_id'],
    #     'user_name': request.json['user_name']
    # }
    # tasks.append(r1)

    # return jsonify(tasks)


@app.route('/user/update',methods=['PUT'])
def modify():
    if not request.json:
        return jsonify('please provide details')
    # return 'success'
    cur=mysql.connection.cursor()
    id=request.json['user_id']
    name=request.json['user_name']
    # return '%s' % name
    sql = "select * from student_info where name=%s"
    val=(name,)
    cur.execute(sql,val)
    # cur.execute( ("select * from student_info where roll_no=%s"), (id) )
    # data=cur.fetchall()
    r1=cur.rowcount

    # return jsonify(r1)
    if r1==0:
        return jsonify('id not exists')

    sql="update student_info set name=%s where roll_no=%s";
    val=(name,id,)

    cur.execute(sql,val)
    # mysql.connection.commit()
    cur.execute("select * from student_info")

    data=cur.fetchall()
    # return jsonify(data)
    return jsonify('Success')


    # return 'id =%d' % id

@app.route('/user/delete/<int:id>', methods=['DELETE'])
def delete(id):
    cur = mysql.connection.cursor()
    sql = "select * from student_info where roll_no=%s"
    val = (id,)
    cur.execute(sql, val)

    r1 = cur.rowcount

    # return jsonify(r1)
    if r1 == 0:
        return jsonify('id not exists')
    sql="delete from student_info where roll_no=%s"
    val=(id,)
    cur.execute(sql,val)
    # mysql.connection.commit()
    cur.execute("select * from student_info")
    data=cur.fetchall()
    # return jsonify(data)
    return jsonify('success')



#
# @app.route('/h1/<int:n1>')
# def h1(n1):
#     return "this is from %d" % n1

# @app.route('/login',methods=['POST','GET'])
# def login():
#     return 'welcome'
#     # if request.method=='POST':
#     #     user=request.form['name']
#     #     return redirect(url_for('success',name=user))
#     # else:
#     #     user=request.args.get('name')
#     #     return redirect(url_for('success',name=user))
#
# @app.route('/success/<name>')
# def success(name):
#     return 'Welcome %s' % name

if __name__ == '__main__':
    app.debug = True
    app.run()
    # app.run(debug=True)
