import os

counter = 300

total_files = len([name for name in os.listdir('D:\data')])
progress = (counter/total_files) * 100

print(f"{round(progress, 2)}%")
