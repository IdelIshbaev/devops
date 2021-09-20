# lab9
report screenshots for both python and vue apps:
![image](./screenshots/1.png)
![image](./screenshots/2.png)
![image](./screenshots/3.png)
## manifest
### python app
![image](./screenshots/4.png)
### Vue.js app + python app
![image](./screenshots/5.png)
#### running app
Check if app is actually accessible and running can be checked by links (after runnig command below) after setting up.
```
minikube service app-vue-serv
OR
minikube service app-python-serv
```
- Ingress is used for managing users's access to the Kubernetes cluster services
- Ingress controleer is a load balancer that provides bridge btw Kubernetes services and external services. 
- StatefulSet manages deployment and scaling of set of Pods.
- DaemonSet ensure that Nodes run cope of Pod.
- PersistentVolumes offers Kub. applications a effecient way to request, consimbe and storage resources. In short, it is a piese of ctorage in a cluster.