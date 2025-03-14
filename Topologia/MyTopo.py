from mininet.topo import Topo


class MyTopo(Topo):
    def __init__(self):
        Topo.__init__(self)

        s1 = self.addSwitch("s1")
        h1 = self.addHost("h1")
        s2 = self.addSwitch("s2")
        h2 = self.addHost("h2")
        s3 = self.addSwitch("s3")
        h3 = self.addHost("h3")
        s4 = self.addSwitch("s4")
        h4 = self.addHost("h4")
        s5 = self.addSwitch("s5")
        h5 = self.addHost("h5")
        s6 = self.addSwitch("s6")
        h6 = self.addHost("h6")
        s7 = self.addSwitch("s7")
        h7 = self.addHost("h7")
        s8 = self.addSwitch("s8")
        h8 = self.addHost("h8")
        s9 = self.addSwitch("s9")
        h9 = self.addHost("h9")
        s10 = self.addSwitch("s10")
        h10 = self.addHost("h10")

        link_h1s1 = self.addLink(h1, s1, bw=10, delay='0.1ms', loss=0, max_queue_size=100)
        link_h2s2 = self.addLink(h2, s2, bw=10, delay='0.1ms', loss=0, max_queue_size=100)
        link_h3s3 = self.addLink(h3, s3, bw=10, delay='0.1ms', loss=0, max_queue_size=100)
        link_h4s4 = self.addLink(h4, s4, bw=10, delay='0.1ms', loss=0, max_queue_size=100)
        link_h5s5 = self.addLink(h5, s5, bw=10, delay='0.1ms', loss=0, max_queue_size=100)
        link_h6s6 = self.addLink(h6, s6, bw=10, delay='0.1ms', loss=0, max_queue_size=100)
        link_h7s7 = self.addLink(h7, s7, bw=10, delay='0.1ms', loss=0, max_queue_size=100)
        link_h8s8 = self.addLink(h8, s8, bw=10, delay='0.1ms', loss=0, max_queue_size=100)
        link_h9s9 = self.addLink(h9, s9, bw=10, delay='0.1ms', loss=0, max_queue_size=100)
        link_h10s10 = self.addLink(h10, s10, bw=10, delay='0.1ms', loss=0, max_queue_size=100)

        link_s1s2 = self.addLink(s1, s2, bw=10, delay='2.8ms', loss=0, max_queue_size=150)
        link_s2s3 = self.addLink(s2, s3, bw=10, delay='3.7ms', loss=0, max_queue_size=150)
        link_s3s4 = self.addLink(s3, s4, bw=10, delay='1.8ms', loss=0, max_queue_size=150)
        link_s3s5 = self.addLink(s3, s5, bw=10, delay='6.2ms', loss=0, max_queue_size=150)
        link_s5s6 = self.addLink(s5, s6, bw=10, delay='6.2ms', loss=0, max_queue_size=150)
        link_s6s7 = self.addLink(s6, s7, bw=10, delay='1.8ms', loss=0, max_queue_size=150)
        link_s7s8 = self.addLink(s7, s8, bw=10, delay='3.5ms', loss=0, max_queue_size=150)
        link_s5s9 = self.addLink(s5, s9, bw=10, delay='7.5ms', loss=0, max_queue_size=150)
        link_s9s10 = self.addLink(s9, s10, bw=10, delay='8.5ms', loss=0, max_queue_size=150)

        link_s5s10 = self.addLink(s5, s10, bw=10, delay='4.5ms', loss=0, max_queue_size=150)
        link_s7s10 = self.addLink(s7, s10, bw=10, delay='4.4ms', loss=0, max_queue_size=150)
        link_s4s5 = self.addLink(s4, s5, bw=10, delay='5.2ms', loss=0, max_queue_size=150)
        link_s1s4 = self.addLink(s1, s4, bw=10, delay='7ms', loss=0, max_queue_size=150)
        link_s2s6 = self.addLink(s2, s6, bw=10, delay='3.7ms', loss=0, max_queue_size=150)
        link_s1s8 = self.addLink(s1, s8, bw=10, delay='9ms', loss=0, max_queue_size=150)

topos = {'MyTopo': (lambda: MyTopo())}