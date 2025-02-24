from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML
import tempfile
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.
    """
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]  # Ensure only logged-in users access the API

    def get_queryset(self):
        """
        Restrict users to see only their own orders unless they are staff.
        """
        user = self.request.user
        if user.is_staff:  # Admins can see all orders
            return Order.objects.all().order_by('-created_at')
        return Order.objects.filter(user=user).order_by('-created_at')  # Users see only their orders

    @action(detail=True, methods=['get'], url_path='invoice')
    def generate_invoice(self, request, pk=None):
        """
        Generate a PDF invoice for a specific order.
        """
        order = get_object_or_404(Order, id=pk)

        # Render HTML template to string
        html_string = render_to_string('orders/invoice_template.html', {'order': order})

        # Create a temporary file for the PDF
        with tempfile.NamedTemporaryFile(delete=True) as temp_file:
            HTML(string=html_string).write_pdf(temp_file.name)
            temp_file.seek(0)
            pdf = temp_file.read()

        # Return the PDF as an HTTP response
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'filename="invoice_{order.id}.pdf"'
        return response
