from django.shortcuts import redirect, render
from .models import Add
from django.contrib import messages

def home(request):
    cadastros = Add.objects.all()
    return render(request, 'home.html', {'cadastros':cadastros})

#Add Method
def add(request):
    if request.method=='POST':
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        fone = request.POST['fone']
        cursoadd = request.POST['cursoadd']
        Add.objects.create(nome=nome, cpf=cpf, fone=fone, cursoadd=cursoadd)
        messages.success(request, 'Cadastro efetivado com sucesso')

    return render(request, 'add.html')

#Update Method1
def update(request, id):
    if request.method=='POST':
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        fone = request.POST['fone']
        cursoadd = request.POST['cursoadd']
        Add.objects.filter(id=id).update(nome=nome, cpf=cpf, fone=fone, cursoadd=cursoadd)
        messages.success(request, 'Cadastro atualizado com sucesso')
    updates = Add.objects.get(id=id)
    return render(request, 'update.html', {'updates':updates})

#Delete Method

def deletar(request, id):
    Add.objects.filter(id=id).delete()
    return redirect ('/')
