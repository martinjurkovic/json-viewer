from django.shortcuts import render
import json
from .forms import FileUploadForm

def load_data(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            data = json.load(request.FILES['file'])

            single_col_metrics = data['metrics']["single_column"]
            for table in single_col_metrics:
                for metric in single_col_metrics[table]:
                    for column in single_col_metrics[table][metric]:
                        single_col_metrics[table][metric][column]["combined_scores"] = zip(single_col_metrics[table][metric][column]["scores"],single_col_metrics[table][metric][column]["aggregation_bootstrap_scores"]["95ci"])

            return render(request, 'viewer/index.html', {'data': data})
    else:
        form = FileUploadForm()

    return render(request, 'viewer/upload.html', {'form': form})

if __name__ == '__main__':
    import os
    print("Current working directory:", os.getcwd())
    data = json.load(open('mutagenesis_mostlyai.json'))
    single_col_metrics = data['metrics']["single_column"]
    for table in single_col_metrics:
        for metric in single_col_metrics[table]:
            for column in single_col_metrics[table][metric]:
                 single_col_metrics[table][metric][column]["combined_scores"] = zip(single_col_metrics[table][metric][column]["scores"],single_col_metrics[table][metric][column]["aggregation_bootstrap_scores"]["95ci"])

