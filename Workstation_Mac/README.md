# Step 1 - Workstation Mac

Progetto per automatizzare il più possibile l'installazione tramite **Ansible** e **Vagrant** di un Docker Master ed un Agent **Jenkins**.

---

## File del progetto

### `Vagrantfile`

Definisce la configurazione della VM:
- Definisce la network con IP statico `192.168.33.61`
- Specifica l'uso di **Ansible** per il provisioning.

### `playbook.yml`

1. Aggiorna i pacchetti.
2. Mi assicuro che sia installato **pip** e il modulo di Python **request**.
3. Installo **Docker** e avvia il servizio.
4. Creo una **Docker Network** dedicata.
5. Eseguo un container **Jenkins Master** configurato per l'accesso sulle porte `8080` e `50000`.
6. Eseguo un container **Jenkins Agent**, connesso al Master.
7. Vado a configurare i container inserendo il sudo, il docker.
8. Inserisco l'utente nel gruppo docker.
9. Cambio il **chown** del file Sock.

---

## Le seguenti operazioni vanno effettuate a mano e non sono automatizzabili.

1. ### Creazione di un Nodo su jenkins. 
- Vai su **Gestisci Jenkins > Nodes > New Node**.
- Inserisci un nome per il nodo (es. `docker-agent`).
- Configura i dettagli del nodo.
- Salva il nodo e nella schermata del nodo appena creato, copia il `SECRET`.

2. ### Inserimento Secret
- Nel file `playbook.yaml`, sostituisci il valore di `JENKINS_SECRET` nella sezione env dell'Agent:
   ```bash
     JENKINS_SECRET: "SECRET" 
   ```
---

**Clona questo repository sul tuo computer.**
   ```bash
   git clone https://github.com/Ludovico1997/formazione_sou_k8s/Workstation_Mac
   ```

