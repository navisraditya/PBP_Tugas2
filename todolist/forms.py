from django.forms import ModelForm

from .models import todolist


class AddList(ModelForm):
    class Meta:
        model = todolist
        fields = '__all__'
    