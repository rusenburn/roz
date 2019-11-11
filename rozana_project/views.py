from django.views.generic import TemplateView
from cars.models import CarModel

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['carmodel_list'] = CarModel.objects.all()
        return context
