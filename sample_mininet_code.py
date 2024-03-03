
from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
        SwitchA = self.addSwitch( 's1' )
        SwitchB = self.addSwitch( 's2' )
        SwitchC = self.addSwitch( 's3' )
        SwitchD = self.addSwitch( 's4' )
        SwitchE = self.addSwitch( 's5' )

        # Add links
        self.addLink( leftHost, SwitchA )
        self.addLink( SwitchA, SwitchB )
        self.addLink( SwitchA, SwitchC )
        self.addLink( SwitchB, SwitchD )
        self.addLink( SwitchB, SwitchE )
        self.addLink( SwitchC, SwitchD )
        self.addLink( SwitchC, SwitchE )
        self.addLink( SwitchE, SwitchD )
        self.addLink( SwitchD, rightHost )

topos = { 'mytopo': ( lambda: MyTopo() ) }
