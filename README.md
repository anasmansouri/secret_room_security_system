# secret_room_security_system

## 1st step:
il faut creer un environnement de travail pour python
```bash	
	$ python3 -m venv env 
	$ . env/bin/activate
```
 
Et après on Install les package nécessaire
```bash	
	$ pip3 install -r requirements.txt 
```
pour lancer le système de surveillance 
```bash	
	$ cd ./secret_room_seurity_system/Serveur/codes_Python	
	$ python programme_principal.py
```

pour émuler la détection d’une personne avec le capteur de presence 
```bash	
	$ cd ./secret_room_seurity_system/Serveur/emulators
	$ python something_is_detected_by_the_pir.py
```
