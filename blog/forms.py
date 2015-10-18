#-*- coding: utf-8 -*-

from django import forms

class contactForm(forms.Form):
    sujet = forms.CharField(max_length = 100)
    message = forms.CharField(widget = forms.Textarea)
    envoyeur = forms.EmailField(label= "Votre adresse Email")
    renvoi = forms.BooleanField(help_text = "Cochez si vous souhaitez manger des haricots", required = False)
    
    def clean_message(self):
        message = self.cleaned_data['message']
        if "pizza" in message:
            raise forms.ValidationError('On ne veut pas entendre parler de pizza')
            
        return message