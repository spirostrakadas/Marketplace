from django import forms
from .models import Item

INPUT_CLASSES='w-full y-4 px-6rounded-xl border'

class Additem(forms.ModelForm):
    class Meta:
        model=Item
        fields=('category','name','description','price','image')

        widgets= {
            'category':forms.Select(attrs={
            'class':INPUT_CLASSES}),

            'name':forms.TextInput(attrs={
            'class':INPUT_CLASSES}),

            'desctription':forms.Textarea(attrs={
            'class':INPUT_CLASSES}),

            'price':forms.TextInput(attrs={
            'class':INPUT_CLASSES}),

            'image':forms.FileInput(attrs={
            'class':INPUT_CLASSES})

                            }