import kanboard
#from kanboard.task import Task

# Access the Kanban board
"""
1)
board = kanboard.Kanboard('http://localhost:8080/jsonrpc.php',
                          '347a020cb5ce709441aa42b2d5652fbb8b02e477104d1d9789f7b2d40df0')

2)
kb = kanboard.Client('http://localhost/jsonrpc.php', 'admin', 'secret')

3)
kb = kanboard.Client(url='https://example.org/jsonrpc.php',
                     username='admin',
                     password='secret',
                     cafile='/path/to/my/cert.pem')

4) Not secure?
kb = kanboard.Client(url='https://example.org/jsonrpc.php',
                     username='admin',
                     password='secret',
                     insecure=True)
"""

# my personal API access token: "161879c114609f1674d2cf1f215dfd358501e1bff83613fe8c6fd9cb3309"

# I am not getting access

kb = kanboard.Client(url='http://cgi-kanban.nrm.se/jsonrpc.php',
                    username = 'alexyara',
                    password = '161879c114609f1674d2cf1f215dfd358501e1bff83613fe8c6fd9cb3309')


"""
board = kanboard.Kanboard('http://cgi-kanban.nrm.se/jsonrpc.php', 
                            '161879c114609f1674d2cf1f215dfd358501e1bff83613fe8c6fd9cb3309')

project = board.get_project_by_name('Biodiv projekt')
print(project)
"""
#print(kb)
projects = kb.get_my_projects()
print(projects)

print(help(kanboard))

#project = kb.get_project_by_id(1)
#print(project)

#tasks = project.get_all_tasks()

#for task in tasks:
#    print(task.title)