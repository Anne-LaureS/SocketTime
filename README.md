# Socket Client / Serveur Python

Ce projet implémente une communication réseau basique via sockets TCP en Python.  
Le serveur crée un socket, se met en écoute sur une adresse IP et un port, puis accepte les connexions entrantes.  
Le client crée un socket et se connecte au serveur via IP:port.  
Les échanges se font par envoi et réception de messages avec `send()` et `recv()`.  
Architecture client–serveur classique à but pédagogique.
