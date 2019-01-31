# Enter script code
date = system.exec_command("date")
keyboard.send_keys("Created at:%s" % date)
