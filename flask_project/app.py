from flask import Flask,url_for,render_template,redirect,session,request
import pymysql
import os
# import logging
#
# logging.basicConfig(filename="/var/log/flask_project/log.txt",format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/')
def index():
    if session.get('username'):
        # return "login in"
        return render_template('index.html')
    else:
        return redirect(url_for('login'))

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username == '44084750' and password == 'Zking2002':
            session['username'] = '44084750'
            return render_template('index.html')
        else:
            return redirect(url_for('login'))
# @app.route('/edit')
# def edit():
#     if session.get('username'):
#         return "Modified"
#     else:
#         return redirect(url_for('login'))

# @app.route('/question/<is_login>')
# def question(is_login):
#     if is_login == '1':
#         return render_template('login.html')
#     else:
#         return "This is question page"

# @app.route('/db/')
# def db():
#     session['username'] = '44084750'
#     conn = pymysql.connect(host='130.49.136.103', port=3306, user='test', passwd='1234', db='pexels', charset='utf8')
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM popular_pics")
#     result = cursor.fetchall()
#     conn.close()
#     return render_template('pexels.html',result=result)

# @app.route('/random/<ip>')
# def random(ip):
#     p = os.popen('ping {}'.format(ip))
#     x=p.readlines()
#     return '<br>'.join(x)

# @app.before_first_request
# def my_before_request():
#     print("hello world")
@app.route('/pipeline_configurations/')
def pipeline_configurations():
    if session.get('username'):
        conn = pymysql.connect(host='130.49.136.103', port=3306, user='test', passwd='1234', db='jenkins_configuration',charset='utf8')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pipeline_configurations")
        result = cursor.fetchall()
        conn.close()
        return render_template('pipeline_configurations.html', result=result)
    else:
        return redirect(url_for('login'))

@app.route('/sonarqube_info')
def sonarqube_info():
    if session.get('username'):
        conn = pymysql.connect(host='130.49.136.103', port=3306, user='test', passwd='1234', db='sonarqube_info',charset='utf8')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sonarqube_info")
        result = cursor.fetchall()
        conn.close()
        return render_template('sonarqube_info.html', result=result)
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)