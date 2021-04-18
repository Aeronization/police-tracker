from django.shortcuts import render

from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from .models import (
    PoliceComplaint,
    Allegation,
    Ethnicity,
    Gender,
    Fado,
    Precinct,
    ContactReason,
    OutcomeDescription,
    BoardDisposition
)
from .serializers import (
    PoliceComplaintSerializer,
    AllegationSerializer,
    EthnicitySerializer,
    GenderSerializer,
    FadoSerializer,
    PrecinctSerializer,
    ContactReasonSerializer,
    OutcomeDescriptionSerializer,
    BoardDispositionSerializer
)

import requests
import csv
import os
import zipfile
import io
import glob
import shutil



class PoliceComplaintViewSet(ModelViewSet):
    # queryset = PoliceComplaint.objects.first()
    serializer_class = PoliceComplaintSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):

        print("Hello")

        params = self.request.query_params

        if params:
            param_dict = params.dict()
            queryset = PoliceComplaint.objects.filter(**param_dict)
        else:
            # (R. Friel - April 15, 2021) - Return the first 100 objects if no parameters are present.
            queryset = PoliceComplaint.objects.all()[:100]

        return queryset


class PoliceComplaintUpdateViewSet(ModelViewSet):
    # queryset = PoliceComplaint.objects.all()
    serializer_class = PoliceComplaintSerializer
    permission_classes = [AllowAny]


    def get_queryset(self):

        queryset = PoliceComplaint.objects.all()[:100]

        # (R. Friel - April 15, 2021) - Update all of the Complaints and add any new complaints to the DB.
        self.get_and_save_zipfile()
        self.open_save_csv_contents()
        self.delete_zip_file()

        return queryset


    def get_and_save_zipfile(self):

        # url = "https://www.propublica.org/datastore/dataset/civilian-complaints-against-new-york-city-police-officers"
        url = "https://www.propublica.org/datastore/index.php/actions/s3SecureDownloads/downloadProxy/getFile?id=UapPfnVxPMwDtYVjSxJQ5Fc4MVc1dz09"


        save_path = os.getcwd() + "/zip_contents"

        response = requests.get(url)
        zip_file = zipfile.ZipFile(io.BytesIO(response.content))
        zip_file.extractall(save_path)


    def open_save_csv_contents(self):
        found_file = glob.glob("./zip_contents/*.csv")

        if found_file:

            with open(found_file[0], 'r', newline='', encoding = 'iso-8859-1') as opened_file:
                # reader = csv.reader(opened_file, delimiter='\n',)
                reader = csv.reader(opened_file)

                for index, row in enumerate(reader):

                    # (R. Friel - April 12, 2021) - Don't try and add the header info from csv to database.
                    if index != 0:

                        # (R. Friel - April 12, 2021) - We now need to get_or_create the different foreign keys.
                        # This will be better for the relationships of the police incidents for filtering.
                        allegation, created = Allegation.objects.get_or_create(
                            allegation = row[22]
                        )
                        mos_ethnicity, created = Ethnicity.objects.get_or_create(
                            ethnicity = row[15]
                        )
                        complaint_ethnicity, created = Ethnicity.objects.get_or_create(
                            ethnicity = row[18]
                        )
                        mos_gender, created = Gender.objects.get_or_create(
                            gender = row[16]
                        )
                        complaint_gender, created = Gender.objects.get_or_create(
                            gender = row[19]
                        )
                        fado_type, created = Fado.objects.get_or_create(
                            fado = row[21]
                        )
                        precinct, created = Precinct.objects.get_or_create(
                            precinct = row[23]
                        )
                        contact_reason, created = ContactReason.objects.get_or_create(
                            contact_reason = row[24]
                        )
                        outcome_description, created = OutcomeDescription.objects.get_or_create(
                            outcome_description = row[25]
                        )
                        board_disposition, created = BoardDisposition.objects.get_or_create(
                            board_disposition = row[26]
                        )

                        PoliceComplaint.objects.get_or_create(
                            unique_mos_id = int(row[0] or 0),
                            first_name = row[1],
                            last_name = row[2],
                            command_now = row[3],
                            shield_no = int(row[4] or 0),
                            complaint_id = int(row[5] or 0),
                            month_received = int(row[6] or 0),
                            year_received = int(row[7] or 0),
                            month_closed = int(row[8] or 0),
                            year_closed = int(row[9] or 0),
                            command_at_incident = row[10],
                            rank_abbrev_incident = row[11],
                            rank_abbrev_now = row[12],
                            rank_now = row[13],
                            rank_incident = row[14],
                            mos_ethnicity = mos_ethnicity,
                            mos_gender = mos_gender,
                            mos_age_incident = int(row[17] or 0),
                            complaint_ethnicity = complaint_ethnicity,
                            complaint_gender = complaint_gender,
                            complainant_age_incident = int(row[20] or 0),
                            fado_type = fado_type,
                            allegation = allegation,
                            precinct = precinct,
                            contact_reason = contact_reason,
                            outcome_description = outcome_description,
                            board_disposition = board_disposition
                        )


    def delete_zip_file(self):

        # (R. Friel - April 12, 2021) - Remove the zip_contents directory. - 
        try:
            dir_path = f'{os.getcwd()}/zip_contents'
            shutil.rmtree(dir_path)
        except OSError as e:
            print("Error: %s : %s" % (dir_path, e.strerror))



class GenderViewSet(ModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer
    permission_classes = [AllowAny]


class AllegationViewSet(ModelViewSet):
    queryset = Allegation.objects.all()
    serializer_class = AllegationSerializer
    permission_classes = [AllowAny]


class EthnicityViewSet(ModelViewSet):
    queryset = Ethnicity.objects.all()
    serializer_class = EthnicitySerializer
    permission_classes = [AllowAny]


class FadoViewSet(ModelViewSet):
    queryset = Fado.objects.all()
    serializer_class = FadoSerializer
    permission_classes = [AllowAny]


class PrecinctViewSet(ModelViewSet):
    queryset = Precinct.objects.all()
    serializer_class = PrecinctSerializer
    permission_classes = [AllowAny]


class ContactReasonViewSet(ModelViewSet):
    queryset = ContactReason.objects.all()
    serializer_class = ContactReasonSerializer
    permission_classes = [AllowAny]


class OutcomeDescriptionReasonViewSet(ModelViewSet):
    queryset = OutcomeDescription.objects.all()
    serializer_class = OutcomeDescriptionSerializer
    permission_classes = [AllowAny]


class BoardDispositionViewSet(ModelViewSet):
    queryset = BoardDisposition.objects.all()
    serializer_class = BoardDispositionSerializer
    permission_classes = [AllowAny]