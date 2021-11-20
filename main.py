import json
from todoist.api import TodoistAPI


if __name__ == '__main__':

    # Read configuration file
    with open('config.json') as config_file:
        config = json.load(config_file)

    api = TodoistAPI(config['API_KEY'])
    api.sync()
    
    while True:
        print('Initial skeleton')
