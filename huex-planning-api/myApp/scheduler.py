import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)
msg = 'Something went wrong!'

def Scheduler(data):
    """
    creates a plan for scheduling appointments
    """
    data = json.loads(data)
    try:
        # TODO: Implement schduler logic
        schedule = []
        msg = 'Successfully created a schedule'
        logger.debug(msg)
        return schedule, msg, 201
    except:
        msg = 'Failed to create a schedule'
        logger.error(msg)
        return [], msg, 400