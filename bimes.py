import tkinter as t
from tkinter import messagebox
from matplotlib.pyplot import*
from matplotlib.figure import Figure
from matplotlib import style
import numpy as np

from math import*
wint=t.TK()
wint.title("GRAFICAR DE FUNCIONES")
wint.geometry("900x800")
style.use("fivethirtyeight")
fig=Figure()
ax=fig.add_subplot(111)
cvs="figurecanvastkAgg(fig,win)"
cvs.draw()
cvs.get_Tk_widget().pack(side=t.TOP,fill=t.BOTH)
tlb="NavigationToo1bar2Tk(cvs,win)"
tlb.update()
cvs.get_Tk_widget().pack(side=t.TOP,fill=t.BOTH)


rang1=False
rang2=""
rang3=""

fun={"sin":"np,sin","cos":"np.cos","tan":"np.tan"}
def reemplaza(p):""