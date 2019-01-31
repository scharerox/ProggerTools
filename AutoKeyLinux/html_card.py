from time import sleep
x = 10

retCode, userInput = dialog.input_dialog(title='Label',
	message='Enter a string', 
	default='N/A')
	

if retCode:
	exit(0)

sl_time = 0.1

pattern = '<div class=card">' 

sleep(0.5)
keyboard.send_keys('<div class=card">')
keyboard.send_keys('<enter>')
keyboard.send_keys('<a (click)=openPanel(XX)"><h6 class=card-header">%s' % userInput)
for i in range(9):
    keyboard.send_keys('<right>')
keyboard.send_keys('<enter>')
keyboard.send_keys('<div class=card-body" [hidden]=XX">')
keyboard.send_keys('<enter>')
keyboard.send_keys('<div class=container">')
keyboard.send_keys('<enter>')



