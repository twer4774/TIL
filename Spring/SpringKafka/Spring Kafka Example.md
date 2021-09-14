# Spring Kafka

- 참고
  - https://baek.dev/post/20/
  - https://velog.io/@tedigom/MSA-%EC%A0%9C%EB%8C%80%EB%A1%9C-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-5Backing-Service-lqk3b7560w

## 메시지 큐

- 프로세스가 데이터를 교환할 때 사용되는 통신 방법
- 네트워크 통신으로 함수를 호출하듯 사용한다. => RPC방식이라고 한다.(Remote Procedure Call)
- 서비스 간의 결합도를 낮춰 전체 서비스가 정상 운영되도록 도와준다.
- 대표적인 메시지 큐 서비스 : RabbitMQ, Kafka
- 특징
  - 비동기 : 비동기 방식으로 응답 처리 속도를 향상 시킬 수 있다.
  - 비동조 : 어플리케이션 서비스와 분리 가능하다.
  - 보증 : 메시지 전송 성공 여부를 확인할 수 있다.
  - 확장성 : 다수의 프로세스들이 큐에 메시지를 보낼 수 있다.
  - 과잉 : 메시지 전송 실패 시 재실행이 가능하다.
  - 탄력성 : 일부분 실패하더라도 다른 서비스에 영향을 미치지 않는다.

## Kafka

- 링크드인에서 개발했으며, 메시지 큐 중에 속도가 가장 빠르고 안정적이다.
- TCP/IP 방식으로 파일로 저장한다. => 오버헤드가 낮다.
- 내부적으로 Zookeper를 이용하며, Kafka를 설치하면 Zookeeper를 반드시 이용하게 된다.
  - Zookeeper를 따로 사용하는 경우라면 설계방식을 바꿔야 하는 경우가 있다.
- 분산 시스템에 최적화 되어 있다.
  - 대량의 데이터 처리 가능
- 애플, 드롭박스, 넷플릭스, 트위터, 우버 등에서 카프카를 사용하고 있다.
- 메시지를 잃어 버리지 않는다.
- 다른 메시지 서비스와의 차이 : Consumer가 Offset 정보를 관리한다.
  - 데이터를 읽은 후 Conusmer는 적절한 시점에 Offset을 Commit 해야 한다.
    - commit : 현재까지 읽은 메시지를 알려주는 행위

- 구성 요소

  - Broker : 데이터를 수신, 전달하는 서비스

    - 하나의 서버 당 하나의 데몬 프로세스로 동작한다.
    - 여러 대의 클러스터로 구성할 수 있다. => 스케일 아웃이 가능하다.
      - 스케일 업 : CPU, Memory 등의 업그레이드를 이용하여 성능을 높임
      - 스케일 아웃 : Load Balancer 등을 이용하여 서버의 대수를 늘려 성능을 높임

  - Message : 데이터를 다루는 최소한의 단위

  - Producer : 데이터 생성자

  - Consumer : 브로커에서 메시지를 취득하는 어플리케이션

    - Conumer Group: group.id로 지정하며, 클러스터의 메시지를 얻을 때 그룹 단위로 얻는다.
    - Consumer의 개수는 Partition의 개수를 초과할 수 없다.(같거나 작아야 한다.)
      - Consumer 개수가 많을 경우, 메시지를 취득할 수 없는 Consumer가 발생한다.
      - Partition이 많으면 Conusmer가 나눠서 적절하게 처리할 수 있다.

  - Topic : 메시지를 종류별로 관리하는 스토리지

    - Partition : 토픽에 대한 대량의 메시지 입출력을 지원하기 위해 Broker상의 데이터를 읽고 쓰는 단위. 파티션 수는 늘릴 수는 있지만 줄일 수 는 없기 때문에 설계에서 신중하게 고려해야한다.

      - Partition 설계시 고려사항 : 메시지 처리 속도, Consumer 개수, Consumer 쓰레드

    - Offset : 각 파티션에서 수신한 메시지의 일련번호

      - Long-End-Offset(LEO) : 파티션 데이터의 끝

      - Current Offset : Consumer가 데이터를 어디까지 취득했는지를 표시. 다음 새 레코드를 가져올 위치 표시

      - Commit Offset : Consumer가 커밋했는지를 나타낸다.

        - commit : 현재까지 읽은 메시지를 알려주는 행위

        - enable.auto.commit과 auto.commit.interval.ms로 설정 가능하며 기본값은 5000ms(5초)이다.

          - 리밸런스나 비정상적인 클라이언트 종료 등으로 데이터 누락을 방지하기 위해서는 수동으로 설정하기도 한다.

          

## 실습

### build.gradle

```groovy
plugins {
	id 'org.springframework.boot' version '2.4.11-SNAPSHOT'
	id 'io.spring.dependency-management' version '1.0.11.RELEASE'
	id 'java'
}

group = 'walter.unit'
version = '0.0.1-SNAPSHOT'
sourceCompatibility = '11'

repositories {
	mavenCentral()
	maven { url 'https://repo.spring.io/milestone' }
	maven { url 'https://repo.spring.io/snapshot' }
}

dependencies {
	implementation 'org.springframework.boot:spring-boot-starter-web'
	implementation 'org.springframework.kafka:spring-kafka'

	annotationProcessor 'org.projectlombok:lombok'
	compileOnly 'org.projectlombok:lombok'

	testImplementation 'org.springframework.boot:spring-boot-starter-test'
	testImplementation 'org.springframework.kafka:spring-kafka-test'
}


test {
	useJUnitPlatform()
}

```

### yml

- kafka server 설정

```yml
#producer etc default
spring.kafka:
  bootstrap-servers: 127.0.0.1:9092

#consumer
spring.kafka.consumer:
  bootstrap-servers: 127.0.0.1:9092
  group-id: waltergroup
  enable-auto-commit: true
  auto-commit-interval: 1000ms #10초마다 커밋. 기본값 500ms(5초)
  auto-offset-reset: latest

```

### docker-compose.yml

- kakfa는 zookeeper를 기본으로 포함하고 있다.

```dockerfile
version: '2'
services:
  zookeeper:
    image: wurstmeister/zookeeper
    container_name: zookeeper
    ports:
      - "12181:2181"
  kafka:
    image: wurstmeister/kafka:2.12-2.5.0
    container_name: kafka
    ports:
      - "9092:9092"
    environment:
      KAFKA_ADVERTISED_HOST_NAME: 127.0.0.1
      KAFKA_CREATE_TOPICS: "walter"
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
```

### Producer

```java
@RequiredArgsConstructor
@Service
public class KafkaProducerService {
    public static final String TOPIC_NAME = "walter";

    private final KafkaTemplate<String, String> kafkaTemplate;

    public void send(String data){
        try{
            kafkaTemplate.send(TOPIC_NAME, data);
        } catch (Exception e){
            e.printStackTrace();
        }
    }
}
```

### Consumer

```java
@Service
public class KafkaConsumerService {

    @KafkaListener(topics = KafkaProducerService.TOPIC_NAME, autoStartup = "true")
    public void consumer(String message){
        System.out.println("receive message : " + message);
    }
}
```

### Controller

```java
@RequiredArgsConstructor
@RestController
public class KafkaController {

    private final KafkaProducerService producerService;

    private final KafkaConsumerService consumerService;

    @GetMapping("/send/{message}")
    public void sendMessage(@PathVariable("message") String message){
        producerService.send(message);
    }
}
```

### 테스트

- docker-compse 실행 : docker-compose.yml이 있는 디렉토리에서 docker-compose up 실행
  - kafka와 zookeeper를 docker로 실행한다.
- Application 실행 후 http://localhost:8080/send/testMessage 접속
- 콘솔 로그 확인

```
2021-09-13 11:29:23.741  INFO 19288 --- [nio-8080-exec-1] o.a.k.clients.producer.ProducerConfig    : ProducerConfig values: 
	acks = 1
	batch.size = 16384
	bootstrap.servers = [127.0.0.1:9092]
	buffer.memory = 33554432
	client.dns.lookup = use_all_dns_ips
	client.id = producer-1
	compression.type = none
	connections.max.idle.ms = 540000
	delivery.timeout.ms = 120000
	enable.idempotence = false
	interceptor.classes = []
	internal.auto.downgrade.txn.commit = true
	key.serializer = class org.apache.kafka.common.serialization.StringSerializer
	linger.ms = 0
	max.block.ms = 60000
	max.in.flight.requests.per.connection = 5
	max.request.size = 1048576
	metadata.max.age.ms = 300000
	metadata.max.idle.ms = 300000
	metric.reporters = []
	metrics.num.samples = 2
	metrics.recording.level = INFO
	metrics.sample.window.ms = 30000
	partitioner.class = class org.apache.kafka.clients.producer.internals.DefaultPartitioner
	receive.buffer.bytes = 32768
	reconnect.backoff.max.ms = 1000
	reconnect.backoff.ms = 50
	request.timeout.ms = 30000
	retries = 2147483647
	retry.backoff.ms = 100
	sasl.client.callback.handler.class = null
	sasl.jaas.config = null
	sasl.kerberos.kinit.cmd = /usr/bin/kinit
	sasl.kerberos.min.time.before.relogin = 60000
	sasl.kerberos.service.name = null
	sasl.kerberos.ticket.renew.jitter = 0.05
	sasl.kerberos.ticket.renew.window.factor = 0.8
	sasl.login.callback.handler.class = null
	sasl.login.class = null
	sasl.login.refresh.buffer.seconds = 300
	sasl.login.refresh.min.period.seconds = 60
	sasl.login.refresh.window.factor = 0.8
	sasl.login.refresh.window.jitter = 0.05
	sasl.mechanism = GSSAPI
	security.protocol = PLAINTEXT
	security.providers = null
	send.buffer.bytes = 131072
	ssl.cipher.suites = null
	ssl.enabled.protocols = [TLSv1.2, TLSv1.3]
	ssl.endpoint.identification.algorithm = https
	ssl.engine.factory.class = null
	ssl.key.password = null
	ssl.keymanager.algorithm = SunX509
	ssl.keystore.location = null
	ssl.keystore.password = null
	ssl.keystore.type = JKS
	ssl.protocol = TLSv1.3
	ssl.provider = null
	ssl.secure.random.implementation = null
	ssl.trustmanager.algorithm = PKIX
	ssl.truststore.location = null
	ssl.truststore.password = null
	ssl.truststore.type = JKS
	transaction.timeout.ms = 60000
	transactional.id = null
	value.serializer = class org.apache.kafka.common.serialization.StringSerializer

2021-09-13 11:29:23.773  INFO 19288 --- [nio-8080-exec-1] o.a.kafka.common.utils.AppInfoParser     : Kafka version: 2.6.2
2021-09-13 11:29:23.773  INFO 19288 --- [nio-8080-exec-1] o.a.kafka.common.utils.AppInfoParser     : Kafka commitId: da65af02e5856e34
2021-09-13 11:29:23.773  INFO 19288 --- [nio-8080-exec-1] o.a.kafka.common.utils.AppInfoParser     : Kafka startTimeMs: 1631500163773
2021-09-13 11:29:23.786  INFO 19288 --- [ad | producer-1] org.apache.kafka.clients.Metadata        : [Producer clientId=producer-1] Cluster ID: 2Gf7Qp4xRUqfmnNRI2tFqQ
receive message : testMessage
```

