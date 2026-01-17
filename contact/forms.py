from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['nom_complet', 'telephone', 'message']
        widgets = {
            'nom_complet': forms.TextInput(attrs={'placeholder': 'أدخل اسمك الكامل'}),
            'telephone': forms.TextInput(attrs={'placeholder': 'أدخل رقم الهاتف'}),
            'message': forms.Textarea(attrs={
                'placeholder': 'اكتب رسالتك هنا',
                'rows': 4
            }),
        }
