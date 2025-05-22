# CI/CD Flask App con Jenkins + Helm + Kubernetes

Questo progetto mostra un flusso **CI/CD completo** per il deploy automatico di un'applicazione **Flask** su Kubernetes usando:

-  Jenkins (con pipeline declarativa)
-  Helm (per il packaging e deploy)
-  Kubernetes (es. Docker Desktop, Minikube o cloud)
-  Docker Hub (per build & push immagini)

---

## 📁 Struttura del progetto


---

## ⚙️ Requisiti

Per testare o usare questo progetto, assicurati di avere:

- Jenkins configurato con:
  - Docker e Helm installati
  - Kubernetes accessibile (es. Docker Desktop, Minikube)
  - Plugin: `Pipeline`, `Docker`, `Git`, `Kubernetes CLI`
-  Un account Docker Hub
-  Una namespace Kubernetes creata (es. `formazione-sou`)

---

## Jenkins Credentials necessarie

Crea una credenziale Jenkins con:

- **ID:** `dockerhub-credentials`
- **Tipo:** Username e Password
- **Uso:** Login automatico su Docker Hub nella pipeline

---

## Cosa fa la pipeline

Il file `Jenkinsfile` esegue i seguenti step:

1. **Pulizia workspace**
2. **Clonazione repo GitHub** (variabile: `GIT_URL`)
3. **Login su Docker Hub**
4. **Visualizzazione release Helm installate**
5. **Deploy su Kubernetes** tramite Helm chart (`helm-chart/`)

---

## Esempio variabili usate nella pipeline

Nel Jenkinsfile:

```groovy
environment {
    GIT_URL = 'https://github.com/Ludovico1997/formazione_sou_k8s'
    IMAGE_NAME = 'ludo97/my_flask'
    DOCKER_CREDENTIALS_ID = 'dockerhub-credentials'
}

---

## Bonus: Accesso via Ingress Controller

Come esercizio extra, puoi installare un **Ingress Controller NGINX** e accedere alla tua app Flask da un URL locale come `http://formazionesou.local`.

### Passaggi

1. **Installa l’Ingress Controller con Helm**:

   ```bash
   helm install ingress-nginx ingress-nginx/ingress-nginx \
     --namespace ingress-nginx \
     --create-namespace

2. "sbloccare" l'ingress all'interno dell'helm chart.