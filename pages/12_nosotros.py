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

# Configuración Apertura
util.Config_pag()

# Llamar el menú
util.generarMenu()

# Construcción robusta de rutas
path_logo1 = os.path.join(util.path, "media", "Logos", "Logo1.png")
path_logo2 = os.path.join(util.path, "media", "Logos", "Logo2.png")
path_logo3 = os.path.join(util.path, "media", "Logos", "Logo3.png")

# Procesa imágenes
logo1 = util.resize_image(path_logo1, 2.00)
logo2 = util.resize_image(path_logo2, 2.00)
logo3 = util.resize_image(path_logo3, 2.00)

util.Logos_y_Titulo(logo1, logo2, logo3)

############################################################################################
# Insertar imagen
imagen = Image.open('media/nos/nosotros.png')

# Incrustar la imagen
st.image(imagen, caption="Equipo PEBC",
         use_container_width=600)
