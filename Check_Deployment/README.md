# Check_Deploy – Verifica automatica del Deployment su Kubernetes

Questa directory contiene uno script Python che automatizza il controllo di qualità del **Deployment Kubernetes** creato tramite Helm.  
Lo script esegue step fondamentali per verificare che le best practice siano rispettate, come la presenza di **Readiness**, **Liveness probe**, **Resource Limits** e **Requests**.

---

## Contenuto

- `script.py`: script che esegue controlli automatici sul deployment della Flask app

---

## Cosa fa lo script?

1. Crea una **ServiceAccount** in namespace `formazione-sou`
2. Genera un **token JWT** per autenticarsi via API Server
3. Crea un **ClusterRoleBinding** collegato al ruolo `view`
4. Esegue una **chiamata API** al server Kubernetes per scaricare la risorsa `Deployment` in formato YAML
5. Verifica la presenza delle seguenti configurazioni nel deployment:
   - Readiness probe
   - Liveness probe
   - Resource `limits`
   - Resource `requests`

---

## Come eseguirlo

Assicurati di avere:

- Python 3 installato
- `kubectl` configurato e accesso al cluster Kubernetes (es. Docker Desktop, Minikube)
- Deployment già creato tramite Helm (`mychart-helm-chart` nel namespace `formazione-sou`)

Poi esegui lo script:

```bash
cd Check_Deploy
python3 check_deploy.py
