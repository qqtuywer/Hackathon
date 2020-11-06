from flask import Flask, request
import json
import numpy as np
import time
import os
from flask_cors import *

app = Flask(__name__)
CORS(app, supports_credentials=True)

point_line1=[0,0,0,0,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,
                 0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,
                 0,0,0,0,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,4,
                 0,0,0,0,1,1,1,2,2,2,2,3,3,3,3,3,4,4,4,4,4]
point_bar1=[10,11,11,12]
@app.route("/test_get_CT_V1", methods=["POST"])
def check_CT_V1():
    '''接收一个时间: %Y-%m-%d %H:%M:%S
    :return: a dict
    '''
    response_time = time.strftime('%Y-%m-%d %H:%M:%S')
    return_dict = {'timestamp': response_time, 'message': 'successful!', 'result': 0, 'statusCode': '200'}
    if not request.get_data():
        return_dict['statusCode'] = '5004'
        return_dict['message'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)

    get_data = request.get_data()  # 获取传入的参数
    get_data = json.loads(get_data)
    get_time = get_data.get('time')
    result = test_response_content(get_time)

    return_dict['result'] = result
    return_dict['timestamp'] = get_time
    return json.dumps(return_dict, ensure_ascii=False)


@app.route("/test_get_CT_V2", methods=["POST"])
def check_CT_V2():
    return_dict = {'message': 'fail', 'statusCode': '200', 'result': None}
    if not request.get_data():
        return_dict['statusCode'] = '5003'
        return_dict['result'] = 'no firstframe'
        return json.dumps(return_dict, ensure_ascii=False)

    get_data = request.get_data()  # 获取UI传入的选取目标框的XY坐标
    print(get_data)
    get_data = json.loads(get_data)
    firstframe = get_data.get('firstframe')

    if os.path.exists(firstframe):
        result = video_process(firstframe)
        return_dict['message'] = 'succeed'
        return_dict['result'] = result.tolist()
        return json.dumps(return_dict, ensure_ascii=False)
    else:
        return_dict['result'] = 'not found of the firstframe'
        return_dict['statusCode'] = "5003"
        return json.dumps(return_dict, ensure_ascii=False)


@app.route("/test_upload_video", methods=["POST"])
def check_folder_link():
    return_dict = {'message': 'fail', 'statusCode': '200', 'result': None}
    if not request.get_data():
        return_dict['statusCode'] = '5003'
        return_dict['result'] = 'no folder link'
        return json.dumps(return_dict, ensure_ascii=False)

    get_data = request.get_data()  # 获取传入的参数
    print(get_data)
    get_data = json.loads(get_data)
    print(get_data)
    folder_link = get_data.get('folder_link')

    if os.path.exists(folder_link):
        test_video_split()
        return_dict['message'] = 'succeed'
        return_dict['result'] = 'video processing succeed'
        return json.dumps(return_dict, ensure_ascii=False)
    else:
        return_dict['result'] = 'not found of the folder link'
        return_dict['statusCode'] = "5003"
        return json.dumps(return_dict, ensure_ascii=False)


@app.route("/test_first_frame", methods=["POST"])
def check_first_frame():
    return_dict = {'message': 'fail', 'statusCode': '200', 'result': None}
    if not request.get_data():
        return_dict['statusCode'] = '5003'
        return_dict['result'] = 'not found of the first frame'
        return json.dumps(return_dict, ensure_ascii=False)

    get_data = request.get_data()  # 获取传入的参数
    print(get_data)
    get_data = json.loads(get_data)
    print(get_data)

    return_dict['message'] = 'succeed'
    return_dict['result'] = 'ger first frame succeed'
    return json.dumps(return_dict, ensure_ascii=False)

@app.route("/test_line_bar_data", methods=["POST"])
def check_line_bar_data():
    return_dict = {'message': 'fail', 'statusCode': '200', 'lineData': None,'barData':None}
    if not request.get_data():
        return_dict['statusCode'] = '5003'
        return_dict['result'] = 'not found of line bar data'
        return json.dumps(return_dict, ensure_ascii=False)

    get_data = request.get_data()  # 获取传入的参数
    print(get_data)
    get_data = json.loads(get_data)
    print(get_data)

    return_dict['message'] = 'succeed'
    return_dict['lineData'] = point_line1
    return_dict['barData'] = point_bar1
    return json.dumps(return_dict, ensure_ascii=False)


# 功能函数
def test_response_content(request_time):
    second = request_time[-2:]
    time_range = np.linspace(0, np.pi / 2, 60)
    return np.sin(time_range[int(second)])


def test_video_split():
    pass


def video_process(link):
    '''
    :param link:
    :return:
    '''
    return np.random.randint(1, 50, 10)


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(
        host='10.178.62.36',
        port=50001,
        debug=True
    )
