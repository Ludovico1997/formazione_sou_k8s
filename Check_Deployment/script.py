import subprocess
import time

comando_create_sa = "kubectl create serviceaccount my-reader-sa -n formazione-sou"
result_sa = subprocess.run(comando_create_sa, shell=True, capture_output=True, text=True)
print(result_sa.stdout)
print(".........")
time.sleep(5)

comando_create_token = "kubectl create token my-reader-sa -n formazione-sou"
result_token = subprocess.run(comando_create_token, shell=True, capture_output=True, text=True)
print(result_token.stdout)
token_sa=result_token.stdout
print(".........")
time.sleep(5)

##view è un clusterrole pre settato! in caso di role o clusterrole specifiche dovremmo crearle.
comando_clusterrolebinding= "kubectl create clusterrolebinding my-reader-sa-binding --clusterrole=view --serviceaccount=formazione-sou:my-reader-sa"
result_clusterrolebinding = subprocess.run(comando_clusterrolebinding, shell=True, capture_output=True, text=True)
print(result_clusterrolebinding.stdout)
print(".........")
time.sleep(5)

print("facciamo il curl del deployment creato con helm chart nel precedente step.")
comando_curl= f'curl --insecure -H "Authorization: Bearer {token_sa}" https://localhost:6443/apis/apps/v1/namespaces/formazione-sou/deployments/mychart-helm-chart > deploy.yaml && echo "DONE"'
result_curl = subprocess.run(comando_curl, shell=True, capture_output=True, text=True)
print(result_curl.stdout)
time.sleep(5)

print("Controllo se abbiamo Readiness e Liveness Probe, Limits e Requests")
comando_grep_readiness= 'cat deploy.yaml | grep -i readiness'
comando_grep_liveness= 'cat deploy.yaml | grep -i liveness'
comando_grep_limits= 'cat deploy.yaml | grep -i limits'
comando_grep_requests= 'cat deploy.yaml | grep -i requests'

result_grep_readiness = subprocess.run(comando_grep_readiness, shell=True, capture_output=True, text=True)
result_grep_liveness = subprocess.run(comando_grep_liveness, shell=True, capture_output=True, text=True)
result_grep_limits = subprocess.run(comando_grep_limits, shell=True, capture_output=True, text=True)
result_grep_requests = subprocess.run(comando_grep_requests, shell=True, capture_output=True, text=True)

if result_grep_readiness.stdout != "" :
    print("readiness c'è")
else:
    print("manca il readiness")
time.sleep(2)
if result_grep_liveness.stdout != "" :
    print("liveness c'è")
else:
    print("manca il liveness")
time.sleep(2)
if result_grep_limits.stdout != "" :
    print("limits c'è")
else:
    print("manca il limits")
time.sleep(2)
if result_grep_requests.stdout != "" :
    print("requests c'è")
else:
    print("manca il requests")
time.sleep(2)


# print("lo yaml ora lo salviamo in un file chiamato deploy.txt")
# comando_salvo_curl= f'{result_curl.stdout} >> deploy.txt'
# result_salvo_curl = subprocess.run(comando_salvo_curl, shell=True, capture_output=True, text=True)
# time.sleep(5) 

# print("Check")
# comando_salvo_curl= f'{result_curl.stdout} >> deploy.txt'
# result_salvo_curl = subprocess.run(comando_salvo_curl, shell=True, capture_output=True, text=True)
# time.sleep(5) 

# for i in range (1, 10):
#     print(".........")
#     print("\033[91m" + "livio is the best" + "\033[0m") 

