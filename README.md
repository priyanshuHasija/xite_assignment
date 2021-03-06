
# xite_assignment

**Question1:** 
Here are the steps to create kafka cluster and ingest data into topicA.
1) create new custom image of kafka using DockerFile.

> Command: docker build -t kafkaimage1 .

2) Run docker compose file to setup the infrastructure.

> Command: docker compose up -d

This command will instantiate zookeeper and kafka clusters. 
kafka-setup container is responsible for topic creation and ingesting data into topic A.

**Question2 and 3:**
 Main.py script is responsible for consuming data from topicA. Each message is checked for its timestamp. 
If message timestamp falls within the specified range, message will be sent to topicA.

> Command: python main.py topicA topicB localhost:19092 localhost:29092
> localhost:39092

**Question4:** 
I can see few potential issues in this approach:
1) Kafka is a distributed cluster and it has the concept of replication. So, this overhead is not required if we are performing this step to avoid data loss and replication.
2) In real time scenario, we have to think of matching the frequency between producing messages to kafka and consuming messages from same kafka topic for filtration. We need to scale up consumers in case load increases on topicA.

Other way to fill gap or to replicate data from one kafka cluster to another is using kafka mirror maker.MirrorMaker is a process in Apache Kafka to replicate or mirror data from one cluster to another 
