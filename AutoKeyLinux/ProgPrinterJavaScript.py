# Enter script code
import time
date = system.exec_command("date")
author = 'Jonas Ahlf'
creationTimeString = 'Created: ' + date 

def createCommentSection():
    keyboard.send_keys('/*')
    keyboard.send_keys('<enter>')
    keyboard.send_keys(' *')
    keyboard.send_keys(' ')
    
def createAuthor():
    keyboard.send_keys('Initial author: ')
    keyboard.send_keys(author)
    keyboard.send_keys('<enter>')
    keyboard.send_keys(creationTimeString)
    
    
createCommentSection()   
createAuthor()