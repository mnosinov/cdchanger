from django.urls import path
from django.views.generic import TemplateView

from .views import CdchangerListView, CdchangerWizard

urlpatterns = [
    path('', TemplateView.as_view(template_name='cdchanger/index.html'), name='index'),
    path('cdchangers', CdchangerListView.as_view(), name='cdchangers'),
    path('cdchangers/', CdchangerListView.as_view(), name='cdchangers'),
    path('cdchangers/create', CdchangerWizard.as_view(CdchangerWizard.FORMS), name='cdchanger-create-wizard'),
    # TODO
    # path('cdchangers/<int:pk>/view', CdchangerDetailView.as_view(), name='cdchanger-detail-view'),
    # path('cdchangers/<int:pk>/update', CdchangerUpdateView.as_view(), name='cdchanger-update'),
    # path('cdchangers/<int:pk>/delete', CdchangerDeleteView.as_view(), name='cdchanger-delete'),
]
