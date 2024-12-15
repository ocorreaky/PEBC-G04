import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import utilidades as util
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error, r2_score
from utilidades import *

# Configuración Apertura
util.Config_pag()

# Llamar el menú
util.generarMenu()

# Redimensionar los logotipos
logo1 = util.resize_image(util.path + "/media/logos/logo1.png", 2.00)
logo2 = util.resize_image(util.path + "/media/logos/logo2.png", 2.00)
logo3 = util.resize_image(util.path + "/media/logos/logo3.png", 2.00)

util.Logos_y_Titulo(logo1, logo2, logo3)

############################################################################################
# Leer y publicar df con la descripción de la base de datos inicial
df = pd.read_csv(util.path + '/data/BD_Inicial_Descrip.csv')

# Insertar dataframe que describe la base de datos original
st.write("---")  # Línea divisoria horizontal
st.write("### Descripción de la base de datos original")
st.dataframe(df)




