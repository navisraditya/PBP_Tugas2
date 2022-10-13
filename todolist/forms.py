from django.forms import ModelForm

from .models import todolist


class AddList(ModelForm):
    class Meta:
        model = todolist
        exclude = ('user', 'is_finished')
        fields = '__all__'