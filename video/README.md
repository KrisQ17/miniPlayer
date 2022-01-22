# miniPlayer

Projekt na zaliczenie Django

### Importowanie danych do bazy
- w folderze fixtures znajdują się pliki json, w których znajdują się dane testowe
- aby zaimportować dane należy ze ścieżki gdzie jest plik "manage.py" wykonać skrypt fixtures/load.py

### Dane testowe
Każdy użytkownik loguje się do portalu za pomocą loginu dostępnego w bazie danych oraz hasła w md5.  
Hasło dla każdego użytkownika jest takie same: miniplayer_user.