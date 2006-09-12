#import pdb
#pdb.set_trace()

import sys
from os import sep
sys.path.append('..'+sep+'pyvolution')

#========================================================================
from config import g, epsilon
from Numeric import allclose, array, zeros, ones, Float
from advection import Domain, Transmissive_boundary, Dirichlet_boundary
from Numeric import array


from mesh_factory import rectangular

#points, vertices, boundary = rectangular(60, 60)
points, vertices, boundary = rectangular(10, 10)

#Create advection domain with direction (1,-1)
domain = Domain(points, vertices, boundary, velocity=[1.0, 0.0])

# Initial condition is zero by default

#domain.initialise_visualiser(scale_z=1.0)
#domain.visualise_range_z = 0.5
#domain.visualise_color_stage = True


#Boundaries
T = Transmissive_boundary(domain)
D = Dirichlet_boundary(array([1.0]))

#turn on the visualisation
rect = [0.0, 0.0, 1.0, 1.0]
#domain.initialise_visualiser(rect=rect)
domain.visualise = True


domain.default_order = 2

print domain.quantities.keys()

domain.set_boundary( {'left': D, 'right': T, 'bottom': T, 'top': T} )
domain.check_integrity()

#Check that the boundary value gets propagated to all elements
for t in domain.evolve(yieldstep = 0.1, finaltime = 1.5):
    domain.write_time()
    #pdb.set_trace()
