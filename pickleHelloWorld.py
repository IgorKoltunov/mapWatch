import pickle
from pprint import pprint as pp

with open('listOfPlacemarks.pkl', 'rb') as f:
    mynewlist = pickle.load(f)

pp(mynewlist)