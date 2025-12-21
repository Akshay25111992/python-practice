# Using datetime, add a week and 12 hours to a date.
# Given date: March 22, 2020, at 10:00 AM.
# Print original date time and new date time.

from datetime import datetime, timedelta

original_date = datetime(2020, 3, 22, 10, 0, 0)
new_date = original_date + timedelta(weeks=1, hours=12)
print(f"Original date time: {original_date}")
print(f"New date time: {new_date}")


# Code to get the dates of yesterday, today, and tomorrow.

today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print(f"Yesterday: {yesterday}")
print(f"Today: {today}")
print(f"Tomorrow: {tomorrow}")


# Write a code snippet using os module, to get the current working directory and print
# and create a folder "test". List all the files and folders in the current working directory
# and remove the directory "test" that was created.

import os

current_dir = os.getcwd()
print(f"Current working directory: {current_dir}")

os.mkdir("test")
print("Folder 'test' created")

files_and_folders = os.listdir(current_dir)
print(f"Files and folders: {files_and_folders}")

os.rmdir("test")
print("Folder 'test' removed")


# Write a Python program to rename a file from old_name.txt to new_name.txt.

# Create old_name.txt first
with open("old_name.txt", "w") as f:
    f.write("Sample content")

os.rename("old_name.txt", "new_name.txt")
print("File renamed from old_name.txt to new_name.txt")

# Clean up
os.remove("new_name.txt")


# Create a file and Write a Python program to get the size of a file named example.txt

with open("example.txt", "w") as f:
    f.write("This is an example file with some content.")

file_size = os.path.getsize("example.txt")
print(f"Size of example.txt: {file_size} bytes")

# Clean up
os.remove("example.txt")


# Convert the string "Feb 25 2020 4:20PM" into a Python datetime object
# O/P: 2020-02-25 16:20:00

date_string = "Feb 25 2020 4:20PM"
date_object = datetime.strptime(date_string, "%b %d %Y %I:%M%p")
print(date_object)


# Subtract 7 days from the date 2025-02-25 and print the result.
# O/P: New date: 2025-02-18

date = datetime(2025, 2, 25)
new_date = date - timedelta(days=7)
print(f"New date: {new_date.date()}")


# Format the date 2020-02-25 as "Tuesday 25 February 2020"

date = datetime(2020, 2, 25)
formatted_date = date.strftime("%A %d %B %Y")
print(formatted_date)

