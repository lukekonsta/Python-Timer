import time
import webbrowser

total_breaks = 3
counter = 0


print("This program has officially started on"+ time.ctime())
while(counter<total_breaks):
    time.sleep(10)
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=tQARCB9wKto")
