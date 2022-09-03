#!/usr/bin/env python

import netfilterqueue
# iptables -I FORWARD -j NFQUEUE --queue-num 0
"""
It is a command that is used to trap all packets
that go through our computer in a queue.
 iptables - program in Kali Linux to modify network rules
 -I FORWARD - We want to modify exactly this chain (FORWARD)
 -I OUTPUT - If we want to use our local computer 
 to capture packets that living our own computer
 -I INPUT - packets sending to our computer
 -j NFQUEUE  - We put them in a Net Filter Queue
 --queue-num 0 - we specify this queue as 0
 """

# iptables --flush
"""
To delete iptables that we created 
"""


def process_packet(packet):
    print(packet)
    # packet.accept() - let them go through
    # dropping packets
    packet.drop()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
