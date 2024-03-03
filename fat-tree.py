"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
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
      for j in range(n/2):
        server = self.addHost('h{}'.format(i*2+j+1))
        self.addLink(server, edgeSwitch)
topos = { 'mytopo': ( lambda: MyTopo() ) }
