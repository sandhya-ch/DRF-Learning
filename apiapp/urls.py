from rest_framework import routers
from apiapp.views import Snippetviewset

router=routers.SimpleRouter()
router.register(r'snippet',Snippetviewset)
urlpatterns=router.urls