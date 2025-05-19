# flask-app

## app.py
Questo codice Python definisce una semplice applicazione web utilizzando Flask, un micro-framework per lo sviluppo web in Python. 

## dockerfile

Questo Dockerfile crea un'immagine Docker per eseguire una semplice applicazione Flask.

- Usa Python 3.8 come base.
- Installa Flask.
- Copia i file dell'app nel container.
- Espone la porta 5000.
- Avvia l'app eseguendo app.py

## jenkinsfile

Questo Jenkinsfile definisce una pipeline CI/CD per automatizzare il processo di build e push di un'immagine Docker della tua applicazione Flask, in base al ramo Git e ai tag.


1. Clona la repository Git

    - Se è presente una variabile TAG, clona quel tag specifico.

    - Altrimenti, clona il ramo indicato (main o develop).

    - Se il ramo non è supportato, mostra un messaggio d’avviso.

2. Login su Docker Hub

    - Usa le credenziali Docker (preconfigurate in Jenkins) per effettuare il login al tuo account Docker Hub.

3. Build & Push dell’immagine Docker

    - In base al ramo, costruisce e invia l'immagine Docker su Docker Hub:

    - main con TAG → push con tag specifico (IMAGE_NAME:TAG)

    - develop → push con tag basato sul commit (IMAGE_NAME:develop-<SHA>)

    - main senza TAG → push come latest (IMAGE_NAME:latest)

    - Se il ramo non è supportato, viene mostrato un messaggio.

