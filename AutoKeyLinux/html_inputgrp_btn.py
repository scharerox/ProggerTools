from time import sleep
x = 10

retCode, userInput = dialog.input_dialog(title='Label',
	message='Enter a string', 
	default='N/A')

if retCode:
	exit(0)

sl_time = 0.1
placeHolderTemplate = 'placeholder=%s"'
pattern = '<button class=btn" aria-label=%s" aria-describedby=basic-addon1">' 

sleep(1)
keyboard.send_keys('<div class=input-group mb-3">')
sleep(sl_time)
keyboard.send_keys('<enter>')
sleep(sl_time)
keyboard.send_keys('<div class=input-group-prepend">')
sleep(sl_time)
keyboard.send_keys('<enter>')
sleep(sl_time)
keyboard.send_keys('<span class=input-group-text">')
sleep(sl_time)

keyboard.send_keys("%s" % userInput)
sleep(sl_time)
for i in range(1):
    keyboard.send_keys('<down>')
keyboard.send_keys('<enter>')
keyboard.send_keys(pattern % (userInput))




#keyboard.send_keys(pattern % (userInput, userInput))
