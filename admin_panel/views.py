from django.shortcuts import render
from django.views.generic.base import View

class HomeView(View):
    """Home View."""

    template_name = 'admin_panel/home.html'

    def get(self, request):
        """Get request."""
        print("REQUEST",request.user)
        context = {}
        return render(request, self.template_name, context)
