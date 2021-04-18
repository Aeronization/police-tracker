from django.db import models

class Gender(models.Model):
    gender = models.CharField(max_length=255)

    def __str__(self):
        return self.gender


class Ethnicity(models.Model):
    ethnicity = models.CharField(max_length=255)

    def __str__(self):
        return self.ethnicity

# FADO = Force, Abuse of Authority, Discourtesy, and Offensive
class Fado(models.Model):
    fado = models.CharField(max_length=255)

    def __str__(self):
        return self.fado


class Allegation(models.Model):

    allegation = models.CharField(max_length=255)

    def __str__(self):
        return self.allegation


class Precinct(models.Model):
    precinct = models.CharField(max_length=255)

    def __str__(self):
        return self.precinct


class ContactReason(models.Model):
    contact_reason = models.CharField(max_length=255)

    def __str__(self):
        return self.contact_reason


class OutcomeDescription(models.Model):
    outcome_description = models.CharField(max_length=255)

    def __str__(self):
        return self.outcome_description


class BoardDisposition(models.Model):
    board_disposition = models.CharField(max_length=255)

    def __str__(self):
        return self.board_disposition


class PoliceComplaint(models.Model):
    unique_mos_id = models.IntegerField()
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    command_now = models.CharField(max_length=255, null=True, blank=True)
    shield_no = models.IntegerField(null=True, blank=True)
    complaint_id = models.IntegerField(null=True, blank=True)
    month_received = models.IntegerField(null=True, blank=True)
    year_received = models.IntegerField(null=True, blank=True)
    month_closed = models.IntegerField(null=True, blank=True)
    year_closed = models.IntegerField(null=True, blank=True)
    command_at_incident = models.CharField(max_length=255, null=True, blank=True)
    rank_abbrev_incident = models.CharField(max_length=255, null=True, blank=True)
    rank_abbrev_now = models.CharField(max_length=255, null=True, blank=True)
    rank_now = models.CharField(max_length=255, null=True, blank=True)
    rank_incident = models.CharField(max_length=255, null=True, blank=True)

    # mos = member of service
    mos_ethnicity = models.ForeignKey(Ethnicity, related_name='mos_ethnicity', on_delete=models.CASCADE, null=True, blank=True)
    mos_gender = models.ForeignKey(Gender, related_name='mos_gender', on_delete=models.CASCADE, null=True, blank=True)
    mos_age_incident = models.IntegerField(null=True, blank=True)

    complaint_ethnicity = models.ForeignKey(Ethnicity, related_name='complaint_ethnicity', on_delete=models.CASCADE, null=True, blank=True)
    complaint_gender = models.ForeignKey(Gender, related_name='complaint_gender', on_delete=models.CASCADE, null=True, blank=True)
    complainant_age_incident = models.IntegerField(null=True, blank=True)
    fado_type = models.ForeignKey(Fado, on_delete=models.CASCADE, null=True, blank=True)
    allegation = models.ForeignKey(Allegation, on_delete=models.CASCADE, null=True, blank=True)
    precinct = models.ForeignKey(Precinct, on_delete=models.CASCADE, null=True, blank=True)
    contact_reason = models.ForeignKey(ContactReason, on_delete=models.CASCADE, null=True, blank=True)
    outcome_description = models.ForeignKey(OutcomeDescription, on_delete=models.CASCADE, null=True, blank=True)
    board_disposition = models.ForeignKey(BoardDisposition, on_delete=models.CASCADE, null=True, blank=True)
