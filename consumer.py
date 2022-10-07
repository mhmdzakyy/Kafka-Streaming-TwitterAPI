import os
os.environ['CONDA_DLL_SEARCH_MODIFICATION_ENABLE'] = '1'

from confluent_kafka import Consumer

################

# Create Consumer Object
c=Consumer({'bootstrap.servers':'localhost:9092','group.id':'python-consumer','auto.offset.reset':'earliest'})
print('Kafka Consumer has been initiated...')

print('Available topics to consume: ', c.list_topics().topics)

# Subscribe to topic
c.subscribe(['topic-indonesia-covid19'])  

################
def main():
    while True: 
        msg=c.poll(1.0) 
        if msg is None:
            continue
        if msg.error():
            print('Error: {}'.format(msg.error()))
            continue
        data=msg.value().decode('utf-8') 
        print(data)
    c.close()
        
if __name__ == '__main__':
    main()