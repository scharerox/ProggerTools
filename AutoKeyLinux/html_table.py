from time import sleep

sl_time = 0.1

pat_head = '<table class=table table-striped">' 
pat_thead = '<thead>'
pat_tr = '<tr>'
pat_th = '<th>'
pat_td = '<td>'
pat_thead_end = '</thead>'
pat_tr_end = '</tr>'
pat_th_end = '</th>'
pat_td_end = '</td>'
pat_head_end = '</table>'

sleep(0.2)
keyboard.send_keys(pat_head)
keyboard.send_keys('<enter>')
keyboard.send_keys(pat_thead)
keyboard.send_keys('<enter>')
keyboard.send_keys(pat_tr)
keyboard.send_keys('<enter>')
keyboard.send_keys(pat_th)
keyboard.send_keys('<down>')
keyboard.send_keys('<down>')
keyboard.send_keys('<right>')
keyboard.send_keys('<right>')
keyboard.send_keys('<enter>')
keyboard.send_keys('<tbody>')
keyboard.send_keys('<enter>')
keyboard.send_keys(pat_tr)
keyboard.send_keys('<enter>')
keyboard.send_keys(pat_td)


#keyboard.send_keys(pattern % (userInput, userInput))
