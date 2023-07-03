#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 19:59:58 2023

@author: gonzalo
"""

import pygraphviz as pgv
from IPython.display import Image

# Crear el grafo
G = pgv.AGraph(directed=True)

# Configuración de atributos visuales
G.node_attr["shape"] = "box"   # Forma de los lugares
G.node_attr["style"] = "filled"   # Estilo de los lugares
G.node_attr["fillcolor"] = "#FFCC00"   # Color de relleno de los lugares
G.node_attr["fontname"] = "Arial"   # Fuente del texto de los lugares
G.edge_attr["arrowhead"] = "normal"   # Estilo de las flechas de las aristas
G.edge_attr["fontname"] = "Arial"   # Fuente del texto de las aristas

# Agregar lugares
G.add_node("Glucosa", label="Glucosa\n", fontsize=12)
G.add_node("Oxígeno", label="Oxígeno\n", fontsize=12)

# Agregar transición
G.add_node("Consumo de Oxígeno", shape="diamond", label="Consumo de Oxígeno", fontsize=12)

# Agregar arcos
G.add_edge("Glucosa", "Consumo de Oxígeno", label="-k1*Glucosa", fontcolor="#FF0000", fontsize=10)
G.add_edge("Oxígeno", "Consumo de Oxígeno", label="-k3*Oxígeno", fontcolor="#FF0000", fontsize=10)
G.add_edge("Consumo de Oxígeno", "Glucosa", label="k2*Consumo de Oxígeno", fontcolor="#009900", fontsize=10)
G.add_edge("Consumo de Oxígeno", "Oxígeno", label="k4*Consumo de Oxígeno", fontcolor="#009900", fontsize=10)

# Establecer el diseño
G.layout(prog="dot")

# Guardar el grafo en un archivo de imagen
graph_file = "red_petri.png"
G.draw(graph_file)

# Mostrar la imagen del grafo
Image(graph_file)