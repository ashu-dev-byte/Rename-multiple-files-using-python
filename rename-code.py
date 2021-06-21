# For renaming multiple files from a list of names
import os


# reading names from a txt file and storing it in a list 
try:
  file = open('<Filename.txt>', 'r')
  name_list = []

  for line in file:
      name_list.append(line.strip())

except:
  print("An error occured while reading names")

finally:
  file.close()

  
# renaming all the files in the provided directory
try:
  for filename in os.listdir("<directory-name>"):
    temp = int(filename.split(".")[0].split("<prefix>").pop())
    src = "<directory-name>/" + filename
    dst = "<directory-name>/" + str(temp) + ". " + name_list[temp-1] + ".mp4"
    os.rename(src, dst)

except:
  print("An error occured while renaming files")  
