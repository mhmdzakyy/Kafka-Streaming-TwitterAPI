# Kafka-Streaming-TwitterAPI

Streaming API Twitter data using Confluent Kafka. In this case, I'll try to consume tweets data from twitter based on topic `Indonesian Covid-19`

## Requirement 
1. Python 3 or latest
2. Docker
3. Twitter Developer account 
4. Python Libraries
```
pip install confluent-kafka
pip install tweepy
```

## How to Run
1. Setup your Twitter Developer Account and get Twitter API Credential. You can follow the instruction [Here](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api)
2. put your Twitter API Credential in `auth.py`
3. Open Docker and running this command in terminal
```
docker-compose build
docker-compose up
```
4. If you want to change the topics, change the "search_term" variable in `producer.py`
5. Open file `producer.py` and running this command in terminal
```
python producer.py
```
6. open file `consumer.py` and running this command in terminal
```
python consumer.py
```
