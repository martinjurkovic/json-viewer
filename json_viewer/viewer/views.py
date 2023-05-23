from django.shortcuts import render
import json
from .forms import FileUploadForm
# Create your views here.

def load_data(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            data = json.load(request.FILES['file'])

            return render(request, 'viewer/index.html', {'data': data})
    else:
        form = FileUploadForm()

    return render(request, 'viewer/upload.html', {'form': form})
