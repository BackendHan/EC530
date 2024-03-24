import logging
from flask import Flask, request, jsonify
from celery.result import AsyncResult
from celery_worker import process_inference_request, process_training_request
from models import db, User, Project

from flask import Flask, request, jsonify

from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'  # 使用你想要的数据库文件
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 可选，用来禁用 Flask-SQLAlchemy 的事件系统
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
# 设置日志记录
logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
db.init_app(app)

@app.route('/inference', methods=['POST'])
def inference():
    # 获取请求数据
    data = request.get_json()
    task = process_inference_request.delay(data)
    return jsonify({'task_id': task.id}), 202

@app.route('/training', methods=['POST'])
def training():
    data = request.get_json()
    task = process_training_request.delay(data)
    return jsonify({'task_id': task.id}), 202

@app.route('/status/<task_id>', methods=['GET'])
def get_status(task_id):
    task = AsyncResult(task_id)
    return jsonify({'status': task.status})

if __name__ == '__main__':
    app.run(debug=True)
