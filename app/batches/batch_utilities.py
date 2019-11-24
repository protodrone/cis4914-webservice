from api.models import Observations
from api.models import Images

def batchImageDepth(batchId):
    max_images = 0
    observations = Observations.objects.filter(upload_batch=batchId)
    for obs in observations:
        images = Images.objects.filter(observation=obs.id)
        if len(images) > max_images:
            max_images = len(images)
    return max_images