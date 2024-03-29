<img width="279" alt="Снимок экрана 2024-02-03 в 17 58 07" src="https://github.com/maxromanovskii/WebApp_Aplication/assets/151863055/941591eb-c849-403d-8818-d6e8ba6d3ccf">

How the model works!
![image](https://github.com/maxromanovskii/WebApp_Aplication/assets/151863055/4b669e76-e0bb-4903-af80-9640f7a5142b)

<img width="569" alt="Снимок экрана 2024-02-03 в 18 06 06" src="https://github.com/maxromanovskii/WebApp_Aplication/assets/151863055/3b1cd942-97ad-4a71-befb-87aca2c9491d">





# .github/workflows/build-and-deploy.yaml

name: Build and Deploy

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Build and push Proper Solution Docker image
      uses: docker/build-push-action@v2
      with:
        context: ./proper_solution
        push: true
        tags: your-docker-hub/proper-solution:latest

    - name: Build and push Fallback Solution Docker image
      uses: docker/build-push-action@v2
      with:
        context: ./fallback_solution
        push: true
        tags: your-docker-hub/fallback-solution:latest

    - name: Deploy to Kubernetes
      uses: azure/k8s-deploy@v1
      with:
        kubeconfig: ${{ secrets.KUBE_CONFIG }}
        manifests: kubernetes/*
