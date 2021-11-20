import json
import time
import logging
import sys
from todoist.api import TodoistAPI
from utils import get_label_by_name, get_project_subtasks, get_topmost_subtask, add_label, remove_label, get_project_tasks


if __name__ == '__main__':

    # Initialize logger
    
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
    root.addHandler(handler)

    filehandler = logging.FileHandler(filename='./app.log')
    filehandler.setLevel(logging.DEBUG)
    filehandler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
    root.addHandler(filehandler)

    logging.info('Script is now running, see app.log to see logging information')
    logging.info('Note: terminating this console window will terminate the script')

    # Read configuration file
    with open('config.json') as config_file:
        config = json.load(config_file)
        API_KEY = config['API_KEY']
        PROJECT_LABEL_TEXT = config['PROJECT_LABEL_TEXT']
        ACTIVE_LABEL_TEXT = config['ACTIVE_LABEL_TEXT']
        PROCESS_ON_PROJECT_LEVEL = config['PROCESS_ON_PROJECT_LEVEL']

        # The above configuration determines which items will be considered as
        # "Projects". Normally, you would have Todoist Projects as Projects.
        # But alternatively, you can set Task Items to be Projects
        # (by setting an @project label on them). If that is the approach you
        # would like to take, then set the above config to 'false'

    api = TodoistAPI(API_KEY)
    api.sync()

    # Retrieve the project and active labels set by the Todoist user

    if not PROCESS_ON_PROJECT_LEVEL:
        try:
            project_label = get_label_by_name(api.state['labels'], PROJECT_LABEL_TEXT)
        except IndexError:
            logging.info('The label "%s" does not exist in your Todoist!' % (PROJECT_LABEL_TEXT))
            exit()
    
    try:
        active_label = get_label_by_name(api.state['labels'], ACTIVE_LABEL_TEXT)
    except IndexError:
        logging.info('The label "%s" does not exist in your Todoist!' % (ACTIVE_LABEL_TEXT))
        exit()

    # Main loop

    while True:
        api.sync()

        # Load all items
        all_items = api.state['items']

        # Load all projects
        if PROCESS_ON_PROJECT_LEVEL:
            all_projects = [p for p in api.state['projects'] if p['is_archived'] == 0 and p['is_deleted'] == 0 and p['name'] != 'Inbox']
        else:
            all_projects = [p for p in all_items if project_label['id'] in p['labels']]

        for project in all_projects:

            # Retrieve first subtask of the project
            if PROCESS_ON_PROJECT_LEVEL:
                project_subtasks = get_project_tasks(project['id'], all_items)
            else:
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
