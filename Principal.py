from tkinter import *
import time
import threading

#ventana inicial
ventana=Tk()

ventana.geometry("700x450")
ventana.title("Curiosidades Numericas")

#Variable globales
variableA=IntVar()
variableB=IntVar()
variableC=IntVar()
variableD=IntVar()
variableE=IntVar()
variableF=IntVar()

global lineas
global lineas2
global lineas3
global lineas4
global lineas5
global nomcodigo

lineas=[]
lineas2=[]
lineas3=[]
lineas4=[]
lineas5=[]
lineas6=[]
nomcodigo=""


#Esta crea la segunda ventana con todos sus elementos
def ConjeturaDeGoldbach():
    ventana.withdraw() 
    ventana2 = Toplevel()
    ventana2.geometry("700x450")

    etiqueta=Label(ventana2,text="La Conjetura De Goldbach")
    etiqueta.place(x=260,y=15)

    texto=Text(ventana2,width=70,height=3)
    texto.insert(INSERT,"Todo número par mayor que 2 puede escribirse como suma de dos números primos.")
    texto.place(x=60,y=45)

    Numero=Label(ventana2,text="Numero =")
    Numero.place(x=20,y=200)

    E1=Entry(ventana2,textvariable=variableA,width=10)
    E1.place(x=85,y=200)

    EtiquetaCodigo=Label(ventana2,text="Codigo")
    EtiquetaCodigo.place(x=200,y=310)

    codigo=Listbox(ventana2,width=75,height=6)
    codigo.place(x=200,y=330)

    EtiquetaVariable=Label(ventana2,text="Variables")
    EtiquetaVariable.place(x=480,y=130)

    variables=Listbox(ventana2,width=25,height=10)
    variables.place(x=480,y=150)

    EtiquetaResultado=Label(ventana2,text="Resulado")
    EtiquetaResultado.place(x=260,y=130)

    resultado=Listbox(ventana2,width=25,height=10)
    resultado.place(x=260,y=150)

    #cargando el archivo en una lista...
    def cargaLista(LInstruccion,nomcodigo):
        f=open(str(nomcodigo)+".py", mode="r")
        contador = 0
        linea = f.readline()
        while linea != "":
            codigo.insert(contador, linea)
            LInstruccion.append(linea)
            linea = f.readline()
            contador = contador+1
        f.close()
        return LInstruccion   

    nomcodigo="la conjetura de Goldbach"
    codigoGold=[]
    codigoGold=cargaLista(codigoGold,nomcodigo)
 

    #esta funcion le asigna el valor de la variableA a n
    #entradas= ninguna
    #salidas= la funcion goldbach(n)
    def gold():
        n=variableA.get()
        return goldbach(n)

    #esta funcion toma el numero, si este es impar o si es mayor de 2, avisa al usuario, sino, se lo manda a goldbach_aux(n,2,2)
    #entradas= numero n
    #salidas= si es impar o mayor de 2 un string, sino, goldbach_aux(n,2,2)
    def goldbach(n):
        global lineas
        lineas=lineas+[0,1]
        variables.insert(0,"goldbach(n)")
        variables.insert(1,"n"+"="+str(n))
        if n%2!=0:
            lineas=lineas+[2]
            w.start()
            return variables.insert(2,"tiene que ser numero par")
        else:
            lineas=lineas+[3,4]
            if n<=2:
                lineas=lineas+[5]
                w.start()
                return variables.insert(2,"el numero tiene que ser mayor que 2")
            else:
                lineas=lineas+[6,7]
                return goldbach_aux(n,2,2)

    #esta funcion devuelve las diferente formas en que un numero puede ser el resultado de dos numeros primos
    #entradas= numero n
    #          a = 2
    #          b = 2
    #salidas= hilera
    def goldbach_aux(n,a,b):
        global lineas
        lineas=lineas+[9,10]
        variables.insert(END,"goldbach_aux("+str(n)+","+str(a)+","+str(b)+")")
        variables.insert(END,"n"+"="+str(n))
        variables.insert(END,"a"+"="+str(a))
        variables.insert(END,"b"+"="+str(b))
        if a>=n:
            lineas=lineas+[11]
            w.start()
            return resultado.insert(END,"")
        elif a+b==n:
            lineas=lineas+[12,13,14,15]
            hilera=str(n)+" = "+str(a)+" + "+str(b)
            resultado.insert(END,hilera)
            return goldbach_aux(n,primo((a+1),2),1)
        elif a+b>n:
            lineas=lineas+[12,16,17]
            return goldbach_aux(n,a+1,1)
        else:
            lineas=lineas+[12,16,18,19]
            if a==1:
                lineas=lineas+[20]
                return goldbach_aux(n,primo(a,2),primo(b,2))
            else:
                lineas=lineas+[21,22]
                return goldbach_aux(n,a,primo(b+1,2))

    #La funcion me dice si n es primo
    #entradas= numero n
    #          contador(c) comenzando en 2
    #salidas= numero n
    def primo(n,c):
        global lineas
        lineas=lineas+[24,25]
        variables.insert(END,"def primo("+str(n)+","+str(c)+")")
        variables.insert(END,"n= "+str(n))
        variables.insert(END,"c= "+str(c))
        if c>n//2:
            lineas=lineas+[26]
            return n
        elif n%c==0:
            lineas=lineas+[27,28]
            return primo(n+1,c)
        else:
            lineas=lineas+[27,29,30]
            return primo(n,c+1)

    #inserta el codigo en un listbox y lo va señalando segun se ejecuta
    #entradas: lista con el codigo
    #salidas: la linea que se ejecuta, subrayada
    def cargaMueve(lineas):
        for linact in lineas:
            codigo.see(linact)
            hilo = (threading.currentThread(), lineas[linact])
            time.sleep (1)
            codigo.selection_set(linact)
            time.sleep (0.5)
            codigo.selection_clear(linact)

    #hilo
    w=threading.Thread(target=lambda:cargaMueve(lineas), name="cc")
    

    #elimina la ventana actual y regresa a la anterior
    def ventanaAnterior():
        ventana2.destroy() 
        ventana.deiconify()

    VenAnt=Button(ventana2,text="Anterior",width=10,command=ventanaAnterior)
    VenAnt.place(x=10,y=400)
 
    ejecutar=Button(ventana2,text="ejecutar",width=20,command=gold)
    ejecutar.place(x=50,y=260)

#crea la ventana para los numeros amigos y todo sus componentes
    def NumsAmigos():
        ventana2.withdraw() 
        ventana3 = Toplevel()
        ventana3.geometry("700x450")

        texto=Text(ventana3,width=70,height=3)
        texto.insert(INSERT,"Dos numeros son considerados amigos si y solo si la suma de los divisores del numero A son igual al numero B y viceversa")
        texto.place(x=60,y=45)

        etiqueta=Label(ventana3,text="Numeros Amigos")
        etiqueta.place(x=260,y=15)

        Numero=Label(ventana3,text="A =")
        Numero.place(x=50,y=175)

        Numero2=Label(ventana3,text="B =")
        Numero2.place(x=50,y=210)

        E1=Entry(ventana3,textvariable=variableB,width=10)
        E1.place(x=85,y=175)

        E2=Entry(ventana3,textvariable=variableC,width=10)
        E2.place(x=85,y=210)

        EtiquetaCodigo=Label(ventana3,text="Codigo")
        EtiquetaCodigo.place(x=200,y=310)

        codigo=Listbox(ventana3,width=75,height=6)
        codigo.place(x=200,y=330)

        EtiquetaVariable=Label(ventana3,text="Variables")
        EtiquetaVariable.place(x=480,y=130)

        variables=Listbox(ventana3,width=25,height=10)
        variables.place(x=480,y=150)

        EtiquetaResultado=Label(ventana3,text="Resulado")
        EtiquetaResultado.place(x=260,y=130)

        resultado=Listbox(ventana3,width=35,height=10)
        resultado.place(x=260,y=150)

        #cargando el archivo en una lista...
        def cargaLista(LInstruccion,nomcodigo):
            f=open(str(nomcodigo)+".py", mode="r")
            contador = 0
            linea = f.readline()
            while linea != "":
                codigo.insert(contador, linea)
                LInstruccion.append(linea)
                linea = f.readline()
                contador = contador+1
            f.close()
            return LInstruccion   

        nomcodigo="numeros amigos"
        codigoamigos=[]
        codigoamigos=cargaLista(codigoamigos,nomcodigo)

        #Toma los valore de variableB y variableC y los asigna
        #entradas= ninguna
        #salidas= NumerosAmigos(a,b)
        def NA():
            a=variableB.get()
            b=variableC.get()
            variables.insert(END,"def NA():")
            return NumerosAmigos(a,b)

        #toma los valores y si la suma de los divisores de a es igual a b y viceversa, los imprime en las listbox
        #entradas= a (numero)
        #          b (numero)
        #salidas= imprime los valores en las listbox o indica que los numeros no son amigos
        def NumerosAmigos(a,b):
            global lineas2
            lineas2=lineas2+[0,1]
            variables.insert(END,"def NumerosAmigos("+str(a)+","+str(b)+")")
            variables.insert(END,"a= "+str(a))
            variables.insert(END,"b= "+str(b))
            if divisores(a,1,0)==b and divisores(b,1,0)==a:
                variables.insert(END,str(divisores(a,1,0))+"==b")
                variables.insert(END,str(divisores(b,1,0))+"==a")
                resultado.insert(END,dividendos(a,2,""))
                resultado.insert(END,dividendos(b,2,""))
                resultado.insert(END,sumas(a,b,2,""))
                lineas2=lineas2+[2,3,4,5]
                w.start()
                return resultado.insert(END,sumas(b,a,2,""))
            else:
                lineas2=lineas2+[6,7]
                w.start()
                return resultado.insert(0,"no son amigos")

        #saca la suma de los divisores del numero
        #entradas= num(numero)
        #          cont(inicializado en 1)
        #          res(numero
        #
        def divisores(num,cont,res):
            global lineas2
            lineas2=lineas2+[9,10]
            variables.insert(END,"def divisores("+str(num)+","+str(cont)+","+str(res)+")")
            variables.insert(END,"num= "+str(num))
            variables.insert(END,"cont= "+str(cont))
            variables.insert(END,"res= "+str(res))
            if cont>num//2:
                lineas2=lineas2+[11]
                return res
            elif num%cont==0:
                lineas2=lineas2+[12,13]
                return divisores(num,cont+1,res+cont)
            else:
                lineas2=lineas2+[12,14,15]
                return divisores(num,cont+1,res)

        #muestra los divisores del numero
        #entradas= a (numero)
        #          cont (contador inicializado en 1)
        #          hilera(string vacio)
        #salidas= los divisores del numero
        def dividendos(a,cont,hilera):
            global lineas2
            lineas2=lineas2+[17,18]
            variables.insert(END,"def dividendos("+str(a)+","+str(cont)+","+str(hilera)+")")
            variables.insert(END,"a= "+str(a))
            variables.insert(END,"cont= "+str(cont))
            variables.insert(END,"hilera= "+str(hilera))
            if cont>a//2:
                lineas2=lineas2+[19]
                return str(a)+": "+hilera[1:]
            else:
                lineas2=lineas2+[20,21]
                if a%cont==0:
                    lineas2=lineas2+[22]
                    return dividendos(a,cont+1,hilera+","+str(a//cont))
                else:
                    lineas2=lineas2+[23,24]
                    return dividendos(a,cont+1,hilera)

        #muestra la suma de los divisores del numero
        #entradas= a (numero)
        #          b (numero)
        #          cont (contador inicializado en 1)
        #          hilera(string vacio)
        #salidas= string con la suma de los divisores del numero
        def sumas(a,b,cont,hilera):
            global lineas2
            lineas2=lineas2+[26,27]
            variables.insert(END,"def sumas("+str(a)+","+str(a)+","+str(cont)+","+str(hilera)+")")
            variables.insert(END,"a= "+str(a))
            variables.insert(END,"b= "+str(b))
            variables.insert(END,"cont= "+str(cont))
            variables.insert(END,"hilera= "+str(hilera))
            if cont>a//2:
                lineas2=lineas2+[28]
                return str(b)+"= "+hilera[1:]
            else:
                lineas2=lineas2+[29,30]
                if a%cont==0:
                    lineas2=lineas2+[31,32]
                    hilera=hilera+"+"+str(a//cont)
                    return sumas(a,b,cont+1,hilera)
                else:
                    lineas2=lineas2+[33,34]
                    return sumas(a,b,cont+1,hilera)
        #inserta el codigo en un listbox y lo va señalando segun se ejecuta
        #entradas: lista con el codigo
        #salidas: la linea que se ejecuta, subrayada
        def cargaMueve(lineas2):
            for linact in lineas2:
                codigo.see(linact)
                hilo = (threading.currentThread(), lineas[linact])
                time.sleep (1)
                codigo.selection_set(linact)
                time.sleep (0.5)
                codigo.selection_clear(linact)

        #hilo
        w=threading.Thread(target=lambda:cargaMueve(lineas), name="cc")

        #elimina la ventana actual y regresa a la anterior
        def ventanaAnterior():
            ventana3.destroy() 
            ventana2.deiconify()

        VenAnt=Button(ventana3,text="Anterior",width=10,command=ventanaAnterior)
        VenAnt.place(x=10,y=400)
 
        ejecutar=Button(ventana3,text="ejecutar",width=20,command=NA)
        ejecutar.place(x=50,y=260)

#crea la ventana para el triangulo de pascal y todo sus componentes
        def TrianguloP():
            ventana3.withdraw() 
            ventana4 = Toplevel()
            ventana4.geometry("700x450")

            texto=Text(ventana4,width=70,height=3)
            texto.insert(INSERT,"Es un árbol invertido o un triángulo donde todos sus bordes son 1 y los valores internos son la suma de los dos valores que se encuentren justo por encima de él.")
            texto.place(x=60,y=45)

            etiqueta=Label(ventana4,text="Triangulo de Pascal")
            etiqueta.place(x=260,y=15)

            Numero=Label(ventana4,text="Numero =")
            Numero.place(x=20,y=200)

            E1=Entry(ventana4,textvariable=variableD,width=10)
            E1.place(x=85,y=200)

            EtiquetaCodigo=Label(ventana4,text="Codigo")
            EtiquetaCodigo.place(x=200,y=310)

            codigo=Listbox(ventana4,width=75,height=6)
            codigo.place(x=200,y=330)

            EtiquetaVariable=Label(ventana4,text="Variables")
            EtiquetaVariable.place(x=480,y=130)

            variables=Listbox(ventana4,width=25,height=10)
            variables.place(x=480,y=150)

            EtiquetaResultado=Label(ventana4,text="Resulado")
            EtiquetaResultado.place(x=260,y=130)

            resultado=Listbox(ventana4,width=25,height=10)
            resultado.place(x=260,y=150)

            #cargando el archivo en una lista...
            def cargaLista(LInstruccion,nomcodigo):
                f=open(str(nomcodigo)+".py", mode="r")
                contador = 0
                linea = f.readline()
                while linea != "":
                    codigo.insert(contador, linea)
                    LInstruccion.append(linea)
                    linea = f.readline()
                    contador = contador+1
                f.close()
                return LInstruccion   

            nomcodigo="Triangulo de Pascal"
            codigoamigos=[]
            codigoamigos=cargaLista(codigoamigos,nomcodigo)

            #Toma los valore de variableD y lo asigna
            #entradas= ninguna
            #salidas= TP(num)
            def TrianguloDePascal():
                num=variableD.get()
                variables.insert(END,"def TrianguloDePascal():")
                return TP(num)

            #entradas= num(numero)
            #salidas= si num es uno sale un "1", sino, TP_aux(num,0,num,0,"")
            def TP(num):
                global lineas3
                lineas3=lineas3+[1,2]
                variables.insert(END,"def TP("+str(num)+")")
                variables.insert(END,"num= "+str(num))
                if num==0:
                    lineas3=lineas3+[2]
                    w.start()
                    return 1
                else:
                    lineas=lineas3+[3,4]
                    return TP_aux(num,0,num,0,"")

            #crea el triangulo de pascal
            #entradas= num (numero)
            #          num2 (numero)
            #          num3 (numero)
            #          k= contador inicializado en 0
            #          fila= string vacio
            #salidas= triangulo de pascal
            def TP_aux(num,num2,num3,k,fila):
                global lineas3
                lineas=lineas3+[6,7]
                variables.insert(END,"def TP_aux("+str(num)+","+str(num2)+str(num3)+","+str(k)+str(fila)+")")
                variables.insert(END,"num= "+str(num))
                variables.insert(END,"num2= "+str(num2))
                variables.insert(END,"num3= "+str(num3))
                variables.insert(END,"k= "+str(k))
                variables.insert(END,"fila= "+str(fila))
                if num2>num:
                    lineas3=lineas3+[8]
                    w.start()
                    return fila
                else:
                    lineas3=lineas3+[9,10]
                    if num2==0:
                        lineas=lineas+[11,12]
                        resultado.insert(END," "*num3+"1")
                        return TP_aux(num,num2+1,num3-1,k,fila)
                    elif k==0:
                        lineas3=lineas3+[13,14,15]
                        fila="1-"+fila
                        return TP_aux(num,num2,num3,k+1,fila)
                    elif k==num2:
                        lineas3=lineas3+[13,16,17,18,19]
                        fila=fila+"1"
                        resultado.insert(END," "*num3+fila)
                        return TP_aux(num,num2+1,num3-1,0,"")
                    else:
                        lineas3=lineas3+[13,16,20,21,22]
                        fila=fila+str(Fact(num2)//(Fact(k)*Fact((num2-k))))
                        return TP_aux(num,num2,num3,k+1,fila+"-")

            #saca el factorial
            #entradas= num (numero)
            # salidas= factorial del numero
            def Fact(num):
                global lineas3
                lineas3=lineas3+[24,25]
                variables.insert(END,"def Fact("+str(num)+")")
                variables.insert(END,"num= "+str(num))
                if num==0 or num==1:
                    lineas3=lineas3+[26]
                    return 1
                else:
                    lineas3=lineas3+[27,28]
                    return num*Fact(num-1)

            #inserta el codigo en un listbox y lo va señalando segun se ejecuta
        #entradas: lista con el codigo
        #salidas: la linea que se ejecuta, subrayada
            def cargaMueve(lineas3):
                for linact in lineas3:
                    codigo.see(linact)
                    hilo = (threading.currentThread(), lineas[linact])
                    time.sleep (1)
                    codigo.selection_set(linact)
                    time.sleep (0.5)
                    codigo.selection_clear(linact)

            #hilo
            w=threading.Thread(target=lambda:cargaMueve(lineas), name="cc")

            

            #elimina la ventana actual y regresa a la anterior
            def ventanaAnterior():
                ventana4.destroy() 
                ventana3.deiconify()

            VenAnt=Button(ventana4,text="Anterior",width=10,command=ventanaAnterior)
            VenAnt.place(x=10,y=400)
 
            ejecutar=Button(ventana4,text="ejecutar",width=20,command=TrianguloDePascal)
            ejecutar.place(x=50,y=260)

#crea la ventana para los numeros triangulares y todo sus componentes
            def NumeroTriangular():
                ventana4.withdraw() 
                ventana5 = Toplevel()
                ventana5.geometry("700x450")

                texto=Text(ventana5,width=70,height=3)
                texto.insert(INSERT,"Es aquel que puede recomponerse en la forma de un triángulo equilátero (por convención, el primer número triangular es el 1)")
                texto.place(x=60,y=45)

                etiqueta=Label(ventana5,text="Numeros Triangulares")
                etiqueta.place(x=260,y=15)

                Numero=Label(ventana5,text="Numero =")
                Numero.place(x=20,y=200)

                E1=Entry(ventana5,textvariable=variableE,width=10)
                E1.place(x=85,y=200)

                EtiquetaCodigo=Label(ventana5,text="Codigo")
                EtiquetaCodigo.place(x=200,y=310)

                codigo=Listbox(ventana5,width=75,height=6)
                codigo.place(x=200,y=330)

                EtiquetaVariable=Label(ventana5,text="Variables")
                EtiquetaVariable.place(x=480,y=130)

                variables=Listbox(ventana5,width=25,height=10)
                variables.place(x=480,y=150)

                EtiquetaResultado=Label(ventana5,text="Resulado")
                EtiquetaResultado.place(x=260,y=130)

                resultado=Listbox(ventana5,width=25,height=10)
                resultado.place(x=260,y=150)

                #cargando el archivo en una lista...
                def cargaLista(LInstruccion,nomcodigo):
                    f=open(str(nomcodigo)+".py", mode="r")
                    contador = 0
                    linea = f.readline()
                    while linea != "":
                        codigo.insert(contador, linea)
                        LInstruccion.append(linea)
                        linea = f.readline()
                        contador = contador+1
                    f.close()
                    return LInstruccion   

                nomcodigo="Numero Triangular"
                codigoamigos=[]
                codigoamigos=cargaLista(codigoamigos,nomcodigo)

                #toma el valor de variableE y lo asigna
                #entradas= ninguna
                #salidas= NumTriangular_aux(num,1)
                def NumTriangular():
                    global lineas4
                    lineas4=lineas4+[0,1]
                    variables.insert(END,"def NumTriangular():")
                    num=variableE.get()
                    return NumeroTriangular_aux(num,1)

                #dice si un numero no es triangular, sino, se lo manda a NT(num,espacios,cont1,cont2,hilera)
                #entradas= num(numero)
                #          cont= contador inicializado en 1
                #salidas= string si el numero no es triangular, sino, NT(num,espacios,cont1,cont2,hilera)
                def NumeroTriangular_aux(num,cont):
                    global lineas4
                    lineas4=lineas4+[3,4]
                    variables.insert(END,"def NumTriangular_aux("+str(num)+","+str(cont)+")")
                    variables.insert(END,"num= "+str(num))
                    variables.insert(END,"cont= "+str(cont))
                    if cont==num:
                        lineas4=lineas4+[5]
                        w.start()
                        return resultado.insert(END,str(num)+"= no es triangular")
                    elif (cont*(cont+1))//2==num:
                        lineas4=lineas4+[6,7]
                        return NT(num,cont,1,1,"")
                    lineas4=lineas4+[8]
                    return NumeroTriangular_aux(num,cont+1)

                #crea el triangulo equilatero
                #entradas= num(numero)
                #          espacios(numero)
                #          con1=contador inicializado en 1
                #          con2=contador inicializado en 1
                #          hilera, string vacia
                #salida= un triangulo equilatero formado de Os
                def NT(num,espacios,cont1,cont2,hilera):
                    global lineas4
                    lineas4=lineas4+[10,11]
                    variables.insert(END,"def NT("+str(num)+","+str(espacios)+str(cont1)+","+str(cont2)+str(hilera)+")")
                    variables.insert(END,"num= "+str(num))
                    variables.insert(END,"espacios= "+str(espacios))
                    variables.insert(END,"cont1= "+str(cont1))
                    variables.insert(END,"cont2= "+str(cont2))
                    variables.insert(END,"hilera= "+str(hilera))
                    if num==1:
                        lineas4=lineas4+[12]
                        w.start()
                        return resultado.insert(END,"o")
                    else:
                        lineas4=lineas4+[13,14]
                        if espacios==0:
                            lineas4=lineas4+[15]
                            w.start()
                            return hilera
                        elif cont2>cont1:
                            lineas4=lineas4+[16,17,18,19]
                            hilera=" "*espacios+hilera
                            resultado.insert(END,hilera)
                            return NT(num,espacios-1,cont1+1,1,"")
                        else:
                            lineas4=lineas4+[16,20,21,22]
                            hilera=hilera+"o "
                            return NT(num,espacios,cont1,cont2+1,hilera)

                #inserta el codigo en un listbox y lo va señalando segun se ejecuta
                #entradas: lista con el codigo
                #salidas: la linea que se ejecuta, subrayada
                def cargaMueve(lineas4):
                    for linact in lineas4:
                        codigo.see(linact)
                        hilo = (threading.currentThread(), lineas[linact])
                        time.sleep (1)
                        codigo.selection_set(linact)
                        time.sleep (0.5)
                        codigo.selection_clear(linact)

                #hilo
                w=threading.Thread(target=lambda:cargaMueve(lineas), name="cc")

                #elimina la ventana actual y regresa a la anterior
                def ventanaAnterior():
                    ventana5.destroy() 
                    ventana4.deiconify()

                VenAnt=Button(ventana5,text="Anterior",width=10,command=ventanaAnterior)
                VenAnt.place(x=10,y=400)

                ejecutar=Button(ventana5,text="ejecutar",width=20,command=NumTriangular)
                ejecutar.place(x=50,y=260)

#crea la ventana para las curiosidades del numero 153 y todo sus componentes
                def Curiosidades153():
                    ventana5.withdraw() 
                    ventana6 = Toplevel()
                    ventana6.geometry("700x450")

                    texto=Text(ventana6,width=70,height=6)
                    texto.insert(INSERT,"1.- Es el número más pequeño que puede ser expresado como la suma de los cubos de sus dígitos")
                    texto.insert(INSERT,"  2.- La suma de sus dígitos es un cuadrado perfecto")
                    texto.insert(INSERT,"  3.- Puede ser expresado como la suma de todos los números enteros del 1 al 17")
                    texto.insert(INSERT,"  4.- Como el 153 es un numero triangular y su inverso 351 tambien es un numero triangular (suma del 1 al 26), decimos que es un numero invertible")
                    texto.place(x=60,y=28)

                    etiqueta=Label(ventana6,text="Curiosidades del 153")
                    etiqueta.place(x=260,y=5)

                    Numero=Label(ventana6,text="curiosidad=")
                    Numero.place(x=30,y=200)

                    E1=Entry(ventana6,textvariable=variableF,width=10)
                    E1.place(x=100,y=200)

                    EtiquetaCodigo=Label(ventana6,text="Codigo")
                    EtiquetaCodigo.place(x=200,y=310)

                    codigo=Listbox(ventana6,width=75,height=6)
                    codigo.place(x=200,y=330)

                    EtiquetaVariable=Label(ventana6,text="Variables")
                    EtiquetaVariable.place(x=480,y=130)

                    variables=Listbox(ventana6,width=25,height=10)
                    variables.place(x=480,y=150)

                    EtiquetaResultado=Label(ventana6,text="Resulado")
                    EtiquetaResultado.place(x=260,y=130)

                    resultado=Listbox(ventana6,width=25,height=10)
                    resultado.place(x=260,y=150)

                    #cargando el archivo en una lista...
                    def cargaLista(LInstruccion,nomcodigo):
                        f=open(str(nomcodigo)+".py", mode="r")
                        contador = 0
                        linea = f.readline()
                        while linea != "":
                            codigo.insert(contador, linea)
                            LInstruccion.append(linea)
                            linea = f.readline()
                            contador = contador+1
                        f.close()
                        return LInstruccion  

                    nomcodigo="curiosidades del 153"
                    codigoamigos=[]
                    codigoamigos=cargaLista(codigoamigos,nomcodigo)

                    #toma el valor de variableF y lo asigna
                    #entradas= ninguna
                    #salidas= CuriosidadesDel153(num)
                    def Curiosidades():
                        variables.insert(END,"def Curiosidades():")
                        num=variableF.get()
                        return CuriosidadesDel153(num)

                    #regresa la funcion que el usuario digite
                    #entradas= num(numero)
                    #salidas=la funcion que le usuario desee o un mensaje si no se digita nada dentro del rango
                    def CuriosidadesDel153(num):
                        variables.insert(END,"def CuriosidadesDel153("+str(num)+"):")
                        variables.insert(END,"num= "+str(num))
                        if num==1:
                            return digitos()
                        elif num==2:
                            return cuadradoPerfecto()
                        elif num==3:
                            return Sum17()
                        elif num==4:
                            return TrianguloInvertible()
                        else:
                            return "ingrese curiosidad"

                    #inicializa hilera y llama a digitos_Aux(153, hilera)
                    #entradas: ninguna
                    #salidas= digitos_Aux(153, hilera)
                    def digitos():
                        global lineas5
                        lineas5=lineas5+[0,1,2]
                        variables.insert(END,"def digitos():")
                        hilera=""
                        return digitos_Aux(153, hilera)

                    #devuelve un string con la suma de los cuadrados de los digitos del 153
                    #entradas= num(numero)
                    #          hilera(string vacio)
                    #salidas= string con la suma de los cuadrados de los digitos del 153
                    def digitos_Aux(num,hilera):
                        global lineas5
                        lineas5=lineas5+[4,5]
                        variables.insert(END,"def digitos_Aux("+str(num)+","+str(hilera)+")")
                        variables.insert(END,"num= "+str(num))
                        variables.insert(END,"hilera= "+str(hilera))                 
                        if num<10:
                            lineas5=lineas5+[6,7]
                            hilera=str(num)+"^3 "+hilera
                            w.start()
                            return resultado.insert(END,"153= "+ hilera)
                        else:
                            lineas5=lineas5+[8,9,10]
                            hilera=str(num%10)+"^3 "+hilera
                            return digitos_Aux(num//10, hilera)
                        
                    #llama a CP(153,"",0)
                    def cuadradoPerfecto():
                        global lineas5
                        lineas5=lineas5+[12,13]
                        variables.insert(END,"def cuadradoPerfecto():")
                        return CP(153,"",0)

                    #muestra que la suma de los cuadrados de los digitos del 153 son un cuadrado perfecto
                    #entradas= num(numero)
                    #          hilera(string vacio) 
                    #          res(numero 0)
                    #salidas= un string
                    def CP(num,hilera,res):
                        global lineas5
                        lineas5=lineas5+[15,16]
                        variables.insert(END,"def CP("+str(num)+","+str(hilera)+","+str(res)+")")
                        variables.insert(END,"num= "+str(num))
                        variables.insert(END,"hilera= "+str(hilera))
                        variables.insert(END,"res= "+str(res)) 
                        if num<10:
                            lineas5=lineas5+[17,18,19]
                            res=res+num
                            hilera=str(num)+hilera+"="+str(res)+"=3^2"
                            w.start()
                            return resultado.insert(END,"153= "+ hilera)
                        else:
                            lineas5=lineas5+[20,21,22,23]
                            hilera=" + "+str(num%10)+hilera
                            res=res+num%10
                            return CP(num//10, hilera,res)

                    #llama a Sum17_aux("",1,0)
                    def Sum17():
                        global lineas5
                        lineas5=lineas5+[25,26]
                        variables.insert(END,"def Sum17():")
                        return Sum17_aux("",1,0)

                    #muestra que la suma de todos los numeros del 1 al 17 es igual a 153
                    #entradas= hilera(string vacio)
                    #          cont(contador en 1)
                    #          res(0)
                    #salidas= string con todos los numeros del 1 al 17 sumandose
                    def Sum17_aux(hilera,cont,res):
                        global lineas5
                        lineas5=lineas5+[28,29]
                        variables.insert(END,"def Sum17_aux("+str(hilera)+","+str(cont)+","+str(res)+")")
                        variables.insert(END,"hilera= "+str(hilera))
                        variables.insert(END,"cont= "+str(cont))
                        variables.insert(END,"res= "+str(res)) 
                        if cont==17:
                            lineas5=lineas5+[30,31,32]
                            res=res+cont
                            hilera=hilera+str(cont)+"="+str(res)
                            w.start()
                            return resultado.insert(END,hilera)
                        else:
                            lineas5=lineas5+[33,34,35,36]
                            hilera=hilera+str(cont)+"+"
                            res=res+cont
                            return Sum17_aux(hilera,cont+1,res)



                    def TrianguloInvertible():
                        global lineas5
                        lineas=lineas5+[38,39,40]
                        variables.insert(END,"def TrianguloInvertible():")

                        resultado.insert(END,TrianguloInvertible_aux(153,1,0,""))
                        return resultado.insert(END,TrianguloInvertible_aux(351,1,0,""))

                    #muestra que el 153 es un triangulo invertible
                    #entradas= num(numero)
                    #          cont(contador en 1)
                    #          res(0)
                    #          hilera(string vacio)
                    #salidas= string con la suma del 1 hasta el 17 y del 1 hasta el 26 
                    def TrianguloInvertible_aux(num,cont,res,hilera):
                        global lineas5
                        lineas5=lineas5+[42,43]
                        variables.insert(END,"def TrianguloInvertible_aux("+str(num)+","+str(cont)+","+str(res)+","+str(hilera)+"):")
                        variables.insert(END,"num= "+str(num))
                        variables.insert(END,"cont= "+str(cont))
                        variables.insert(END,"res= "+str(res))
                        variables.insert(END,"hilera= "+str(hilera))
                        if res==num:
                            lineas5=lineas5+[44]
                            w.start()
                            return str(num)+"= "+hilera[1:]
                        else:
                            lineas5=lineas5+[45,46,47,48]
                            hilera=hilera+" + "+str(cont)
                            res=res+cont
                            return TrianguloInvertible_aux(num,cont+1,res,hilera)

                    #inserta el codigo en un listbox y lo va señalando segun se ejecuta
                    #entradas: lista con el codigo
                    #salidas: la linea que se ejecuta, subrayada
                    def cargaMueve(lineas5):
                        for linact in lineas5:
                            codigo.see(linact)
                            hilo = (threading.currentThread(), lineas[linact])
                            time.sleep (1)
                            codigo.selection_set(linact)
                            time.sleep (0.5)
                            codigo.selection_clear(linact)

                    #hilo
                    w=threading.Thread(target=lambda:cargaMueve(lineas), name="cc")

                    #elimina la ventana actual y regresa a la anterior
                    def ventanaAnterior():
                        ventana6.destroy() 
                        ventana5.deiconify()

                    VenAnt=Button(ventana6,text="Anterior",width=10,command=ventanaAnterior)
                    VenAnt.place(x=10,y=400)

                    ejecutar=Button(ventana6,text="ejecutar",width=20,command=Curiosidades)
                    ejecutar.place(x=50,y=260)

#botones para seguir de pantalla
                siguiente=Button(ventana5,text="siguiente",width=10,command=Curiosidades153)
                siguiente.place(x=100,y=400)
 

            siguiente=Button(ventana4,text="siguiente",width=10,command=NumeroTriangular)
            siguiente.place(x=100,y=400)


        siguiente=Button(ventana3,text="siguiente",width=10,command=TrianguloP)
        siguiente.place(x=100,y=400)

    siguiente=Button(ventana2,text="siguiente",width=10,command=NumsAmigos)
    siguiente.place(x=100,y=400)




#imagen de fondo
imgFondo= PhotoImage (file="mat4.gif")

fondo1=Label(image=imgFondo)
fondo1.pack(side='top', fill='both', expand='yes')

imgBoton=PhotoImage(file="flecha.gif")
boton1=Button(fondo1,image=imgBoton,bd=0,command=ConjeturaDeGoldbach)
boton1.place(x=575,y=350)

ventana.mainloop()
