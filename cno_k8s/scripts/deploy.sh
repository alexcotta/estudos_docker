#!/bin/bash
# Build e push imagem
docker tag cno-etl gcr.io/SEU-PROJETO/cno-etl:latest
docker push gcr.io/SEU-PROJETO/cno-etl:latest

# Deploy sequencial
kubectl apply -f k8s-simple/
kubectl rollout status deployment/cno-etl
