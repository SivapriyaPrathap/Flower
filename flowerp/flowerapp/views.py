from django.shortcuts import render, redirect
from . models import Flower
from .forms import Form

# Create your views here.
def index(request):
    flower=Flower.objects.all()

    return render(request,"index.html",{'flower':flower})
def detail(request,id):
    flower=Flower.objects.get(id=id)

    return render(request,"detail.html",{'flower' : flower})
def add(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        places=request.POST.get('places')
        des=request.POST.get('des')
        img=request.FILES['img']
        flower=Flower(name=name,places=places,des=des,img=img)
        flower.save()
    return render(request,"add.html")

def update(request,id):
    flower=Flower.objects.get(id=id)
    form=Form(request.POST or None,request.FILES,instance=flower)
    if form.is_valid():
        form.save()
        return redirect("/index")

    return render(request,"update.html",{'flower':flower ,'form': form})
def delete(request,id):
    if request.method == 'POST':
        flower=Flower.objects.get(id=id)
        flower.delete()
        return redirect("/index")
    return render(request,"delete.html")