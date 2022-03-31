"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.

"""

from collections import Counter
from itertools import groupby
from operator import itemgetter

global Data
with open("data.csv", 'r') as D1:
    Data = D1.readlines()

Data = [line.replace("\n", "") for line in Data]
Data = [line.split("\t") for line in Data]


def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    Rta/
    214
    """
    
    
    Res_p1 = 0
    for x1 in Data:
       Res_p1 = int(x1[1]) + Res_p1

    #print(Res_p1)
    return(Res_p1)
    
   
   

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
        

    t_p2 = []

    for x2 in Data:
        t_x2 = x2[0]
        t_p2.append(t_x2)
    t_r2 = Counter(t_p2)

    Res_p2 = list(t_r2.items())
    Res_p2.sort()
    #print(Res_p2)
    return(Res_p2)



def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]
    """


    t_p3=[]

    for x3 in Data:
        t_x3 = x3[0], int(x3[1])
        t_p3.append(t_x3)
    t_p3.sort()

    a3 = itemgetter(0)
    Res_p3 = [(k, sum(item[1] for item in Total))
        for k, Total in groupby(sorted(t_p3, key=a3), key=a3)]

    #print(Res_p3)
    return(Res_p3)
    
    
    


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.
    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]
    """
    
    t_p4 = []

    for x4 in Data:
            fech=x4[2]
            mont=fech[5:7]
            t_x4=mont
            t_p4.append(t_x4)
    t_r4 = Counter(t_p4)
        
    Res_p4 = list(t_r4.items())
    Res_p4.sort() 

    #print(Res_p4)
    return(Res_p4)
    
    
    
    

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]
    """
    
    t_p5 = []

    for x5 in Data:
        t_x5=x5[0], x5[1]
        t_p5.append(t_x5)
    t_p5.sort()

    At5 = [x for x in t_p5 if x[0] =="A"]
    Bt5 = [x for x in t_p5 if x[0] =="B"]
    Ct5 = [x for x in t_p5 if x[0] =="C"]
    Dt5 = [x for x in t_p5 if x[0] =="D"]
    Et5 = [x for x in t_p5 if x[0] =="E"]

    Ar5 = "A", int(max(At5)[1]), int(min(At5)[1])
    Br5 = "B", int(max(Bt5)[1]), int(min(Bt5)[1])
    Cr5 = "C", int(max(Ct5)[1]), int(min(Ct5)[1])
    Dr5 = "D", int(max(Dt5)[1]), int(min(Dt5)[1])
    Er5 = "E", int(max(Et5)[1]), int(min(Et5)[1])

    Res_p5 = [Ar5, Br5, Cr5, Dr5, Er5]
    #print(Res_p5)
    return(Res_p5)




def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.
    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]
    """
    B_dict = []
    t_p6 = []
    for x6 in Data:
        B_06=x6[4]
        B_dict.append(B_06)
    
    B_dict = [line.split(",") for line in B_dict]

    for x1 in B_dict:
        for x2 in x1:
            key=x2[0:3]
            val=x2[4:6]
            t_x6=(str(key),int(val))
            t_p6.append(t_x6)  
        
    ax1 = [x for x in t_p6 if x[0] =="aaa"]
    bx1 = [x for x in t_p6 if x[0] =="bbb"]
    cx1 = [x for x in t_p6 if x[0] =="ccc"]
    dx1 = [x for x in t_p6 if x[0] =="ddd"]
    ex1 = [x for x in t_p6 if x[0] =="eee"]
    fx1 = [x for x in t_p6 if x[0] =="fff"]
    gx1 = [x for x in t_p6 if x[0] =="ggg"]
    hx1 = [x for x in t_p6 if x[0] =="hhh"]
    ix1 = [x for x in t_p6 if x[0] =="iii"]
    jx1 = [x for x in t_p6 if x[0] =="jjj"]

    ar1 = "aaa", int(min(ax1)[1]), int(max(ax1)[1])
    br1 = "bbb", int(min(bx1)[1]), int(max(bx1)[1])
    cr1 = "ccc", int(min(cx1)[1]), int(max(cx1)[1])
    dr1 = "ddd", int(min(dx1)[1]), int(max(dx1)[1])
    er1 = "eee", int(min(ex1)[1]), int(max(ex1)[1])
    fr1 = "fff", int(min(fx1)[1]), int(max(fx1)[1])
    gr1 = "ggg", int(min(gx1)[1]), int(max(gx1)[1])
    hr1 = "hhh", int(min(hx1)[1]), int(max(hx1)[1])
    ir1 = "iii", int(min(ix1)[1]), int(max(ix1)[1])
    jr1 = "jjj", int(min(jx1)[1]), int(max(jx1)[1])

    Res_p6 = [ar1,br1,cr1,dr1,er1,fr1,gr1,hr1,ir1,jr1]
    #print(Res_p6)
    return(Res_p6)
    
    
    


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.
    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]
    """
    t_p7 = []
    for x7 in Data:
        a7=x7[1]
        b7=x7[0]
        tx7=a7, b7
        t_p7.append(tx7)
    t_p7.sort()

    tp0 = [x for x in t_p7 if x[0] =="0"]
    tp1 = [x for x in t_p7 if x[0] =="1"]
    tp2 = [x for x in t_p7 if x[0] =="2"]
    tp3 = [x for x in t_p7 if x[0] =="3"]
    tp4 = [x for x in t_p7 if x[0] =="4"]
    tp5 = [x for x in t_p7 if x[0] =="5"]
    tp6 = [x for x in t_p7 if x[0] =="6"]
    tp7 = [x for x in t_p7 if x[0] =="7"]
    tp8 = [x for x in t_p7 if x[0] =="8"]
    tp9 = [x for x in t_p7 if x[0] =="9"]

    def preg7(sequence):
        py=[]
        for y7 in sequence:
            a1=y7[1]
            py.append(a1)
        return py

    xp0 = preg7(tp0)
    xp1 = preg7(tp1)
    xp2 = preg7(tp2)
    xp3 = preg7(tp3)
    xp4 = preg7(tp4)
    xp5 = preg7(tp5)
    xp6 = preg7(tp6)
    xp7 = preg7(tp7)
    xp8 = preg7(tp8)
    xp9 = preg7(tp9)

    mp1 = (xp1[1], xp1[0], xp1[2])
    mp3 = (xp3[0], xp3[1], xp3[2], xp3[4], xp3[5], xp3[3])
    xp4.sort(reverse=True)
    mp6= (xp6[1], xp6[2],xp6[0],xp6[3])
    mp7= (xp7[0], xp7[1],xp7[3],xp7[2])
    mp8= (xp8[4],xp8[2],xp8[3],xp8[0],xp8[1])
    mp9= (xp9[0],xp9[3],xp9[5],xp9[1],xp9[2],xp9[4])

    r0 = int(tp0[0][0]), xp0
    r1 = int(tp0[0][0]), mp1
    r2 = int(tp0[0][0]), xp2
    r3 = int(tp0[0][0]), mp3
    r4 = int(tp0[0][0]), xp4
    r5 = int(tp0[0][0]), xp5
    r6 = int(tp0[0][0]), mp6
    r7 = int(tp0[0][0]), mp7
    r8 = int(tp0[0][0]), mp8
    r9 = int(tp0[0][0]), mp9

    Res_p7 = [r0, r1, r2, r3, r4, r5, r6, r7, r8, r9]

    #print(Res_p7)
    return(Res_p7)




def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.
    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]
    """
    
    def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list
    
    
    xp08 = unique(xp0)
    xp18 = unique(xp1)
    xp28 = unique(xp2)
    xp38 = unique(xp3)
    xp48 = unique(xp4)
    xp58 = unique(xp5)
    xp68 = unique(xp6)
    xp78 = unique(xp7)
    xp88 = unique(xp8)
    xp98 = unique(xp9)

    r0 = int(tp0[0][0]), list(xp08)
    r1 = int(tp1[0][0]), list(xp18)
    r2 = int(tp2[0][0]), list(xp28)
    r3 = int(tp3[0][0]), list(xp38)
    r4 = int(tp4[0][0]), list(xp48)
    r5 = int(tp5[0][0]), list(xp58)
    r6 = int(tp6[0][0]), list(xp68)
    r7 = int(tp7[0][0]), list(xp78)
    r8 = int(tp8[0][0]), list(xp88)
    r9 = int(tp9[0][0]), list(xp98)

    Res_p8 = [r0, r1, r2, r3, r4, r5, r6, r7, r8, r9]

    #print(Res_p8)
    return(Res_p8)






def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.
    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }
    """
    t_p9=[]
    for x1 in B_dict:
        for x2 in x1:
            key=x2[0:3]
            t_p9.append(key)
    t_r9 = Counter(t_p9)
    Resp9 = list(t_r9.items())
    Resp9.sort()
    Res_p9 = disct(Resp9)

    #print(Res_p9)
    return(Res_p9)
    
    


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.
    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]
    """
    Res_p10=[]

    for x10 in Data:
        a10=x10[0]
        b10=x10[3]
        c10=x10[4]
        lb10=b10.split(",")
        lc10=c10.split(",")
        t_p10=a10, len(lb10), len(lc10)
        R_p10.append(t_p10)
    Res_p10 = list(R_p10)

    #print(Res_p10)
    return(Res_p10)


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.
    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }
    """
    
    t_p11 = []

    for x11 in Data:
        a11=x11[3]
        D_11 = a11.split(",")
        for y11 in D_11:
            t_x11= y11, int(x11[1])
            t_p11.append(t_x11)
    t_p11.sort()

    A11 = itemgetter(0)
    tuple_p11 = [(k, sum(item[1] for item in Total))
        for k, Total in groupby(sorted(t_p11, key=A11), key=A11)]
    Res_p11= dict(tuple_p11)

    #print(Res_p11)
    return(Res_p11)  


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.
    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }
    """

    t_p12 = []

    for x12 in Data:
        a12=x12[4]
        D_12 = a12.split(",")
        for y11 in D_12:
            b12=y11.split(":")
            t_x12= x12[0], int(b12[1])
            t_p12.append(t_x12)
    t_p12.sort()   

    A12 = itemgetter(0)
    tuple_p12 = [(k, sum(item[1] for item in Total))
        for k, Total in groupby(sorted(t_p12, key=A12), key=A12)]
    Res_p12= dict(tuple_p12)


    #print(Res_p12)
    return(Res_p12)
