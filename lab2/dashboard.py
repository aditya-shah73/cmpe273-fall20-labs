import zmq

def dashboard():
    context = zmq.Context()
    results_receiver = context.socket(zmq.PULL)
    results_receiver.bind("tcp://127.0.0.1:5558")
    for x in range(10001):
        result = results_receiver.recv_json()
        print(result['num'])

dashboard()
