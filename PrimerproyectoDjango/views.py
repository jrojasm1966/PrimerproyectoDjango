from django.http import HttpResponse, JsonResponse

from django.shortcuts import HttpResponse, redirect

# Create your views here.
def root(request):
	return redirect("/blogs") 

def index(request):
    return HttpResponse("placeholder para luego mostrar una lista de todos los blogs") 

def new(request):
    return HttpResponse("placeholder para mostrar un nuevo formulario para crear un nuevo blog") 

def create(request):
	return redirect("/") 

def show(request, number):
    
    documento = """
                <HTML>	 	 
                    <BODY>	 
                        <h1> placeholder para mostrar el blog numero: %s </h1>
                    </BODY>	 
                </HTML>	 
                """ %number
                
    return HttpResponse(documento)

def edit(request, number):
    
    documento = """
                <HTML>	 	 
                    <BODY>	 
                        <h1> placeholder para editar el blog: %s </h1>
                    </BODY>	 
                </HTML>	 
                """ %number
                
    return HttpResponse(documento)

def destroy(request, number):
    return redirect("/blogs") 

def respuestaJson(request):
    return JsonResponse({ 'Titulo Pagina JsonResponse' : 'Esta pagina es un BONUS aplicando JsonResponse !!!!' })
