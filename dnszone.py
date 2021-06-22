#!/usr/bin/python3

#script to test zone transfers
#requires dnspython

import dns.query
import dns.resolver
import dns.zone

#set lookup info here - this could be passed as parameters later
domain = "megacorpone.com"
nsname = "NS2.MEGACORPONE.COM"

nsip = dns.resolver.resolve(nsname, 'A')   #comes back as array or list object?
lookupip = str(nsip[0])  #covert resulting ip to string

z = dns.zone.from_xfr(dns.query.xfr(lookupip, domain))   #perform zone transfer
#print results
for n in sorted(z.nodes.keys()):
    print(z[n].to_text(n))