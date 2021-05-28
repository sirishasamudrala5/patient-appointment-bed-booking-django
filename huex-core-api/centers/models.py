from django.db import models
import logging
import json
from multiselectfield import MultiSelectField

# Get an instance of a logger
logger = logging.getLogger(__name__)
msg = 'Something went wrong!'

class CentersManager(models.Manager):
    def get_center(self, cen_id):
        """
        fetch a dialysis center by it's id
        """
        try:
            center = Centers.objects.filter(cen_id = cen_id)
            msg = 'Fetched center: '+ cen_id
            logger.debug(msg)
            return center, msg, 200
        except:
            msg = 'Failed to fetched center:'+ cen_id
            logger.debug(msg)
            return [], msg, 400

    def get_all_centers(self):
        """
        fetch all dialysis centers belonging to the corporation
        """
        try:
            centers_list = Centers.objects.all()
            msg = 'Fetched centers list'
            logger.debug(msg)
            return centers_list, msg, 200
        except:
            msg = 'Failed to Fetched centers list'
            logger.debug(msg)
            return [], msg, 400

    def create_or_update_center(self, data):
        """
        create a dialysis center if no id is passed
        or 
        update the dialysis center based on id
        """
        data = json.loads(data)
        try:
            center = Centers()
            # TODO : implement data validation
            for key in data:
                setattr(center, key, data[key])
            center.save()
            msg = 'Successfully Inserted or Updated a row'
            logger.debug(msg)
            return [], msg, 201
        except:
            msg = 'Unexpected error occured, Failed to modify'
            logger.error(msg)
            return [], msg, 400

class Centers(models.Model):
    """
    dialysis centers belonging to the corporation
    """
    class Meta:
        db_table = "centers"
        # index_together = [
        #     ["cen_id",],
        # ]
    objects = CentersManager()
    cen_id = models.AutoField(primary_key=True)
    cen_location = models.CharField(max_length=200)
    cen_slots = models.IntegerField() # no.of seats alloted for dialysis

    def __str__(self):
        return self.cen_location