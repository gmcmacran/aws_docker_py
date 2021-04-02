###################################
# Overview
#
# Simple function definitions to
# to score with a model. Nothing
# fancy. Just need something to
# work with.
###################################
import json
import numpy as np
from sklearn.ensemble import RandomForestClassifier

def prediction_function(json_input, skmodel):
    
    
    temp = json.loads(json_input)
    X = np.array(temp)
    
    if X.shape[0] > 0 and X.shape[1] == 2:
        prob = skmodel.predict_proba(X)
    else:
        prob = np.empty([0, 2])
        
    prob = prob[:,1]
        
    out = prob.tolist()
    out = json.dumps(out)
    return out

# =============================================================================
# # testing code
# X, _ = make_classification(n_samples=10,
#                            n_clusters_per_class=1, n_features = 2, 
#                            n_informative=2, n_redundant = 0, 
#                          n_repeated = 0, random_state=1)
# temp = X.tolist()
# temp = json.dumps(temp)
# prediction_function(temp, clf)  
# =============================================================================
    
    
    