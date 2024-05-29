from django import forms
from .models import Francesinha, Ingredients


class FrancesinhaForm(forms.ModelForm):
    
    ingredients = forms.ModelMultipleChoiceField(
        queryset = Ingredients.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label = "Ingredients"
    )
    
    
    class Meta:
        model = Francesinha
        fields = [
            'name',
            'price',
            'rating',
            'ingredients',
        ]
        
        
    def clean_rating(self, *args, **kwargs):
        rating = self.cleaned_data.get("rating")
        if rating > 5:
            raise forms.ValidationError("Rating must be between 0 and 5")
        elif rating < 0:
            raise forms.ValidationError("Rating must be between 0 and 5")
        return rating
    
    
    def clean_price(self, *args, **kwargs):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise forms.ValidationError("Price must be greater than 0")
        return price