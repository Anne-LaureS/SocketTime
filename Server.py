import socket

# Configuration du serveur
ipServer = "127.0.0.1"
portServer = 12345

# Création du socket serveur
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((ipServer, portServer))
serverSocket.listen(5)

print(f"🟢 Serveur en écoute sur {ipServer}:{portServer}")
print("En attente de connexion client...\n")

# Accepter une connexion client
clientSocket, addr = serverSocket.accept()
print(f"✅ Client connecté depuis {addr[0]}:{addr[1]}")
print("=" * 50)

# Boucle de communication continue
while True:
    try:
        # Recevoir le message du client
        data = clientSocket.recv(1024)
        
        # Si pas de données, le client s'est déconnecté
        if not data:
            print("\n❌ Client déconnecté")
            break
        
        # Décoder le message
        messageLisible = data.decode().strip()
        
        # Afficher le message reçu
        print(f"📨 Client: {messageLisible}")
        
        # Vérifier si le client veut quitter
        if messageLisible.lower() == "exit":
            print("\n🔴 Le client a demandé la fermeture de la connexion")
            messageConfirmation = "Au revoir ! Connexion fermée."
            clientSocket.send(messageConfirmation.encode())
            break
        
        # Demander la réponse du serveur
        reponse = input("📤 Serveur: ")
        
        # Envoyer la réponse au client
        clientSocket.send(reponse.encode())
        
        # Si le serveur tape "exit", fermer la connexion
        if reponse.lower() == "exit":
            print("\n🔴 Serveur ferme la connexion")
            break
            
    except Exception as e:
        print(f"\n⚠️ Erreur: {e}")
        break

# Fermer les sockets
clientSocket.close()
serverSocket.close()
print("\n✅ Serveur arrêté")