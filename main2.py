import tariff
import numpy as np


tariff.set({"Function": 100,
            "lib": 100,
            })


from lib.util import Function

x = np.array([73, 86, 93, 92, 72, 65, 58, 75])
y = np.array([70, 80, 96, 85, 68, 68, 62, 78])


job = Function(x, y, len(x))

job.frame()
job.Graphh()

