"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "fat-tree topology."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        coreSwitch1 = self.addSwitch('c1')
        coreSwitch2 = self.addSwitch('c2')

        for i in range(4):
            edgeSwitch = self.addSwitch(f'e{i+1}')
            self.addLink(edgeSwitch, coreSwitch1)
            self.addLink(edgeSwitch, coreSwitch2)

            # Connect 2 servers to each edge switch
            for j in range(2):
                server = self.addHost(f'h{i*2+j+1}')
                self.addLink(server, edgeSwitch)


topos = { 'mytopo': ( lambda: MyTopo() ) }
