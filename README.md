[![Docker Image CI](https://github.com/minsoo9506/mrx-on-boarding/actions/workflows/docker-image.yml/badge.svg)](https://github.com/minsoo9506/mrx-on-boarding/actions/workflows/docker-image.yml)

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