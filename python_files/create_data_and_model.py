###################################
# Overview
#
# Simple script that creates data
# and saves a model. Nothing fancy.
# Just need a model to work with.
#
# When docker is built, the saved
# model is copyied over. This code
# is kept for reproducibility
# purposes.
###################################
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from joblib import dump

X, y = make_classification(n_samples=500,
                           n_clusters_per_class=1, n_features = 2, 
                           n_informative=2, n_redundant = 0, 
                           n_repeated = 0, random_state=1)

clf = RandomForestClassifier(max_features='sqrt')
clf.fit(X,y)

dump(clf, 'models/random_forest_model.joblib')
