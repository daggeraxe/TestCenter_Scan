#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# --author：gzhao--
# Edit time: 2020/11/16 16:30
from scapy.layers.inet import IP, TCP, ICMP, sr, sr1
from random import randint
from ipaddress import ip_network
from threading import Thread
import time
import sys

def scan_ip(ip):
    ip_record = 'TestCenter_IP_SCAN.txt'  # this txt file is for record scan IP which is addressable TC IP
    ip_id = randint(1, 65535)
    icmp_id = randint(1, 65535)
    icmp_seq = randint(1, 65535)
    Picmp = IP(dst=ip, ttl=64, id=ip_id)/ICMP(id=icmp_id, seq=icmp_seq)
    pingresponse = sr(Picmp, timeout=1, verbose=0)    # verbose不显示详情，也可替换为False
    if pingresponse:
        Ptcp = IP(dst=ip, ttl=64, id=ip_id)/TCP(dport=40004)
        tcpresponse = sr1(Ptcp, timeout=5, verbose=0)
        if tcpresponse:
            try:
                flag = str(tcpresponse['TCP'].flags)
            except:
                print('  [-] Debug ...', ip, ' TCP: ', tcpresponse.show())
                flag = ''
            if flag == 'SA':
                print("  [-] %s is alive" % str(ip))
                with open(ip_record, 'a+') as file:
                    file.write(str(ip)+' ')

def get_last_line(filename):
    """
    get last line of a file
    :param filename: file name
    :return: last line or None for empty file
    """
    try:
        filesize = os.path.getsize(filename)
        if filesize == 0:
            return None
        else:
            with open(filename, 'rb') as fp: # to use seek from end, must use mode 'rb'
                offset = -8                 # initialize offset
                while -offset < filesize:   # offset cannot exceed file size
                    fp.seek(offset, 2)      # read # offset chars from eof(represent by number '2')
                    lines = fp.readlines()  # read from fp to eof
                    if len(lines) >= 2:     # if contains at least 2 lines
                        return lines[-1]    # then last line is totally included
                        # return str(lines[-1].split(), 'utf-8')
                    else:
                        offset *= 2         # enlarge offset
                fp.seek(0)
                lines = fp.readlines()
                return lines[-1]
                # return str(lines[-1].split(), 'utf-8')
    except FileNotFoundError:
        print('  [-]', filename + ' not found!')
        return None


def scan_network(network):
    ip_list = ip_network(network)
    print('  [-] Scan Network ... ', ip_list)
    for ip in ip_list:
        t = Thread(target=scan_ip, args=[str(ip)])
        t.start()