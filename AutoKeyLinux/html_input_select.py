from time import sleep
x = 10

retCode, userInput = dialog.input_dialog(title='Label',
	message='Enter a string', 
	default='N/A')
	
retCode, elId = dialog.input_dialog(title='Id',
	message='Enter a string', 
	default='cmbX')

if retCode:
	exit(0)

sl_time = 0.1

pattern = '<select id=%s" class=custom-select">' 

sleep(1)
keyboard.send_keys('<div class=input-group mb-3">')
sleep(sl_time)
keyboard.send_keys('<enter>')
sleep(sl_time)
keyboard.send_keys('<div class=input-group-prepend">')
sleep(sl_time)
keyboard.send_keys('<enter>')
sleep(sl_time)
keyboard.send_keys('<label class=input-group-text" for=%s">' % elId)
sleep(sl_time)
keyboard.send_keys("%s" % userInput)
sleep(sl_time)
for i in range(1):
    keyboard.send_keys('<down>')
keyboard.send_keys('<enter>')
keyboard.send_keys(pattern % elId)

