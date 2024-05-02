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

#tasks = kb.get_all_tasks(project_id=1, status_id=0)
#print(tasks)

print('- - - - - - - - - - - -')

subtasks = kb.get_all_subtasks(task_id=315)
print(subtasks)

class Tasks:
    def __init__(self, dnr, subtask_received, subtask_extracted, subtask_sent-away, subtask_analysis):
        self.dnr = dnr
        self.subtask_received = subtask_received
        self.subtask_extracted = subtask_extracted
        self.subtask_sent-away = subtask_sent-away
        self.subtask_analysis = subtask_analysis

