from django.forms import ModelForm

from .models import todolist


class AddList(ModelForm):
    class Meta:
        model = todolist
        exclude = ('is_finished',)
        fields = '__all__'