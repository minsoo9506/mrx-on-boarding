[![Docker Image CI](https://github.com/minsoo9506/mrx-on-boarding/actions/workflows/docker-image.yml/badge.svg?branch=master)](https://github.com/minsoo9506/mrx-on-boarding/actions/workflows/docker-image.yml) [![Commit For ArgoCD](https://github.com/minsoo9506/mrx-on-boarding/actions/workflows/argocd.yml/badge.svg)](https://github.com/minsoo9506/mrx-on-boarding/actions/workflows/argocd.yml)

## rest api 만들기
- flask 이용하여 간단한 restapi 구현
    - request에서 "name"이 "minsoo" 이면 "Hi", 아니면 "Who are u" return

## dockerize
- Dockerfile 이용하여 image build하고 container 띄워서 서버띄우기
- curl 명령어를 이용하여 POST 보내기

```bash
docker build . -t restapi:1.0.0

docker run --name myrestapi -p 8080:8080 restapi:1.0.0

curl -X POST \
     -H 'Content-Type: application/json' \
     -d '{"name": "minsoo"}' \
         http://localhost:8080/login
```

## CI (github action)
- push하면 docker build가 수행되는 github action 만들기
- docker build 후에 이미지를 github container registry에 저장되도록 github action 만들기

## Docker compose
- 위에서 만든 dockerfile을 이용해 `docker-compose.yml`를 작성하기

```bash
docker-compose up
```

## Helm
- minikube와 바로 ip통신이 안된다.
- `port-forward`를 해줘야 한다.
```bash
helm install restapi ./restapi/
kubectl port-forward svc/restapi-restapi 8080:8080
curl -X POST \
    -H 'Content-Type: application/json' \
    -d '{"name": "minsoo"}' \
        http://localhost:8080/login
```

## Ingress
- not yet

## ArgoCD
- `master` branch에서 restapi 관련 내용을 수정하고 push하면 git action으로 `ArgoCD` branch의 helm관련 `values.yml` 파일을 수정하고 push한다.
- 그러면 해당 repo의 `ArgoCD` branch를 ArgoCD가 바라보고 있고 자동으로 syncronize한다. (CD)