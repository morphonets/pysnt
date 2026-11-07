import pysnt
pysnt.initialize()
from pysnt import SNTService
tree = SNTService().demoTree("pyramidal")
tree.show3D()
