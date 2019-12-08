from flask import jsonify
# 构建请求响应体，用于返回请求的数据
class ResultResp():
    status = 200
    msg = ''
    data = None

    def __init__(self,status, msg, data):
        self.status = status
        self.msg = msg
        self.data = data

    def to_resp(self):
        return jsonify({
            'status':self.status,
            'msg': self.msg,
            'data': self.data
        })