from django.urls import path
from core.views import pagina_inicial

app_name = 'core'

urlpatterns = [
    path('', pagina_inicial, name='index'),
]

# path('process-list-full', ProcessList.as_view(), name='process-list-full'),
# path('process-list-partner', ProcessListPartner.as_view(), name='process-list-partner'),
# path('process-list-owner', ProcessListOwner.as_view(), name='process-list-owner'),
# path('process-create', ProcessCreate.as_view(), name='process-create'),
# path('process-detail/<uuid:pk>', ProcessDetail.as_view(), name='process-detail'),
# path('process-update/<uuid:pk>', ProcessUpdate.as_view(), name='process-update'),
# path('process-delete/<uuid:pk>', ProcessDelete.as_view(), name='process-delete'),