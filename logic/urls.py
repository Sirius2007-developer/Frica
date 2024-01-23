from django.urls import path
from .views import index, contact, about, service, team, menu, testimonial, birthdaydetailview,\
    weddingdetailview, customdetailview, categorydetailview, teamdetailview, testimonialdetailview,\
    birthdayCreateView, birthdayDeleteView, birthdayUpdateView, weddingCreateView, weddingDeleteView,\
    weddingUpdateView, categoryUpdateView, categoryCreateView, categoryDeleteView, customCreateView,\
    customDeleteView, customUpdateView, teamDeleteView, teamUpdateView, teamCreateView, testimonialCreateView,\
    testimonialDeleteView, testimonialUpdateView

urlpatterns = [
    path('testimonial/create/', testimonialCreateView.as_view(), name="testimonialCreateView"),
    path('team/create/', teamCreateView.as_view(), name="teamCreateView"),
    path('birthday/create/', birthdayCreateView.as_view(), name="birthdayCreateView"),
    path('wedding/create/', weddingCreateView.as_view(), name="weddingCreateView"),
    path('custom/create/', customCreateView.as_view(), name="customCreateView"),
    path('category/create/', categoryCreateView.as_view(), name="categoryCreateView"),
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('service/', service, name='service'),
    path('team/', team, name='team'),
    path('menu/', menu, name='menu'),
    path('testimonial/', testimonial, name='testimonial'),
    path('birthday/<slug:birthday>/', birthdaydetailview, name="birthdaydetail"),
    path('birthday/delete/<slug>/', birthdayDeleteView.as_view(), name="birthdayDeleteView"),
    path('birthday/edit/<slug>/', birthdayUpdateView.as_view(), name="birthdayUpdateView"),
    path('wedding/<slug:wedding>/', weddingdetailview, name="weddingdetail"),
    path('wedding/delete/<slug>/', weddingDeleteView.as_view(), name="weddingDeleteView"),
    path('wedding/edit/<slug>/', weddingUpdateView.as_view(), name="weddingUpdateView"),
    path('custom/<slug:custom>/', customdetailview, name="customdetail"),
    path('custom/delete/<slug>/', customDeleteView.as_view(), name="customDeleteView"),
    path('custom/edit/<slug>/', customUpdateView.as_view(), name="customUpdateView"),
    path('category/<slug:category>/', categorydetailview, name="categorydetail"),
    path('category/delete/<slug>/', categoryDeleteView.as_view(), name="categoryDeleteView"),
    path('category/edit/<slug>/', categoryUpdateView.as_view(), name="categoryUpdateView"),
    path('team/<slug:team>/', teamdetailview, name="teamdetail"),
    path('team/delete/<slug>/', teamDeleteView.as_view(), name="teamDeleteView"),
    path('team/edit/<slug>/', teamUpdateView.as_view(), name="teamUpdateView"),
    path('testimonial/<slug:testimonial>/', testimonialdetailview, name='testimonialdetail'),
    path('testimonial/delete/<slug>/', testimonialDeleteView.as_view(), name="testimonialDeleteView"),
    path('testimonial/edit/<slug>/', testimonialUpdateView.as_view(), name="testimonialUpdateView"),
]
