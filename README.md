# 🖧 Socket Client / Serveur en Python
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Sockets](https://img.shields.io/badge/Protocol-Socket-green)
![TCP](https://img.shields.io/badge/Mode-TCP-orange)
![Status](https://img.shields.io/badge/Status-Fonctionnel-brightgreen)

---

## 🎯 Présentation

Ce projet implémente une communication réseau basique via sockets TCP entre un serveur et un client en Python.  

Le serveur crée un socket, se met en écoute sur une adresse IP et un port, puis accepte les connexions entrantes 🌐. 
Le client crée un socket et se connecte au serveur **via IP:port** afin d’établir la communication.  
Les échanges s’effectuent par envoi et réception de messages à l’aide des méthodes ```send()``` et ```recv()``` 📤📥.  

---

## 🧩 Architecture client–serveur classique
```
                +-----------------------+
                |       Serveur         |
                |-----------------------|
                |  socket()             |
                |  bind(127.0.0.1,5000) |
                |  listen()             |
                |  accept() <-----------+
                |  send(time)           |
                |  close()              |
                +-----------+-----------+
                            ^
                            |
                            | Connexion TCP
                            |
                +-----------+-----------+
                |        Client         |
                |-----------------------|
                |  socket()             |
                |  connect(127.0.0.1) -->|
                |  recv(time)           |
                |  print()              |
                |  close()              |
                +-----------------------+
```
---

## ⚙️ Exécution

# ▶️ Lancer le serveur
```
python3 Server.py
```

Le serveur :
- ouvre un socket
- écoute sur un port
- attend une connexion entrante

# ▶️ Lancer le client
```
python3 Client.py
```

Le client :
- se connecte au serveur via IP:port
- envoie un message
- reçoit la réponse

---

## 💬 Exemple d’échange client/serveur
# Côté serveur (console)
```
[+] Serveur démarré sur 127.0.0.1:5000
[+] Client connecté
[>] Envoi de l'heure : 14:32:51
```

# Côté client (console)
```
[>] Connexion au serveur...
[<] Heure reçue : 14:32:51
```

---

## 📈 Diagramme de séquence (Markdown)
```
sequenceDiagram
    participant C as Client
    participant S as Serveur

    C->>S: Connexion TCP (connect)
    S->>S: accept()
    C->>S: send("Bonjour serveur !")
    S->>S: recv()
    S->>C: send("Bien reçu, client.")
    C->>C: recv()
    C-->>S: Fermeture de la connexion
```

---

## 📝 Conclusion
Ce projet constitue une base solide pour comprendre :
- la création et gestion de sockets
- les échanges TCP
- la logique client–serveur
- les fondements des communications réseau
