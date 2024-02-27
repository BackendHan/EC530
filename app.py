import logging
from flask import Flask

from models import db, User, Project

from flask import Flask, request, jsonify

from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'  # 使用你想要的数据库文件
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 可选，用来禁用 Flask-SQLAlchemy 的事件系统
# 设置日志记录
logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
db.init_app(app)


@app.before_request
def create_tables():
    db.create_all()


@app.route('/')
def home():
    app.logger.info('主页被访问')
    return "Welcome to my Flask app!"


@app.route('/upload', methods=['POST'])
def upload_file():
    # 伪代码，返回成功响应
    return jsonify({"message": "File uploaded successfully", "status": "success"}), 200


@app.route('/train', methods=['POST'])
def train_model():
    # 伪代码，返回成功响应
    return jsonify({"message": "Model training initiated", "status": "success"}), 200


if __name__ == '__main__':
    app.run(debug=True)
