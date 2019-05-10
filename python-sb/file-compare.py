#!/usr/bin/env python

with open('pcln-all-linux-hosts') as f1:
    linux_hosts = f1.read().splitlines()

with open('cloud-ansible-hosts-only') as f2:
    cloud_ansible = f2.read().splitlines()

append_list = []

for hosts in linux_hosts:
    if hosts not in cloud_ansible:
        print (hosts)
        final = append_list.append(hosts)
    else:
        pass
print (final)
