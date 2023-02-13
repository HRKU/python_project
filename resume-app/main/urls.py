from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
	path('', views.IndexView.as_view(), name="home"),
	path('contact/', views.ContactView.as_view(), name="contact"),
	path('portfolio/', views.PortfolioView.as_view(), name="portfolios"),
	path('Work_Experience/', views.Work_Experience_View.as_view(), name="Work_Experiences"),
	path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name="portfolio"),
	path('Work_Experience/<slug:slug>', views.Work_Experience_View_DetailView.as_view(), name="Work_Experience"),
	path('blog/', views.BlogView.as_view(), name="blogs"),
	path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog"),
	]