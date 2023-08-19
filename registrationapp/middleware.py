from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

class UnauthorizedAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Middleware to Check if request.user is authenticated 
        # and if the response status code is 403 (Forbidden)
        if not request.user.is_authenticated and response.status_code == 403:
            messages.warning(request, 'You are not authorized to access this page. Please log in.')
            return redirect(reverse('coursereg:login'))
        return response
