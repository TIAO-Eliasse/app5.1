import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Application de distribution normale")
st.subheader("auteur: TIAO ELIASSE")

st.write("Cette application permet d'afficher l'histogramme d'une distribution normale."
         " L'utlisateur a la possibilité de modifier le nombre de binns de l'Histogramme."
         " Par ailleurs l'utilisateur a le libre choix de donner un nom au graphique")

data=np.random.normal(size=1000)
data=pd.DataFrame(data, columns=["Dist_norm"])
st.write(data)# Afficher le dataframe
# ON peut aussi utiliser la syntaxe suivante pour afficher le dataframe
#st.dataframe(data)
fig, ax = plt.subplots()
# Ajout de bins
n_bins=st.number_input(label="choisir un nombre de bins", min_value=10, max_value=20)
#Ajout de titre de graphique , L'utilisateur aura la possibilité d'ajouter le titre qui le convient
graph_title=st.text_input(label="choisir le titre du graphique")
ax.hist(data.Dist_norm,bins=n_bins)
plt.title(graph_title)
st.pyplot(fig)