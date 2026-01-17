from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم إرسال رسالتك بنجاح!')
            return redirect('contact:contact_page')
        else:
            messages.error(request, 'حدث خطأ، يرجى التأكد من تعبئة الحقول.')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
