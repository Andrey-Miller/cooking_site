from django import forms

from .models import Recipe, Category


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'cooking', 'cooking_time', 'image', 'products', 'author']
        widgets = {
            'cooking': forms.Textarea(attrs={'rows': 6}),
        }

    category = forms.ModelChoiceField(queryset=Category.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Нет категории"
