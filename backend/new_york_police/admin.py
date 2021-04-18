from django.contrib import admin

from .models import (
    Gender,
    Ethnicity,
    Fado,
    Allegation,
    Precinct,
    ContactReason,
    OutcomeDescription,
    BoardDisposition,
    PoliceComplaint
)

# Register your models here.
admin.site.register(Gender)
admin.site.register(Ethnicity)
admin.site.register(Fado)
admin.site.register(Allegation)
admin.site.register(Precinct)
admin.site.register(ContactReason)
admin.site.register(OutcomeDescription)
admin.site.register(BoardDisposition)
admin.site.register(PoliceComplaint)