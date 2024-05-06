import kanboard

# Personal API access token: "161879c114609f1674d2cf1f215dfd358501e1bff83613fe8c6fd9cb3309"

# Access the Kanban board
kb = kanboard.Client(url='http://cgi-kanban.nrm.se/jsonrpc.php',
                    username = 'alexyara',
                    password = '161879c114609f1674d2cf1f215dfd358501e1bff83613fe8c6fd9cb3309')

# Fetch all tasks in the "Biodiv projekt" project on Kanban, id = 1
tasks = kb.get_all_tasks(project_id=1, status_id=1)

# Creates the Tasks_class class, 'pass' makes it possible to make it empty
class Tasks_class:
    pass

# The list that will contain all the task objects
task_object_list = []

# Loop through all the tasks fetched from kanban, and filter out the information we need for the web page
for task in tasks:

    # Skip projects that we are not actively working on. 'continue' skips the remaining code of the current iteration, and continues to the next
    if task['color']['name'] != 'Green':
        continue
    
    # Need task id in order to get subtasks
    local_task_id = task['id']
    
    # Make an empty class instance to add dnr and statuses to
    task_object = Tasks_class()
    
    # Adds the whole title (containing the dnr)
    task_object.dnr = task['title']
    
    
    # Get all subtasks for the current task
    subtasks = kb.get_all_subtasks(task_id=local_task_id)
    
    # Filters out the statuses for the task, and adds them to the object created above
    for subtask in subtasks:
        if subtask['title'] == 'Diarienummer':
            task_object.subtask_diarienummer = subtask['status']
            
        if subtask['title'] == 'Rapport':
            task_object.subtask_rapport = subtask['status']
        
        if subtask['title'] == 'Fakturerad':
            task_object.subtask_fakturerad = subtask['status']
    
    # Appends the object to the list
    task_object_list.append(task_object)

print('- - - - - - - - - - - -')

# Export the task_object_list as a CSV file



"""
Statuses:
- Prover mottagna
- DNA extraherad
- Väntar på sekvenscenter
- Analys av data
- Rapportskrivning

Add/Change:
- Mål-DNA amplifierat
- Bibliotek?/Sekvenseringsprepp
- Skickat till sekvenscenter

"""
