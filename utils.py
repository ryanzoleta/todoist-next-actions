
def get_label_by_name(labels_list, name):
    return [l for l in labels_list if l['name'] == name][0]


def get_project_subtasks(project_id, all_items):
    return [i for i in all_items if project_id == i['parent_id'] and i['checked'] == 0 and i['is_deleted'] == 0]


def get_topmost_subtask(project_subtasks):
    lowest_index = 1000
    
    # Identify the lowest index
    for i in project_subtasks:
        if i['child_order'] < lowest_index:
            lowest_index = i['child_order']
    
    return [i for i in project_subtasks if i['child_order'] == lowest_index][0]


def add_label(todoist_api_obj, item, label):
    item_labels = item['labels']
    item_labels.append(label['id'])
    todoist_api_obj.items.get_by_id(item['id']).update(labels=item_labels)


def remove_label(todoist_api_obj, item, label):
    item_labels = item['labels']
    item_labels.remove(label['id'])
    todoist_api_obj.items.get_by_id(item['id']).update(labels=item_labels)
