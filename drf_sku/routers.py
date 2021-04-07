from demoApp.viewsets import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('product-api', ProductViewset)
router.register('sku-api', SkuViewset)
router.register('batch-api', BatchViewset)