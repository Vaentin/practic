from importlib.metadata import files
import os
import time
spisok = []
# for adress, dirs, files in os.walk('C:\\Users\Laptop\Documents\Devops\Git'):
#     spisok.append(adress)

# for adress, dirs, files in os.walk('C:\\Users\Laptop\Documents\Devops\Git'):
#     for file in files:
#         spisok.append(os.path.join(adress,file))

for adress, dirs, files in os.walk('C:\\Users\Laptop\Documents\Devops\Git'):
     for file in files:
        full = os.path.join(adress,file)
        if time.time() - os.path.getctime(full) < 86400:
            spisok.append(full)

print(spisok)
    