from django.shortcuts import render
from .forms import FormEntryForm, WorkshopPass

def form_view(request):
    if request.method == 'POST':
        form = FormEntryForm(request.POST)
        if form.is_valid():
            form_instance = form.save(commit=False)

            selected_preferences = form.cleaned_data['preferences']

            form_instance.save()

            for preference in selected_preferences:
                workshop_pass, _ = WorkshopPass.objects.get_or_create(preference=preference)
                if workshop_pass.allocated_passes < workshop_pass.total_passes:
                    workshop_pass.allocated_passes += 1
                    workshop_pass.total_passes -= 1
                    workshop_pass.form_entry = form_instance 
                    workshop_pass.save()
                    print(preference)  
                    print("Success: Workshop allocated!")
                    break

        else:
            print("Error")

    else:
        form = FormEntryForm()

    return render(request, 'forms.html', {'form': form})
