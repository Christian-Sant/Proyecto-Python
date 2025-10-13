import matplotlib.pyplot as plt #type: ignore
from baseDeDatos import obtener_grafico 
#-----------------------------Creacion del grafico------------------------------#
def generar_graficas(correo,nombre_db="IncidenciasInformaticas.db"):
    
    por_categoria, por_estado, tiempos_resolucion = obtener_grafico(correo,nombre_db) #Obtener los datos de la base de datos

    
    plt.figure(figsize=(16, 5))

    plt.gcf().canvas.manager.set_window_title("Grafico de las Incidencias")# Titulo de la ventana

    #-----------------------------Grafico de Categoria------------------------------#
    plt.subplot(1, 3, 1)
    if por_categoria:
        categorias, counts_cat = zip(*por_categoria)
        plt.bar(categorias, counts_cat)
        for i, v in enumerate(counts_cat):
            plt.text(i, v + max(counts_cat)*0.01, str(v), ha='center', va='bottom', fontsize=8)
    else:
        plt.text(0.5, 0.5, 'No hay datos', ha='center')
        categorias, counts_cat = [], []

    plt.title("Incidencias por Categoría")
    plt.xlabel("Categoría")
    plt.ylabel("Cantidad")

    #-----------------------------Grafico de Estado------------------------------#
    plt.subplot(1, 3, 2)
    if por_estado:
        estados, counts_est = zip(*por_estado)
        plt.bar(estados, counts_est, color='orange')
        for i, v in enumerate(counts_est):
            plt.text(i, v + max(counts_est)*0.01, str(v), ha='center', va='bottom', fontsize=8)
    else:
        plt.text(0.5, 0.5, 'No hay datos', ha='center')
        estados, counts_est = [], []

    plt.title("Incidencias por Estado")
    plt.xlabel("Estado")

    #-----------------------------Grafico de Tiempo de resolucion------------------------------#
    plt.subplot(1, 3, 3)
    if tiempos_resolucion:
        plt.hist(tiempos_resolucion, bins=10, edgecolor='black')
        plt.title("Tiempo de resolución (días) — distribución")
        plt.xlabel("Días")
        plt.ylabel("Cantidad de incidencias")
    else:
        plt.text(0.5, 0.5, 'No hay incidencias cerradas con fecha de cierre', ha='center')

    plt.tight_layout()
    plt.show(block=False)
#-----------------------------FIN------------------------------#
