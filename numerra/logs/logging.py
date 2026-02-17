from datetime import datetime

LOG_FILE = 'numerra/logs/numerra.log'

def logging(string: str):
  with open(LOG_FILE, 'a') as file:
    file.write(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] -> {string}\n')
