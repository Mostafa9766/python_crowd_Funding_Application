#!/bin/python

def usr_id():
    nid=open(r"usrs_data.txt", 'r') 
    lastid = len(nid.readlines())
    nid.close()
    return lastid+1
usr_id()
