from email.message import EmailMessage
from pyexpat.errors import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .import forms
                              

# Create your views here.

class TopView(TemplateView):
    template_name = "mondai1/top.html"

class QuestionView(FormView):
    template_name="mondai1/question.html"
    form_class=forms.QuestionForm                 
                                             
    success_url = reverse_lazy('mondai1_3:question')
    
    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['question_title']
        message = form.cleaned_data['question_detail']
        
        subject = 'お問い合わせ：{}'.format(title)
        message = '送信者名：{0}\nメールアドレス：{1}\nタイトル：{2}\nメッセージ：{3}'.format(name, email, title, message)
        
        from_email = 'admin@example.com'
        to_list = ['admin@example.com']
        
        message = EmailMessage(subject=subject, body=message, from_email=from_email,  to=to_list)
        message.send()
        
        messages.success(self.request, 'お問い合わせは正常に送信されました')
        return super().form_valid(form)
