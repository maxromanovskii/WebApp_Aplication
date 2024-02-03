<img width="279" alt="Снимок экрана 2024-02-03 в 17 58 07" src="https://github.com/maxromanovskii/WebApp_Aplication/assets/151863055/941591eb-c849-403d-8818-d6e8ba6d3ccf">

How the model works!
![image](https://github.com/maxromanovskii/WebApp_Aplication/assets/151863055/4b669e76-e0bb-4903-af80-9640f7a5142b)

If the service is not working or there is no access, this message will appear!
"Work is underway on the site!"

Build and deploy the app to minikube for the first time!
Start minikube
minikube start

Point your terminal to minikube's Docker using minikube docker-env
# on Mac or Linux
eval $(minikube docker-env)

Build Docker image inside minikube
docker build -t local/devex:v1 .

Deploy to Kubernetes
kubectl apply -f deploy/k8s.yaml

Accees the deployed service in your browser
minikube service local-devex-svc

