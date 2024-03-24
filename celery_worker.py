from celery import Celery

app = Celery('celery_worker')
app.config_from_object('celery_config')

@app.task
def process_inference_request(data):
    # 推理请求处理逻辑
    pass

@app.task
def process_training_request(data):
    # 训练请求处理逻辑
    pass
