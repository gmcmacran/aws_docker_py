import json
import numpy as np

json_input = '{"rings" : [[[-8081441.0, 5685214.0], [-8081446.0, 5685216.0], [-8081442.0, 5685219.0], [-8081440.0, 5685211.0], [-8081441.0, 5685214.0]]]}'
dict = json.loads(json_input)
numpy_2d_arrays = [np.array(ring) for ring in dict["rings"]][0]


json_input = '{"[[-8081441.0, 5685214.0], [-8081446.0, 5685216.0], [-8081442.0, 5685219.0], [-8081440.0, 5685211.0], [-8081441.0, 5685214.0]]}'
X = np.asarray(json_input)
X.concatenate(X, axis=0)


json_input = '{"rings" : [[[-8081441.0, 5685214.0], [-8081446.0, 5685216.0], [-8081442.0, 5685219.0], [-8081440.0, 5685211.0], [-8081441.0, 5685214.0]]]}'
skmodel = clf

temp = X.tolist()
json_input = json.dumps(temp)

temp = json.loads(json_input)
X2 = np.array(temp)