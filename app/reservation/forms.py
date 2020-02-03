from django.forms import ModelForm, ModelChoiceField, Textarea, CharField

from users.models import User
from .models import Reservation

class CreateReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ('title', 'room', 'approver', 'reserved_start_date', 'reserved_end_date', 'participants_gmail')

    participants_gmail = CharField(widget=Textarea, required=False, help_text='in each line, one gmail address')
    approver = ModelChoiceField(queryset=User.objects.filter(is_professor=True), required=False)
