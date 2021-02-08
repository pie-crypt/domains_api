import threading
from whois_4_ips import NICClient
domain = "google.com"

t0 = threading.Thread(NICClient.whois_t, args=(query, hostname, flags, 'eth0'))
t1 = threading.Thread(NICClient.whois_t, args=(query, hostname, flags, 'eth1'))
t2 = threading.Thread(NICClient.whois_t, args=(query, hostname, flags, 'eth2'))
t3 = threading.Thread(NICClient.whois_t, args=(query, hostname, flags, 'eth3'))

t0.start()
t1.start()
t2.start()
t3.start()

t0.join()
t1.join()
t2.join()
t3.join()