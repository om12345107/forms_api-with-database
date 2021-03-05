from django.shortcuts import render
from app.forms import doc
from app.models import jock
# Create your views here.
def show(request):
    if request.method =='POST':
        mam = doc(request.POST)
        if mam.is_valid():
            nm = mam.cleaned_data['name']
            mb = mam.cleaned_data['mobile']
            ct = mam.cleaned_data['city']
            em = mam.cleaned_data['email']
            ps = mam.cleaned_data['password']
            pk = jock(name=nm,mobile=mb,city=ct,email=em,password=ps)
            pk.save()
    else:
        mam = doc()
    return render(request, 'folder/index.html', {'fil':mam})
    


