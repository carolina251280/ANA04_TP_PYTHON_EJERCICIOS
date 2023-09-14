# Generar para cada provincia una tupla con el nombre de la provincia, su 
# capital, su población y su PBI. Armar un diccionario donde cada valor sea 
# la tupla de una provincia y la clave sea el nombre de la provincia. Mostrar 
# para cada provincia su PBI per capita.


provincias = [
    ("Buenos Aires", "La Plata", 15428125, 420000),
    ("Catamarca", "San Fernando del Valle de Catamarca", 429556, ),
    ("Chaco","Resistencia",1142963,),
    ("Chubut", "Rawson", 603120,),
    ("Córdoba", "Córdoba", 3308876, 100000),
    ("Corrientes", "Corrientes",1197553, ),
    ("Entre Rios", "Paraná",1426426, ),
    ("Formosa","Formosa", 606041, ),
    ("Jujuy","San Salvador", 797955, ),
    ("La Pampa","Santa Rosa", 366022, ),
    ("La Rioja", "La Rioja", 384607, ),
    ("Mendoza", "Mendoza", 2014533, ),
    ("Misiones", "Misiones", 1280960, ),
    ("Neuquén","Neuquén", 726590, ),
    ("Río Negro", "Viedma", 762067, ),
    ("Salta","Salta", 1440672, ),
    ("San Juan", "San Juan", 818234 , ),
    ("San Luis", "San Luis", 540905 , ),
    ("Santa Cruz", "Río Gallegos", 333473, ),
    ("Santa Fe", "Santa Fe", 3556522, 90000),
    ("Santiago del Estero", "Santiago del Estero", 1054028, ),
    ("Tierra del Fuego", "Ushuaia", 190641, ),
    ("Antártida e Islas del Atlántico Sur","", 190641, ),
    ("Tucumán", "San Miguel", 1703186, ), 
]

dic_provincias = {}  

for provincia in provincias:
    nombre = provincia[0]  
    dic_provincias[nombre] = provincia  
print(dic_provincias)

for provincia, (provincia, capital, poblacion, pbi) in dic_provincias.items():
    pbi_per_capita = pbi / poblacion
    print(f"PBI per cápita de {provincia}: {pbi_per_capita}")