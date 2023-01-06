from django import forms
from shop.models import Product, Category


class ProductForm(forms.ModelForm):
    rating = forms.IntegerField(required=True, initial=3)

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.friendly_name) for c in categories if c.friendly_name]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
            field.widget.attrs['placeholder'] = field.label
            if field_name != 'category' and field_name != 'availability':
                field.label = False
