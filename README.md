## rest api & dockerize & run
- flask 이용하여 간단한 restapi 구현
    - request에서 "name"이 "minsoo" 이면 "Hi", 아니면 "Who are u" return
- Dockerfile 이용하여 image build하고 container 띄워서 서버띄우기
- curl 명령어를 이용하여 POST 보내기
- rest-api-docker 위치에서 아래 명령어 실행하면 됨

```bash
docker build . -t restapi:1.0.0

docker run --name myrestapi -p 8080:8080 restapi:1.0.0

curl -X POST \
     -H 'Content-Type: application/json' \
     -d '{"name": "minsoo"}' \
         http://localhost:8080/login
```