import webbrowser
import time

total_breaks = 3
break_count = 0

print("This program started on " + time.ctime())
while break_count < total_breaks:
    time.sleep(60 * 60 * 2)
    webbrowser.open("www.eslhandout.com")
    break_count += 1

# We set the timer to every two hours. 7200 seconds
# Equals two hours 60 * 60 * 2
