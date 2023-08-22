from tkinter import *

aplicacion = Tk()

aplicacion.geometry('1020x630+0+0')

aplicacion.resizable(0, 0)

aplicacion.title('Mi Restaurante - Sistema de Facturacion')

aplicacion.config(bg='burlywood')

panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

etiqueta_titulo = Label(panel_superior, text='Sistema de Facturacion', fg='azure4',
                        font=('Dosis', 58), bg='burlywood', width=27)

etiqueta_titulo.grid(row=0, column=0)

panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT)
panel_costos.pack(side=BOTTOM)

panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)


panel_derecha = Frame(aplicacion, bd=1,  relief=FLAT)
panel_derecha.pack(side=RIGHT)

panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()

panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()

lista_comidas = ['pollo', 'arroz chino', 'pescado', 'salmon', 'otacos', 'empanadas']
lista_bebidas = ['agua', 'agua panela', 'soda', 'limonada', 'vino']
lista_postres = ['helado', 'fruta', 'brownie','flan']

variables_comida = []
cuadros_comida = []
texto_comida = []

contador = 0
for comida in lista_comidas:

    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, text=comida.title(), font=('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_comida[contador] )
    comida.grid(row=contador, column=0, sticky=W)

    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador]= Entry(panel_comidas, font=('Dosis', 18, 'bold'), bd=1, width=6, state=DISABLED, textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador, column=1)

    contador += 1


variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_bebida[contador] )
    bebida.grid(row=contador, column=0, sticky=W)

    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador]= Entry(panel_bebidas, font=('Dosis', 18, 'bold'), bd=1, width=6, state=DISABLED, textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador, column=1)


    contador += 1

variables_postres = []
cuadros_postres = []
texto_postres = []
contador = 0
for postre in lista_postres:
    variables_postres.append(IntVar())
    comida = Checkbutton(panel_postres, text=postre.title(), font=('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_postres[contador])
    comida.grid(row=contador, column=0, sticky=W)

    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador]= Entry(panel_postres, font=('Dosis', 18, 'bold'), bd=1, width=6, state=DISABLED, textvariable=texto_postres[contador])
    cuadros_postres[contador].grid(row=contador, column=1)


    contador += 1

var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()


etiqueta_costo_comida = Label(panel_costos, text='Costo Comida', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1)


etiqueta_costo_bebida = Label(panel_costos, text='Costo Bebida', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_costo_bebida.grid(row=0, column=0)

texto_costo_bebida = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1)

etiqueta_costo_postre = Label(panel_costos, text='Costo Postre', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_costo_postre.grid(row=1, column=0)

texto_costo_postre = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_costo_postre)
texto_costo_postre.grid(row=1, column=1)

etiqueta_subtotal = Label(panel_costos, text='Subtotal', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_subtotal.grid(row=1, column=2)

texto_subtotal = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_subtotal)
texto_subtotal.grid(row=1, column=3)

etiqueta_impuestos = Label(panel_costos, text='Impuestos', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_impuestos.grid(row=1, column=2)

texto_impuestos = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_impuesto)
texto_impuestos.grid(row=1, column=3)

etiqueta_total = Label(panel_costos, text='Total', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_total)
texto_total.grid(row=2, column=3)

aplicacion.mainloop()