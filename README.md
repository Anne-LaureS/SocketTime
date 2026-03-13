# 🖧 Socket Client / Serveur en Python
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Sockets](https://img.shields.io/badge/Protocol-Socket-green)
![TCP](https://img.shields.io/badge/Mode-TCP-orange)
![Status](https://img.shields.io/badge/Status-Fonctionnel-brightgreen)

---

## 🎯 Présentation

Ce projet illustre une communication réseau simple en **TCP** entre un serveur et un client Python.

- Le **serveur** Le serveur écoute sur **127.0.0.1:5000** et envoie l’heure courante au client.
  
- Le client se connecte, reçoit l’heure, l’affiche, puis ferme la connexion.

---

## 🧩 Architecture client–serveur classique
```
                +-----------------------+
                |       Serveur         |
                |-----------------------|
                |  socket()             |
                |  bind(127.0.0.1:5000) |
                |  listen()             |
                |  accept() <-----------+
                |  send(time)           |
                |  close()              |
                +-----------+-----------+
                            ^
                            |
                            | Connexion TCP
                            |
                +-----------+-----------------+
                |           Client            |
                |-----------------------------|
                |  socket()                   |
                |  connect(127.0.0.1:5000) -->|
                |  recv(time)                 |
                |  print()                    |
                |  close()                    |
                +-----------------------------+
```
---

## ⚙️ Exécution

# ▶️ Lancer le serveur
```
python3 Server.py
```

# Sortie
```
Serveur en écoute sur 127.0.0.1:5000
Client connecté
Heure envoyée : 14:32:51
```

# ▶️ Lancer le client
```
python3 Client.py
```

# Sortie
```
Connexion au serveur...
Heure reçue : 14:32:51
```

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
