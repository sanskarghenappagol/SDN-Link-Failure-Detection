from mininet.topo import Topo
from mininet.node import OVSKernelSwitch

class RingTopo(Topo):
    def build(self):
        s1 = self.addSwitch('s1', cls=OVSKernelSwitch, failMode='standalone')
        s2 = self.addSwitch('s2', cls=OVSKernelSwitch, failMode='standalone')
        s3 = self.addSwitch('s3', cls=OVSKernelSwitch, failMode='standalone')
        s4 = self.addSwitch('s4', cls=OVSKernelSwitch, failMode='standalone')
        h1 = self.addHost('h1', ip='10.0.0.1/24')
        h2 = self.addHost('h2', ip='10.0.0.2/24')
        h3 = self.addHost('h3', ip='10.0.0.3/24')
        h4 = self.addHost('h4', ip='10.0.0.4/24')
        self.addLink(h1, s1)
        self.addLink(h2, s2)
        self.addLink(h3, s3)
        self.addLink(h4, s4)
        self.addLink(s1, s2, bw=10, delay='5ms')
        self.addLink(s2, s3, bw=10, delay='5ms')
        self.addLink(s3, s4, bw=10, delay='5ms')
        self.addLink(s4, s1, bw=10, delay='5ms')
        self.addLink(s1, s3, bw=5, delay='10ms')

topos = {'ringtopo': RingTopo}
