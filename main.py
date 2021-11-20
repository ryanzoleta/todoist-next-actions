import json
import time
import logging
from todoist.api import TodoistAPI
from utils import get_label_by_name, get_project_subtasks, get_topmost_subtask, add_label, remove_label


if __name__ == '__main__':

    print('Script is now running, see app.log to see logging information')
    print('Note: terminating this console window will terminate the script')

    # Read configuration file
    with open('config.json') as config_file:
        config = json.load(config_file)
        API_KEY = config['API_KEY']
        PROJECT_LABEL_TEXT = config['PROJECT_LABEL_TEXT']
        ACTIVE_LABEL_TEXT = config['ACTIVE_LABEL_TEXT']

    api = TodoistAPI(API_KEY)
    api.sync()

    project_label = get_label_by_name(api.state['labels'], PROJECT_LABEL_TEXT)
    active_label = get_label_by_name(api.state['labels'], ACTIVE_LABEL_TEXT)

    while True:
        logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

        api.sync()

        # Load all items
        all_items = api.state['items']

        # Load all projects
        all_projects = [p for p in all_items if project_label['id'] in p['labels']]

        for project in all_projects:

            # Retrieve first subtask of the project
            project_subtasks = get_project_subtasks(project['id'], all_items)

            if len(project_subtasks) > 0:
                first_item = get_topmost_subtask(project_subtasks)

                # Adds an @active label to the first subtask of the project if none exists yet
                if active_label['id'] not in first_item['labels'] and first_item['due'] is None:
                    logging.info('Adding @active to : "%s" (%s)' % (first_item['content'], first_item['id']))
                    add_label(api, first_item, active_label)

        if len(api.queue):
            api.commit()

        time.sleep(3)
