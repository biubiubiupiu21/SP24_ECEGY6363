"""Custom topology
In this fat-tree topology, there are 2 core switches on the top layer (c1 and c2). Each of them have 4 wires facing down and connecting to an edge switch. Each core switch has one and only one connetion with every edge switch. 
There are 4 edge switches (e1, e2, e3, e4) on the second layer. Each of them has two wires going up and connect to different core switchs. That is, one edge switch would have one and only one connection to both of the core switches.
Each edge switch has two wires facing down and each of these wire connecting to a server. Therefore, there will be 4*2 = 8 servers in total (h1, h2, h3, h4, h5, h6, h7, h8) supported by this topology.

"""

from mininet.topo import Topo
N=4
class MyTopo( Topo ):
  def build(self, n=N):
    if n % 2 != 0:
      raise ValueError("N must be an even number.")
    coreSwitch1 = self.addSwitch('c1')
    coreSwitch2 = self.addSwitch('c2')
    for i in range(n):
      edgeSwitch = self.addSwitch('e{}'.format(i+1))
      self.addLink(edgeSwitch, coreSwitch1)
      self.addLink(edgeSwitch, coreSwitch2)
      for j in range(n//2):
        server = self.addHost('h{}'.format(i*2+j+1))
        self.addLink(server, edgeSwitch)
topos = { 'mytopo': ( lambda: MyTopo() ) }
