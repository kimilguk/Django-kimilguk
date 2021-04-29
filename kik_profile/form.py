from django.forms import ModelForm
from .models import Award

class AwardForm(ModelForm):
    class Meta:
        model = Award
        fields = ['title','award_date','pub_date']