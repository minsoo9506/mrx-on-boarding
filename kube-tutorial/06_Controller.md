## Controller
- Index
    - ReplicationController
    - ReplicaSet
    - Deployment
    - DaemonSet
    - StatefulSet
    - Job
    - CronJob

- Controller란
    - pod의 개수를 보장
    - 예) 어떤 application을 운영할 때, pod 개수를 몇개 사용할지~
    - 예) `kubectl create deployment app --image=nginx --replicas=3` : 이러면 알아서 API, controller, scheduler, etcd가 같이 일하면서 pod 3개를 알아서 만들고 유지

### ReplicationController
- 요구하는 pod의 개수를 보장, 부족하면 template를 이용해 pod를 추가하고 넘치면 최근 pod를 삭제
- 기본구성
    - `selector`
    - `replicas`
    - `template`

```yaml
apiVersion: v1
kind: ReplicationController
metadata:
  name: <RC이름>
spec:
  replicas: <배포갯수>
  selector:
    key: value
  template:
    <컨테이너 템플릿>
...
```

- RC는 pod의 `metadata`에 있는 `labels`에 해당하는 녀셕의 `replicas`개수만큼 유지시켜준다. (`06-rc-nginx.yml` 참고)
- RC로 만든 pod들은 RC를 refer하고 있다. yaml을 확인해보자.
- `kubectl delete rc RC이름`해야 pod들을 지울 수 있다. 안 그러면 pod다 지워도 계속 생긴다. RC를 지우면 이에 해당하는 pod들도 다 지워진다.

- 명령어 한눈에 보기
```bash
kubectl create -f 06-rc-ngix.yml
kubectl get rc
kubectl get pod --show-labels
kubectl edit rc rc-nginx
kubectl scale rc rc-nginx --replicas=2
```
- `kubectl create -f 06-rc-ngix.yml`: pod가 3개 실행된다.
- `kubectl get rc(또는 replicationcontrollers)`: 실행중인 rc를 보여준다.
- `kubectl get pod --show-labels`: pod의 `labels`를 보여준다.
- `kubectl edit rc rc-nginx`: rc-nginx 관련 내용 수정가능
    - 여기서 `replicas`를 수정하면 바로 rc가 반영하여 개수가 달라진다.
- `kubectl scale rc rc-nginx --replicas=2`: pod의 개수를 2개로 바꾼다. 줄여야되면 가장 최근의 pod를 terminate한다.

- 질문) `replicas: 3` 이고 pod가 3개가 실행 중인 상태인 경우이다. 그런데 새로운 pod를 만드는데 위의 replicas에서의 `labels`를 yaml에 포함해서 띄우면 어떻게 될까?
    - 새로운 pod가 안 만들어진다. (바로 terminated 된다)
    - controller는 해당 `labels`을 갖고 있는 pod를 정해진 replicas만큼만 운영하기 때문이다.
- 질문) 이미 pod가 running되고 있는 상태에서 container image의 nginx 버전을 바꾸면 어떻게 될까?
    - 변화없다.
    - ReplicationController는 selector만 보고 있다.
    - 그런데 pod중에 하나를 삭제하면 controller가 바로 pod하나를 띄우는데 이 때는 바꾼 버전으로 띄워진다.

### ReplicaSet
- RC와 성격은 동일하다. pod의 개수 보장!
- RC보다 다양한 `selector`를 사용할 수 있다.
```yaml
selector:
  matchLabels:
    component: redis
  matchExpressions:
  - {key: tier, operator: In, values: [cache]}
  - {key: environment, operator: NotIn, values: [dev]}
```
- matchExpressions 연산자 (`operator`)
    - `In`: `key`와 `values`를 지정하여 `key`,`values`가 일치하는 pod만 연결
    - `NotIn`: `key`는 일치하고 `value`는 일치하지 않는 pod에 연결
    - `Exists`: `key`에 맞는 `label`의 pod를 연결
    - `DoesNotExist`: `key`와 다른 `label`의 pod를 연결 
- 예) `labels`은 `app: webui`이고 version이 [2.1, 2.2] 중 아무거나
```yaml
selector:
  matchLabels:
    app: webui
  matchExpressions:
  - {key: version, operator: In, values: ["2.1", "2.2"]}
```
- 명령어 한눈에 보기
    - 위에서 본 RC 명령어들과 거의 다 유사하다.
```bash
kubectl get rs
kubectl scale rs rs-nginx --replicas=2
kubectl delete rs rs-nginx --cascade=false
```
- `kubectl delete rs rs-nginx --cascade=false`: RS는 지워지지만 이에 해당하는 pod들은 살린다.
- 질문) 그러면 위의 명령어로 RS를 지웠다가 다시 동일한 RS를 만들면?
    - 기존의 pod들이 다시 RS의 control을 받는다.
    - `labels`, `selector` 가 중요한 기준!


### Deployment
### DaemonSet
### StatefulSet
### Job
### CronJob