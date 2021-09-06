from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def upload_file(request):
    if request.method == 'POST' and request.FILES['myFile']:
        myFile = request.FILES['myFile']
        fs = FileSystemStorage()
        filename = fs.save(myFile.name, myFile)
        upload_file_url = fs.url(filename)
        return render(request, 'index.html',{
            'uploaded_file_url':upload_file_url
        })
    return render(request,'index.html')