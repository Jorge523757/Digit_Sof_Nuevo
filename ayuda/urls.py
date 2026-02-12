"""
URLs para el Sistema de Ayuda
"""

from django.urls import path
from . import views

app_name = 'ayuda'

urlpatterns = [
    # Centro de ayuda
    path('', views.centro_ayuda, name='centro_ayuda'),
    
    # Tickets
    path('tickets/', views.mis_tickets, name='mis_tickets'),
    path('tickets/crear/', views.crear_ticket, name='crear_ticket'),
    path('tickets/<int:ticket_id>/', views.ver_ticket, name='ver_ticket'),
    path('tickets/<int:ticket_id>/cerrar/', views.cerrar_ticket, name='cerrar_ticket'),
    
    # FAQs
    path('faqs/', views.faqs, name='faqs'),
    path('faqs/<int:faq_id>/', views.ver_faq, name='ver_faq'),
]

