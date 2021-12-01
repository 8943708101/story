from django.shortcuts import render, redirect
from . models import Mystory
from . forms import Storiesforms

# Create your views here.
def story_view(request):
    obj1=Mystory.objects.all()
    if request.method == 'POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        date=request.POST.get('date')
        obj=Mystory(name=name,desc=desc,date=date)
        obj.save()
    return render(request,'story_view.html',{'obj1':obj1})

def delete(request,storyid):
    mysto = Mystory.objects.get(id=storyid)
    if request.method == 'POST':
        mysto.delete()
        return redirect('/')
    return render(request,'delete.html',{'mysto':mysto})

def update(request,id):
    mysto = Mystory.objects.get(id=id)
    form = Storiesforms(request.POST or None, instance=mysto)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'mysto': mysto,'form':form})