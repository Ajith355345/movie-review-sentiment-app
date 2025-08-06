import pandas as pd 
import pickle as pk
from sklearn.feature_extraction.text import TfidfVectorizer
import streamlit as st

model = pk.load(open('model.pkl','rb'))
scaler = pk.load(open('scaler.pkl','rb'))
