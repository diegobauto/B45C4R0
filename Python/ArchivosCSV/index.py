#from pruebas import pruebas_codigo_estudiante
import csv

data = []

def createFile():
    with open("Python\\ZZZ\\analisis_archivo.csv", "w", newline="") as File_W:
        File_W = csv.writer(File_W, delimiter="\t")
        File_W.writerows([["Fecha", "Concepto"]])
        File_W.writerows(data)

def datos(date, close):
    concepto = ""
    if close<1624:
        concepto = "MUY BAJO"
    elif close>=1624 and close<1854:
        concepto = "BAJO"
    elif close>=1854 and close<2084:
        concepto = "MEDIO"
    elif close>=2084 and close<2314:
        concepto = "ALTO"
    elif close>=2314:
        concepto = "MUY ALTO"
    data.append([date, concepto])
    
def solucion():
    prom = 0
    lista = []
    date_lowest_mean = ""
    lowest_mean = 0.0
    date_highest_mean = ""
    highest_mean = 0.0
    
    with open("Python\ZZZ\GOOG.csv", newline="") as File:
        reader = csv.reader(File)
        next(reader)
        for row in reader:
            datos(row[0], float(row[4]))
            prom = (float(row[2])+float(row[3]))/2
            lista.append((row[0], prom))
            
    lista = sorted(lista, key=lambda x:x[1])

    date_lowest_mean = lista[0][0]
    lowest_mean = lista[0][1]
    date_highest_mean = lista[-1][0]
    highest_mean = lista[-1][1]

    createFile()

    return date_lowest_mean, lowest_mean, date_highest_mean, highest_mean

solucion()
#pruebas_codigo_estudiante(solucion)