from django.shortcuts import render

def index(request):
    context={}
    return render(request, 'pages/index.html', context)

def login(request):
    context={}
    return render(request, 'pages/login.html', context)

def form1(request):
    context={}
    return render(request, 'pages/form1.html', context)

def plants(request):
    context={}
    return render(request, 'pages/plants.html', context)

def listProducto(request):
    context={}
    return render(request, 'pages/listProducto.html', context)

def crud(request):
    productos = Producto.objects.all()
    context = {'productos':productos}
    return render(request, 'pages/listProducto.html', context)

def addProducto(request):
    if request.method is not "POST":
        return render(request, 'pages/addProducto.html', context)
    else:
        idProducto = request.POST["id"]
        nombreProducto = request.POST["nombre"]
        cantidad = request.POST["cantidad"]
        precio = request.POST["precio"]
        estadoProducto = request.POST["estado"]

        obj = Producto.objects.create(
            idProducto = idProducto,
            nombreProducto = nombreProducto,
            cantidad = cantidad,
            precio = precio,
            estadoProducto = estado
        )
        obj.save()
        context = {'mensaje':"Producto añadido"}
        return render (request, 'pages/addProducto.html', context)

def delProducto(request,pk):
    context = {}
    try:
        producto = Producto.objects.get(idProducto=pk)
        producto.delete()
        mensaje = "Producto eliminado"
        productos = Producto.objects.all()
        context = {'productos':productos,'mensaje':mensaje}
        return render(request, 'pages/listProducto.html', context)
    except:
        mensaje = "Producto no encontrado"
        productos = Producto.objects.all()
        context = {'productos':productos, 'mensaje':mensaje}
        return render(request, 'pages/listProducto.html', context)

def retModProducto(request,pk):
    if pk != "":
        producto = Producto.objects.get(idProducto=pk)
        context = {'producto':producto}
        if producto:
            return render(request, 'pages/editProducto.html', context)
        else:
            context = {'mensaje':"producto inexistente o id inválida"}
            return render(request, 'pages/listProducto.html', context)

def updProducto (request):
    if request.method == "POST":
        idProducto = request.POST["id"]
        nombreProducto = request.POST["nombre"]
        cantidad = request.POST["cantidad"]
        precio = request.POST["precio"]
        estadoProducto = request.POST["estado"]

        producto = Producto()
        producto.idProducto = id
        producto.nombreProducto = nombre
        producto.cantidad = cantidad
        producto.precio = precio
        producto.estadoProducto = estado
        producto.save()

        context = {'mensaje':"Datos del producto actualizados",'producto':producto}
        return render(request, 'pages/editProducto.html', context)
    else:
        productos = Producto.objects.all()
        context = {'producto':producto}
        return render(request,'pages/listProducto.html', context)