from django.db import models
import logging
import json
from multiselectfield import MultiSelectField

# Get an instance of a logger
logger = logging.getLogger(__name__)
msg = 'Something went wrong!'

class PatientsManager(models.Manager):
    def get_patient(self, pat_id):
        """
        Fetch a Patient by Id
        """
        patient = Patients.objects.filter(pat_id = pat_id)
        return patient
    
    def get_all_patients(self):
        """
        Fetch all patients
        """
        try:
            patients_list = Patients.objects.all()
            msg = 'Fetched patients list'
            logger.debug(msg)
            return patients_list, msg, 200
        except:
            msg = 'Failed to Fetched patients list'
            logger.debug(msg)
            return [], msg, 400

    def create_or_update_patient(self, data):
        """
        create a patient if no id is passed
        or 
        update the patient details based on id
        """
        data = json.loads(data)
        try:
            patient = Patients()
            # TODO: validation of data and keys in patient
            # also to implement exception handling based on validation
            for key in data:
                setattr(patient, key, data[key])
            patient.save()
            msg = 'Successfully Inserted or Updated a row'
            logger.debug(msg)
            # throw an exception if the key is not found 
            # tell django to tell it to convert it into 400 exception to the user
            return [], msg, 201
        except:
            msg = 'Unexpected error occured, Failed to modify'
            logger.error(msg)
            return [], msg, 400


class Patients(models.Model):
    """
    Patients registered for dialysis
    """
    class Meta:
        db_table = "patients"
        # index_together = [
        #     ["pat_id",],
        # ]
    MEDICAL_CONDITION = ((1, 'Diabetes'),
                     (2, 'Asthma'),
                     (3, 'Blind'),
                     (4, 'Arthritis'),
                     (5, 'Bronchitis'),
                     (6, 'Nausea'))

    PREFFERED_DAYS = ((1, 'Monday'),
                (2, 'Tuesday'),
                (3, 'Wednesday'),
                (4, 'Thursday'),
                (5, 'Friday'),
                (6, 'Saturday'),
                (7, 'Sunday'))

    PREFFERED_TIME_SLOTS = ((1, '9-12'),
             (2, '12-3'),
             (3, '3-6'),
             (4, '6-9'))

    objects = PatientsManager()
    pat_id = models.AutoField(primary_key=True)
    pat_name = models.CharField(max_length=200)
    age = models.IntegerField()
    flag = models.BooleanField()
    last_dialysis = models.DateTimeField('date of last sitting')
    next_dialysis = models.DateTimeField('date of last sitting')
    start_dialysis = models.DateTimeField()
    end_dialysis = models.DateTimeField()
    freq_dialysis = models.IntegerField()
    pref_days = MultiSelectField(choices=PREFFERED_DAYS)
    pref_time = MultiSelectField(choices=PREFFERED_TIME_SLOTS)
    duration = models.IntegerField()
    registered_date = models.DateTimeField('date of registration')
    medical_cond = MultiSelectField(choices=MEDICAL_CONDITION)
    # cen_id = models.ForeignKey(Centers, on_delete=models.CASCADE)

    def __str__(self):
        return self.pat_name


