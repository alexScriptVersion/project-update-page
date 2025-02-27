import kanboard
import csv
import json

# Personal API access token: "161879c114609f1674d2cf1f215dfd358501e1bff83613fe8c6fd9cb3309"

# Access the Kanban board
kb = kanboard.Client(url='http://cgi-kanban.nrm.se/jsonrpc.php',
                    username = 'alexyara',
                    password = '161879c114609f1674d2cf1f215dfd358501e1bff83613fe8c6fd9cb3309')

# Fetch all tasks in the "Biodiv projekt" project on Kanban, id = 1
tasks = kb.get_all_tasks(project_id=1, status_id=1)
columns = kb.get_columns(project_id=1)


for column in columns:
    print(column)
    print("- - - -")

# id 1 = Incoming
# id 2 = To be started
# id 176 = On going
# id 134 = Lab-work done
# id 177 = In analysis
# id 3 = Finished projects
# id 4 = Invoiced projects

# Empty list that will contain all the filtered tasks. Each task will be a dictionary and have its dnr number and column id
list_of_filtered_tasks = []

# Loop through all the tasks fetched from kanban, and filter out the information we need for the web page
for task in tasks:
    
    # Skip projects that we are not actively working on. 'continue' skips the remaining code of the current iteration, and continues to the next
    if task['color']['name'] != 'Green':
        continue
    
    # Adds the whole title (containing the dnr) to 'dnr_string', but first remove all commas (to not disturb in the csv file later)
    # filter out only the dnr number. Demand: 1) the dnr needs to be at the end, and 2) have a colon ('dnr:')
    dnr_string = task['title'].replace(',', '').lower()
    dnr_index = dnr_string.rfind('dnr:') + 4
    dnr = dnr_string[dnr_index:].strip()
    #print(dnr)
    
    # get the column id of the task
    column_id = task['column_id']
    #print(column_id)
    
    current_task_dictionary = {'dnr': dnr, 'column_id': column_id}
    
    list_of_filtered_tasks.append(current_task_dictionary)

#print(list_of_filtered_tasks)
print('- - - - - - - - - - - -')

with open("data.json", "w") as j:
    json.dump(list_of_filtered_tasks, j)

"""
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
    
    # Adds the whole title (containing the dnr) to 'dnr_string', but first remove all commas (to not disturb in the csv file later)
    # filter out only the dnr number. Demand: 1) the dnr needs to be at the end, and 2) have a colon ('dnr:')
    dnr_string = task['title'].replace(',', '').lower()
    dnr_index = dnr_string.rfind('dnr:') + 4
    dnr = dnr_string[dnr_index:].strip()
    
    task_object.dnr = dnr
    
    
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
"""
"""
# Export the task_object_list as a CSV file
csv_fields = ['dnr_string', 'Diarienummer', 'Rapport', 'Fakturerad'] 
"""
"""
with open('task_statuses', 'w', newline='') as csvfile:
    # csv.writer() method
    write = csv.writer(csvfile)
    write.writerow(csv_fields)
    
    for object in task_object_list:
        write.writerow([
        object.dnr, 
        object.subtask_diarienummer, 
        object.subtask_rapport, 
        object.subtask_fakturerad
        ])

"""
"""
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump([ob.__dict__ for ob in task_object_list], f, ensure_ascii=False)
"""

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
