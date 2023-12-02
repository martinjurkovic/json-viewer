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
                        if 'detection' in metric:
                            continue
                        try:    
                            ci95_tuples = [tuple(sub_array) for sub_array in single_col_metrics[table][metric][column]["reference_fold_statistics"]["95ci"]]
                            ci95_tuples = single_col_metrics[table][metric][column]["reference_fold_statistics"]["95ci"]
                            single_col_metrics[table][metric][column]["combined_statistics"] = zip(single_col_metrics[table][metric][column]["fold_statistics"]["mean"],
                                                                                                    ci95_tuples)
                        except:
                            single_col_metrics[table][metric][column]["combined_statistics"] = zip(single_col_metrics[table][metric][column]["fold_statistics"]["mean"],
                                                                                                []*len(single_col_metrics[table][metric][column]["fold_statistics"]["mean"]))

            return render(request, 'viewer/index.html', {'data': data})
    else:
        form = FileUploadForm()

    return render(request, 'viewer/upload.html', {'form': form})

if __name__ == '__main__':
    import os
    print("Current working directory:", os.getcwd())
    data = json.load(open('biodegradability_SDV.json'))
    single_col_metrics = data['metrics']["single_column"]
    for table in single_col_metrics:
        for metric in single_col_metrics[table]:
            for column in single_col_metrics[table][metric]:
                 single_col_metrics[table][metric][column]["combined_statistics"] = zip(single_col_metrics[table][metric][column]["fold_statistics"]["mean"],
                                                                                                    single_col_metrics[table][metric][column]["reference_fold_statistics"]["95ci"])

