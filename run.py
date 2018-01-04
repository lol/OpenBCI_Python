from OpenBCIBoard import OpenBCIBoard
from OpenBCIBoard import OpenBCISample
import time
import threading
import random
from queue import Queue
import numpy
import matplotlib.pyplot as plt
import csv
#import pylab
#import pyqtgraph as pg
#import pyqtgraph.multiprocess as mp


#data = []

#def handle_sample(sample, out_q):
#    data = sample.channel_data[7]
#    out_q.put(data)
#    test = out_q.get(data)
#    print(test)

def receiver(in_q):
    while True:
        sample = in_q.get()
        #print(data.id)
        data.append(sample.channel_data[7])

def plotter(in_q):
    data = []
    #plt.figure()
    #graph = plt.plot([])
    #plt.ion()
    #plt.show()
    while True:
        sample = in_q.get()   #id, channel_data
        #data.append(sample.id)
        print(sample.id, sample.channel_data)
        #print(range(len(data)))
        #plt.pause(1)
        #graph.set_xdata(range(len(data)))
        #graph.set_ydata(numpy.asarray(data))
        #plt.draw()

def csvwriter(in_q):
    print("---- Writing to signal.csv")
    c = csv.writer(open('signal.csv', 'w'), delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #c = csv.writer(open('signal.csv', 'w'), delimiter=',', escapechar=';', quoting=csv.QUOTE_NONE)
    while True:
        sample = in_q.get()
        c.writerow([sample.id, sample.channel_data[0], sample.channel_data[1], sample.channel_data[2], sample.channel_data[3], sample.channel_data[4], sample.channel_data[5], sample.channel_data[6], sample.channel_data[7]])
        
    
if __name__ == '__main__':
    board = OpenBCIBoard()
#board.print_register_settings()
    q = Queue()
    
    #t1 = threading.Thread(target=board.start_streaming(handle_sample, q))
    t1 = threading.Thread(target=board.start_streaming, args=(q, ))
    #t2 = threading.Thread(target=receiver, args=(q, ))
    #t2 = threading.Thread(target=plotter, args=(q, ))
    t2 = threading.Thread(target=csvwriter, args=(q, ))
    #t1.daemon = True
    t1.start()
    t2.start()
    
#    plt.figure()
#    ln, = plt.plot([])
#    plt.ion()
#    plt.show()
#    
#    plt.ion()
#    while True:
#        plt.pause(1)
#        ln.set_xdata(range(len(data)))
#        ln.set_ydata(data)
#        plt.draw()
