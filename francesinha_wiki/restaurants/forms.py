from django import forms
from .models import Francesinha, Restaurant


class RestaurantForm(forms.ModelForm):
    class Meta:
        
        ingredients = forms.ModelMultipleChoiceField(
            queryset = Francesinha.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            required=True,
            label = "Ingredients"
        )
        
        model = Restaurant
        fields = [
            'name',
            'address',
            'city',
            'country',
            'rating',
            'francesinhas',
        ]
        
    def clean_rating(self, *args, **kwargs):
        rating = self.cleaned_data.get("rating")
        if rating > 5:
            raise forms.ValidationError("Rating must be between 0 and 5")
        elif rating < 0:
            raise forms.ValidationError("Rating must be between 0 and 5")
        return rating