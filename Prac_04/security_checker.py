"""
CP1404 Prac
security_checker
"""

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


username = input("Username: ")
if username in usernames:
    print("Access granted")
else: print("Access Denied")