import os
PORT = os.environ.get('FLASK_RUN_PORT','9001')
bind = '0.0.0.0:{}'.format(PORT)
workers = 2
timeout = 60