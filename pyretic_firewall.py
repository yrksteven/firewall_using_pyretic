#!/usr/bin/python
from pyretic.lib.corelib import *
from pyretic.lib.std import *
from pyretic_switch import act_like_switch
import os
import csv

def main():
   not_allowed=none

   csvFile=open("%s/pyretic/firewall-policies.csv"%os.environ['HOME'], 'r')
   
   cursor=csv.DictReader(csvFile)
   
   for d in cursor:
      not_allowed = not_allowed +(match(srcmac=MAC(d['mac_0'])) & match(dstmac=MAC(d['mac_1']))) + (match(srcmac=MAC(d['mac_1']))& match(dstmac=MAC(d['mac_0'])))
   
   allowed=~not_allowed

   return allowed >> act_like_switch()


