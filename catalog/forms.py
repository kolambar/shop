from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('creation_date', 'last_change_date', )

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        forbidden_words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар',)
        for word in forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Тут такое продавать нельзя!')
            return cleaned_data
