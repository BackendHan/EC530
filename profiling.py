# profiling.py

import cProfile
import pstats
from app import app
from memory_profiler import profile

with app.test_request_context():
    cProfile.run('app.test_client().post("/train", data={})', 'train_profile')

stats = pstats.Stats('train_profile')
stats.sort_stats('cumulative').print_stats(10)

@profile
def train():
    # 调用训练函数
    app.test_client().post('/train', data={})

train()