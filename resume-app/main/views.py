from django.shortcuts import render
from django.contrib import messages
from .models import (
    UserProfile,
    Blog,
    Portfolio,
    Testimonial,
    Certificate,
    Work_Experience,
    # ContactProfile
)

from django.core.mail import send_mail
from django.shortcuts import render
from django.views import generic


from . forms import ContactForm


class IndexView(generic.TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        testimonials = Testimonial.objects.filter(is_active=True)
        certificates = Certificate.objects.filter(is_active=True)
        blogs = Blog.objects.filter(is_active=True)
        portfolio = Portfolio.objects.filter(is_active=True)
        work_experience = Work_Experience.objects.filter(is_active=True)

        context["testimonials"] = testimonials
        context["certificates"] = certificates
        context["blogs"] = blogs
        context["portfolio"] = portfolio
        context["work_experience"] = work_experience
        return context


class ContactView(generic.FormView):
    template_name = "main/contact.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        # Send email
            # Todo Added something like The subject should be new contact 
            # form from Name of the sender 
            # Also send the email notifying that person that mail is sent.
            # And also a validation that the mail is valid. 
            # Also research about risks and vulenebility issues here 
            # The above are future scope / things to work upon.
        send_mail(
            'New Contact Form Submission',
            f'Name: {name}\nEmail: {email}\nMessage: {message}',
            email,  # Sender's email address
            ['chinum.upadhyaya@gmail.com'],  # Recipient's email address
            fail_silently=False,
        )

        # Display success message
        messages.success(self.request, 'Thank you. We will be in touch soon.')

        return super().form_valid(form)


class PortfolioView(generic.ListView):
    model = Portfolio
    template_name = "main/portfolio.html"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = "main/portfolio-detail.html"


class BlogView(generic.ListView):
    model = Blog
    template_name = "main/blog.html"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = "main/blog-detail.html"


class Work_Experience_View(generic.ListView):
    template_name = "main/work_exp.html"
    model = Work_Experience
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Work_Experience_View_DetailView(generic.DetailView):
    model = Work_Experience
    template_name = "main/work_exp_details.html"
