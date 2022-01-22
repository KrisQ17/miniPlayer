import os
os.system("python manage.py loaddata fixtures/users.json")
os.system("python manage.py loaddata fixtures/videos.json")