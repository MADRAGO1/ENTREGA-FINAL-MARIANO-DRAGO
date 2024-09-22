from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from EncMus.models import Musicos, Bandas, Barandpubs, Salasensayo, Productores
from .forms import Musicosformulario, Bandasformulario, Barsandpubsformulario, Salasensayoformulario, Productoresformulario


# Create your views here.

def crea_musicos(req, nombre, apellido, instrumento, email, tel, edad, dni):
  
  nnuevo_musico = Musicos (nombre=nombre, apellido=apellido, instrumento=instrumento, email=email, tel=tel, edad=edad, dni=dni)
  nuevo_musico.save()  

  return HttpResponse(f"""
    <p>Nombre: {nuevo_musico.nombre} - Apellido: {nuevo_musico.apellido} - Instrumento: {nuevo_musico.instrumento} - email: {nuevo_musico.email} - tel: {nuevo_musico.tel} - edad: {nuevo_musico.edad} - dni: {nuevo_musico.dni}
 """)




# Creo vistas

def inicio(req):
  
  return render(req, "inicio.html", {})


def musicos(req):
  
  return render(req, "musicos.html", {})


def bandas(req):
  
  return render(req, "bandas.html", {})


def barandpubs(req):
  
  return render(req, "barandpubs.html", {})


def salasensayo(req):
  
  return render(req, "salasensayo.html", {})


def productores(req):
  
  return render(req, "productores.html", {})



#formularios Clase 21

def musicosFormulario(request):
 
    print('method', request.method)
    print('data', request.POST)

    if request.method =='POST':
      nuevo_musico = Musicos(nombre=request.POST["nombre"], apellido=request.POST["apellido"], instrumento=request.POST["instrumento"], email=request.POST["email"], tel=request.POST["tel"], edad=request.POST["edad"], dni=request.POST["dni"])
      nuevo_musico.save()

      return render(request,"inicio.html")
    
    else:
      mi_formulario= Musicosformulario()  
      return render(request,"musicosFormulario.html", { "mi_formulario": mi_formulario})







def bandasFormulario(request):
 
    print('method', request.method)
    print('data', request.POST)

    if request.method =='POST':
      nuevo_banda = Bandas(nombre_b=request.POST["nombre banda"], contacto=request.POST["contacto banda"], email_b=request.POST["email banda"])
      nuevo_banda.save()

      return render(request,"inicio.html")
    
    else:
      mi_formulario= Bandasformulario()  
      return render(request,"bandasformulario.html", { "mi_formulario": mi_formulario})
        




def barsandpubsFormulario(request):
 
    print('method', request.method)
    print('data', request.POST)
    if request.method =='POST':
       nuevo_barandpubs = Barandpubs(nombre_bar=request.POST["nombre"], contacto_bar=request.POST["contacto"], email_bar=request.POST["email"], tel_bar=request.POST["tel"], estilo_bar=request.POST["estilo"], dir_bar=request.POST["dir"], sonidopropio=request.POST["sonidopropio"])
       nuevo_barandpubs.save()
       return render(request,"inicio.html")
    else:
        mi_formulario= Barsandpubsformulario()  
        return render(request,"barsandpubsFormulario.html", { "mi_formulario": mi_formulario})








def salasensayoFormulario(request):

    print('method', request.method)
    print('data', request.POST)
    if request.method =='POST':
       nuevo_salasensayo = Salasensayo(nombre_sala=request.POST["nombre"], contacto_sala=request.POST["contacto"], email_sala=request.POST["email"], tel_sala=request.POST["tel"], estilo_sala=request.POST["estilo"], dir_sala=request.POST["dir"], cantsalas=request.POST["cantsalas"])
       nuevo_salasensayo.save()
       return render(request,"inicio.html")
    else:
        mi_formulario= Salasensayoformulario()  
        return render(request,"salasensayoFormulario.html", { "mi_formulario": mi_formulario})






def productoresFormulario(request):
    
    print('method', request.method)
    print('data', request.POST)
    if request.method =='POST':
       nuevo_prodcutores = Productores(nombre_prod=request.POST["nombre"], apellido_prod=request.POST["apellido"], email_prod=request.POST["email"], tel_prod=request.POST["tel"])
       nuevo_prodcutores.save()
       return render(request,"inicio.html")
    else:
        mi_formulario= Productoresformulario()  
        return render(request,"productoresformulario.html", { "mi_formulario": mi_formulario})


#BUSQUEDAS
#Musicos
def busquedaMusicos(request):
   
   return render (request, "busqueda_musicos.html")

def buscarMusicos(request):

  n_nombre= request.GET["nombre"]
  musicos= Musicos.objects.filter(nombre__icontains=n_nombre)
  return render(request,"resultado_busqueda.html", { "Musicos": musicos, "nombre":n_nombre})

#Bandas
def busquedaBandas(request):
   
   return render (request, "busqueda_bandas.html")

def buscarBandas(request):

  n_nombre= request.GET["nombre_b"]
  bandas= Bandas.objects.filter(nombre_b__icontains=n_nombre)
  return render(request,"resultado_busquedaBandas.html", { "Bandas": bandas, "nombre":n_nombre})

#Bars and Pubs
def busquedaBars(request):
   
   return render (request, "busqueda_bars.html")

def buscarBars(request):

  n_nombre= request.GET["nombre_bar"]
  bars= Barandpubs.objects.filter(nombre_bar__icontains=n_nombre)
  return render(request,"resultado_busquedaBars.html", { "Barandpubs": bars, "nombre":n_nombre})

#Salas
def busquedaSalas(request):
   
   return render (request, "busqueda_sala.html")

def buscarSalas(request):

  n_nombre= request.GET["nombre_sala"]
  sala= Salasensayo.objects.filter(nombre_sala__icontains=n_nombre)
  return render(request,"resultado_busquedaSala.html", { "Salasensayo": sala, "nombre":n_nombre})

#Productores
def busquedaProductores(request):
   
   return render (request, "busqueda_productores.html")

def buscarProductores(request):

  n_nombre= request.GET["nombre_prod"]
  productor= Productores.objects.filter(nombre_prod__icontains=n_nombre)
  return render(request,"resultado_busquedaProductores.html", { "Productores": productor, "nombre":n_nombre})


#CRUD 

def lista_musicos(req):
  
  lista = Musicos.objects.all()
  return render(req, 'lista_musicos.html', {"lista_musicos": lista})


def crea_musico(request):
 
    print('method', request.method)
    print('data', request.POST)

    if request.method =='POST':

      mi_formulario= Musicosformulario(request.POST) 
      if mi_formulario.is_valid():
         data = mi_formulario.cleaned_data

         nuevo_musico = Musicos(nombre=data["nombre"], apellido=data["apellido"], instrumento=data["instrumento"], email=data["email"], tel=data["tel"], edad=data["edad"], dni=data["dni"])
         nuevo_musico.save()

         return HttpResponseRedirect("/EncMus")
    
      else:
        return render(request,"musicosFormulario.html", { "mi_formulario": mi_formulario})

    else:
      mi_formulario= Musicosformulario()  
      return render(request,"musicosFormulario.html", { "mi_formulario": mi_formulario})
    
#Bandas

def lista_bandas(req):
  
  lista = Bandas.objects.all()
  return render(req, 'lista_bandas.html', {"lista_bandas": lista})


def crea_banda(request):
 
    print('method', request.method)
    print('data', request.POST)

    if request.method =='POST':

      mi_formulario= Bandasformulario(request.POST) 
      if mi_formulario.is_valid():
         data = mi_formulario.cleaned_data

         nuevo_banda = Bandas(nombre_b=data["nombre_b"], Contacto=data["Contacto"], email_b=data["email_b"])
         nuevo_banda.save()

         return HttpResponseRedirect("/EncMus")
    
      else:
        return render(request,"bandasformulario.html", { "mi_formulario": mi_formulario})

    else:
      mi_formulario= Bandasformulario()  
      return render(request,"bandasformulario.html", { "mi_formulario": mi_formulario})
    



def lista_bars(req):
  
  lista = Barandpubs.objects.all()
  return render(req, 'lista_bars.html', {"lista_bars": lista})


def crea_bars(request):
 
    print('method', request.method)
    print('data', request.POST)

    if request.method =='POST':

      mi_formulario= Barsandpubsformulario(request.POST) 
      if mi_formulario.is_valid():
         data = mi_formulario.cleaned_data

         nuevo_bar = Barandpubs(nombre_bar=data["nombre_bar"], Contacto_bar=data["Contacto_bar"], email_bar=data["email_bar"], tel_bar=data["tel_bar"], Estilo_bar=data["Estilo_bar"], dir_bar=data["dir_bar"], Sonidopropio=data["Sonidopropio"])
         nuevo_bar.save()

         return HttpResponseRedirect("/EncMus")
    
      else:
        return render(request,"barsandpubsformulario.html", { "mi_formulario": mi_formulario})

    else:
      mi_formulario= Barsandpubsformulario()  
      return render(request,"barsandpubsformulario.html", { "mi_formulario": mi_formulario})
    








def lista_salas(req):
  
  lista = Salasensayo.objects.all()
  return render(req, 'lista_salas.html', {"lista_salas": lista})







def crea_salas(request):
 
    print('method', request.method)
    print('data', request.POST)

    if request.method =='POST':

      mi_formulario= Salasensayoformulario(request.POST) 
      if mi_formulario.is_valid():
         data = mi_formulario.cleaned_data

         nuevo_bar = Salasensayo(nombre_sala=data["nombre_sala"], Contacto_sala=data["Contacto_sala"], email_sala=data["email_sala"], tel_sala=data["tel_sala"], Estilo_sala=data["Estilo_sala"], dir_sala=data["dir_sala"], cantsalas=data["cantsalas"])
         nuevo_bar.save()

         return HttpResponseRedirect("/EncMus")
    
      else:
        return render(request,"salasensayoformulario.html", { "mi_formulario": mi_formulario})

    else:
      mi_formulario= Salasensayoformulario()  
      return render(request,"salasensayoformulario.html", { "mi_formulario": mi_formulario})
    



def lista_prod(req):
  
  lista = Productores.objects.all()
  return render(req, 'lista_prod.html', {"lista_prod": lista})




def crea_prod(request):
 
    print('method', request.method)
    print('data', request.POST)

    if request.method =='POST':

      mi_formulario= Productoresformulario(request.POST) 
      if mi_formulario.is_valid():
         data = mi_formulario.cleaned_data

         nuevo_bar = Productores(nombre_prod=data["nombre_prod"], apellido_prod=data["apellido_prod"], email_prod=data["email_prod"], tel_prod=data["tel_prod"])
         nuevo_bar.save()

         return HttpResponseRedirect("/EncMus")
    
      else:
        return render(request,"productoresformulario.html", { "mi_formulario": mi_formulario})

    else:
      mi_formulario= Productoresformulario()  
      return render(request,"productoresformulario.html", { "mi_formulario": mi_formulario})



#DELETE

def eliminar_musico(request, id):
   
  if request.method =='POST':
     musico = Musicos.objects.get(id=id)
     musico.delete()
     return redirect('lista_musicos')
  else:
     lista = Musicos.objects.all()
  return render(request, 'lista_musicos.html', {"lista_musicos": lista})



def eliminar_banda(request, id):
   
  if request.method =='POST':
     banda = Bandas.objects.get(id=id)
     banda.delete()
     return redirect('lista_bandas')
  else:
     lista = Bandas.objects.all()
  return render(request, 'lista_bandas.html', {"lista_bandas": lista})


def eliminar_bars(request, id):
   
  if request.method =='POST':
     bar = Barandpubs.objects.get(id=id)
     bar.delete()
     return redirect('lista_bars')
  else:
     lista = Barandpubs.objects.all()
  return render(request, 'lista_bars.html', {"lista_bars": lista})





def eliminar_salas(request, id):
   
  if request.method =='POST':
     sala = Salasensayo.objects.get(id=id)
     sala.delete()
     return redirect('lista_salas')
  else:
     lista = Salasensayo.objects.all()
  return render(request, 'lista_salas.html', {"lista_salas": lista})


def eliminar_prod(request, id):
   
  if request.method =='POST':
     prod = Productores.objects.get(id=id)
     prod.delete()
     return redirect('lista_prod')
  else:
     lista = Productores.objects.all()
  return render(request, 'lista_prod.html', {"lista_prod": lista})


# EDITAR UPDATE
#MUSICOS
def editar_musicos(request, id):
   
   if request.method =='POST':
    
    mi_formulario= Musicosformulario(request.POST)
    musico = Musicos.objects.get(id=id)

    if mi_formulario.is_valid():
     data = mi_formulario.cleaned_data

     musico.nombre=data["nombre"]
     musico.apellido=data["apellido"]
     musico.instrumento=data["instrumento"]
     musico.email=data["email"]
     musico.tel=data["tel"]
     musico.edad=data["edad"]
     musico.dni=data["dni"]     

     musico.save()

     return HttpResponseRedirect("/EncMus")
    
    else:
     return render(request,"musicosFormulario.html", { "mi_formulario": mi_formulario})

   else:
     
     musico = Musicos.objects.get(id=id)

     mi_formulario= Musicosformulario(initial={
       "nombre": musico.nombre,                               
       "apellido": musico.apellido,
       "instrumento": musico.instrumento,
       "email": musico.email,
       "tel": musico.tel,
       "edad": musico.edad,
       "dni": musico.dni,                              
         })  
     return render(request,"editar_musico.html", { "mi_formulario": mi_formulario, "id": musico.id })



#BANDAS
def editar_bandas(request, id):
   
   if request.method =='POST':
    
    mi_formulario= Bandasformulario(request.POST)
    banda = Bandas.objects.get(id=id)

    if mi_formulario.is_valid():
     data = mi_formulario.cleaned_data

     banda.nombre_ba=data["nombre_b"]
     banda.Contacto=data["Contacto"]
     banda.email_b=data["email_b"]
     
     banda.save()

     return HttpResponseRedirect("/EncMus")
    
    else:
     return render(request,"bandasformulario.html", { "mi_formulario": mi_formulario})

   else:
     
     banda = Bandas.objects.get(id=id)

     mi_formulario= Bandasformulario(initial={
       "nombre_b": banda.nombre_ba,                               
       "Contacto": banda.Contacto,
       "email_b": banda.email_b,
          })  
     return render(request,"editar_banda.html", { "mi_formulario": mi_formulario, "id": banda.id })
   


   #BARS
def editar_bars(request, id):
   
   if request.method =='POST':
    
    mi_formulario= Barsandpubsformulario(request.POST)
    bar = Barandpubs.objects.get(id=id)

    if mi_formulario.is_valid():
     data = mi_formulario.cleaned_data

     bar.nombre_bar=data["nombre_bar"]
     bar.Contacto_bar=data["Contacto_bar"]
     bar.email_bar=data["email_bar"]
     bar.tel_bar=data["tel_bar"]
     bar.Estilo_bar=data["Estilo_bar"]
     bar.dir_bar=data["dir_bar"]
     bar.Sonidopropio=data["Sonidopropio"]

     
     bar.save()

     return HttpResponseRedirect("/EncMus")
    
    else:
     return render(request,"barsandpubsformulario.html", { "mi_formulario": mi_formulario})

   else:
     
     bar = Barandpubs.objects.get(id=id)

     mi_formulario= Barsandpubsformulario(initial={
       "nombre_bar": bar.nombre_bar,                               
       "Contacto_bar": bar.Contacto_bar,
       "email_bar": bar.email_bar,
       "tel_bar": bar.tel_bar,
       "Estilo_bar": bar.Estilo_bar,
       "dir_bar": bar.dir_bar,
       "Sonidopropio": bar.Sonidopropio,


          })  
     return render(request,"editar_bar.html", { "mi_formulario": mi_formulario, "id": bar.id })
   


#Salas
def editar_salas(request, id):
   
   if request.method =='POST':
    
    mi_formulario= Salasensayoformulario(request.POST)
    sala = Salasensayo.objects.get(id=id)

    if mi_formulario.is_valid():
     data = mi_formulario.cleaned_data

     sala.nombre_sala=data["nombre_sala"]
     sala.Contacto_sala=data["Contacto_sala"]
     sala.email_sala=data["email_sala"]
     sala.tel_sala=data["tel_sala"]
     sala.Estilo_sala=data["Estilo_sala"]
     sala.dir_sala=data["dir_sala"]
     sala.cantsalas=data["cantsalas"]


     
     sala.save()

     return HttpResponseRedirect("/EncMus")
    
    else:
     return render(request,"salasensayoformulario.html", { "mi_formulario": mi_formulario})

   else:
     
     sala = Salasensayo.objects.get(id=id)

     mi_formulario= Salasensayoformulario(initial={
       "nombre_sala": sala.nombre_sala,                               
       "Contacto_sala": sala.Contacto_sala,
       "email_sala": sala.email_sala,
       "tel_sala": sala.tel_sala,
       "Estilo_sala": sala.Estilo_sala,
       "dir_sala": sala.dir_sala,
       "cantsalas": sala.cantsalas,


          })  
     return render(request,"editar_sala.html", { "mi_formulario": mi_formulario, "id": sala.id })





#Productores
def editar_prod(request, id):
   
   if request.method =='POST':
    
    mi_formulario= Productoresformulario(request.POST)
    prod = Productores.objects.get(id=id)

    if mi_formulario.is_valid():
     data = mi_formulario.cleaned_data

     prod.nombre_prod=data["nombre_prod"]
     prod.apellido_prod=data["apellido_prod"]
     prod.email_prod=data["email_prod"]
     prod.tel_prod=data["tel_prod"]
    
         
     prod.save()

     return HttpResponseRedirect("/EncMus")
    
    else:
     return render(request,"productoresformulario.html", { "mi_formulario": mi_formulario})

   else:
     
     prod = Productores.objects.get(id=id)

     mi_formulario= Productoresformulario(initial={
       "nombre_prod": prod.nombre_prod,                               
       "apellido_prod": prod.apellido_prod,
       "email_prod": prod.email_prod,
       "tel_prod": prod.tel_prod,
      
    
          })  
     return render(request,"editar_prod.html", { "mi_formulario": mi_formulario, "id": prod.id })