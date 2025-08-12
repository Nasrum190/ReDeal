from django import forms
from .models import Item

# This form is used to create a new item
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category','name', 'description','price','image')
        widgets = {
            'category': forms.Select(attrs={'class': 'w-1/5 py-4 px-6 bg-gray-100 rounded-xl border form-select'}),
            'name': forms.TextInput(attrs={'class': 'w-1/2 py-2 px-3 bg-gray-100 rounded-xl border form-input'}),
            'description': forms.Textarea(attrs={'class': 'w-full py-3 px-4 bg-gray-100  rounded-xl border form-textarea'}),
            'price': forms.NumberInput(attrs={'class': 'w-1/5 h-9 py-2 px-3 bg-gray-100  rounded-xl border form-input'}),
            'image': forms.ClearableFileInput(attrs={'class': 'w-2/11  py-4 px-4 h-13  form-input'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select a category"


# This form is used to edit an existing item

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description','price','image','is_sold')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-1/2 py-2 px-3 bg-gray-100 rounded-xl border form-input'}),
            'description': forms.Textarea(attrs={'class': 'w-full py-3 px-4 bg-gray-100 rounded-xl border form-textarea'}),
            'price': forms.NumberInput(attrs={'class': 'w-1/5 h-9 py-2 px-3 bg-gray-100 rounded-xl border form-input'}),
            'image': forms.ClearableFileInput(attrs={'class': 'w-2/11  py-4 px-4 h-13  form-input'}),
        }