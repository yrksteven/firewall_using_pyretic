

# firewall_using_pyretic
Create a fully functional layer-2 Firewall application using Pyretic

Objective:
Implement a layer 2 firewall that runs alongside the MAC learning module on the Pyretic runtime

1. Pyretic runtime system
2. Verify Hub behavior with tcpdump
3. Verify Switch behavior with tcpdump
4. Understand pyretic_hub.py and pyretic_switch.py

Firewall:
1. pyretic_firewall.py: a skeleton class which you will update with the logic for installing firewall rules.
2. firewall-policies.csv:  a list of MAC pairs (i.e., rules) read as input by the firewall application. These pairs are the hosts can’t communicate with each other.
3. You can provide the firewall rules in firewall-policies.csv  and read it into the main function
4. Rules are decided by you!
5. These 2 files can be downloaded on the course webpage
