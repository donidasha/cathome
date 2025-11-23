from django import forms
from .models import Volunteer, Application, Cat

class ApplicationForm(forms.ModelForm):
    name = forms.CharField(max_length=150)
    phone_number = forms.CharField(max_length=150)
    email = forms.EmailField()
    
    class Meta:
        model = Volunteer
        fields = ("name","phone_number", "email")
        
    def save(self, commit=True):
        volunteer = super().save(commit=False)
        
        if commit:
            volunteer.save()
        return volunteer
    
class CatForm(forms.ModelForm):
    
    class Meta:
        model = Application
        fields = ("name", "email", "phone_number", "comment", "cat")
        
        def save(self, commit=True):
            application = super().save(commit=False)
        
            if commit:
                application.save()
            return application
    