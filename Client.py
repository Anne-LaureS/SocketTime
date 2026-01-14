import socket

# Configuration de connexion au serveur
ipServer = "127.0.0.1"
portServer = 12345

# Création du socket client
socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connexion au serveur
    socketClient.connect((ipServer, portServer))
    print(f"✅ Connecté au serveur {ipServer}:{portServer}")
    print("=" * 50)
    print("💬 Vous pouvez maintenant dialoguer avec le serveur")
    print("ℹ️  Tapez 'exit' pour quitter")
    print("=" * 50 + "\n")
    
    # Boucle de communication continue
    while True:
        # Demander le message à envoyer
        message = input("📤 Vous: ")
        
        # Envoyer le message au serveur
        messageEncode = message.encode()
        socketClient.send(messageEncode)
        
        # Si l'utilisateur tape "exit", quitter après réception de la confirmation
        if message.lower() == "exit":
            data = socketClient.recv(1024)
            messageRecu = data.decode()
            print(f"📨 Serveur: {messageRecu}")
            print("\n🔴 Déconnexion...")
            break
        
        # Recevoir la réponse du serveur
        data = socketClient.recv(1024)
        
        # Si pas de données, le serveur s'est déconnecté
        if not data:
            print("\n❌ Serveur déconnecté")
            break
        
        # Décoder et afficher la réponse
        messageRecu = data.decode()
        print(f"📨 Serveur: {messageRecu}")
        
        # Si le serveur a envoyé "exit", quitter
        if messageRecu.lower() == "exit":
            print("\n🔴 Le serveur a fermé la connexion")
            break

except ConnectionRefusedError:
    print("❌ Erreur: Impossible de se connecter au serveur")
    print("   Assurez-vous que le serveur est lancé")
except Exception as e:
    print(f"⚠️ Erreur: {e}")
finally:
    # Fermer le socket
    socketClient.close()
    print("\n✅ Client déconnecté")