# I created a file Mobydick.txt in my repository pands-weekly-tasks
link = "https://github.com/quyenphanlyons/pands-weekly-tasks/blob/main/Mobydick.txt"

# Open file in python - Source stackoverflow.com
from urllib.request import urlopen
data = urlopen(link).read().decode('utf-8')
data.count('e')

