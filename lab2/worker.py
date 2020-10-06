import zmq
import math

def consumer():
    context = zmq.Context()
    consumer_receiver = context.socket(zmq.PULL)
    consumer_receiver.connect("tcp://127.0.0.1:5557")
    consumer_sender = context.socket(zmq.PUSH)
    consumer_sender.connect("tcp://127.0.0.1:5558")

    while True:
        work = consumer_receiver.recv_json()
        print (work)
        data = work['num']
        result = {'num' : math.sqrt(data)}
        consumer_sender.send_json(result)

consumer()
