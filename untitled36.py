from flask import Flask
from flask import render_template
import utils
from flask import jsonify
from flask import request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/test1')
def test1():
    return render_template("test1.html")

@app.route('/get_left1',methods=['get','post'])
def get_left1():
    res = utils.get_left1()
    day,confirm,suspect,heal,dead = [],[],[],[],[]
    for tup in res:
        day.append(tup[0].strftime("%m-%d"))
        confirm.append(tup[1])
        suspect.append(tup[2])
        heal.append(tup[3])
        dead.append(tup[4])
    return jsonify({"day":day,"confirm":confirm,"suspect":suspect,"heal":heal,"dead":dead})

@app.route('/get_left2',methods=['get','post'])
def get_left2():
    res = utils.get_left2()
    day,confirm,suspect = [],[],[]
    for item in res:
        day.append(item[0].strftime("%m-%d"))
        confirm.append(item[1])
        suspect.append(item[2])
    return jsonify({"day":day,"confirm":confirm,"suspect":suspect})


@app.route('/get_right1',methods=['get','post'])
def get_right1():
    res = utils.get_right1()
    city,confirm = [],[]
    for item in res:
        city.append(item[0])
        confirm.append(str(item[1]))
    return jsonify({"city":city,"confirm":confirm})



@app.route('/get_right2',methods=['get','post'])
def get_right2():
    res = utils.get_right2()
    day,confirm_add,suspect_add = [],[],[]
    for item in res:
        day.append(item[0].strftime("%m-%d"))
        confirm_add.append(item[1])
        suspect_add.append(item[2])
    return jsonify({"day":day,"confirm_add":confirm_add,"suspect_add":suspect_add})


@app.route('/get_center2',methods=['get','post'])
def get_center2():
    datas = []
    res = utils.get_center2()
    for item in res:
        datas.append({"name":item[0],"value":str(item[1])})
    return jsonify({"data":datas})

@app.route('/get_center1',methods=['get','post'])
def get_center1():
    #获取数据库中我想要的数据
    res = utils.get_center1()
    #把数据转换为json字符串
    return jsonify({"confirm":str(res[0]),"suspect":str(res[1]),"heal":str(res[2]),"dead":str(res[3])})

@app.route('/get_sys_time',methods=['get','post'])
def get_sys_time():
    dt = utils.get_sys_time()
    return dt

if __name__ == '__main__':
    app.run()
