name = "Jonas Ahlf"
date = system.exec_command("date")

retCode, userInput = dialog.input_dialog(title='Input required',
	message='Enter a string', 
	default='My string')

if retCode:
	myMessage = 'Dialog exit code was: ' + str(retCode)
	dialog.info_dialog(title='You cancelled the dialog', 
	message=myMessage, width='200') # width is extra zenity parameter 
else:
	dialog.info_dialog(title='The string you entered', message=userInput)  # **