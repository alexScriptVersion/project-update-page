import kanboard

# Personal API access token: "161879c114609f1674d2cf1f215dfd358501e1bff83613fe8c6fd9cb3309"

# Access the Kanban board
kb = kanboard.Client(url='http://cgi-kanban.nrm.se/jsonrpc.php',
                    username = 'alexyara',
                    password = '161879c114609f1674d2cf1f215dfd358501e1bff83613fe8c6fd9cb3309')

"""
# Get all projects
projects = kb.get_my_projects()
print(projects)
"""
#print('- - - - - - - - - - - -')
"""
project = kb.get_project_by_id(project_id=1)
print(project)
"""
#print('- - - - - - - - - - - -')

#tasks = kb.get_all_tasks(project_id=1, status_id=1)
#print(tasks)

print('- - - - - - - - - - - -')

subtasks = kb.get_all_subtasks(task_id=315)
print(subtasks)
print('- - - - - - - - - - - -')
print(subtasks[1])

for subtask in subtasks:
    print(subtask)
    print(type(subtask))
    print(subtask['id'])

print('- - - - - - - - - - - -')
"""
task_list = []

for task in tasks:
    task_list.append(task)
    

print(len(task_list))
print(task_list[-1])
"""
"""
Get all tasks
For each task, get all subtasks
Filter out the subtasks that we want
- dnr
- different statuses
Save them in an object representing that task
Append all task objects to a list, which will be the reference for the web page
"""


"""
class Tasks:
    def __init__(self, dnr, subtask_received, subtask_extracted, subtask_sentaway, subtask_analysis):
        self.dnr = dnr
        self.subtask_received = subtask_received
        self.subtask_extracted = subtask_extracted
        self.subtask_sentaway = subtask_sentaway
        self.subtask_analysis = subtask_analysis

"""