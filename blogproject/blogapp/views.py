from django.shortcuts import render
# django.views.genericからListView、DetailViewをインポート
from django.views.generic import ListView, DetailView

# モデルBlogPostをインポート
from .models import BlogPost
from django.views.generic import FormView
# django.urlsからreverse_lazyをインポート
from django.urls import reverse_lazy
# formsモジュールからContactFormをインポート
from .forms import ContactForm
# django.contribからmesseagesをインポート
from django.contrib import messages
# django.core.mailモジュールからEmailMessageをインポート
from django.core.mail import EmailMessage

class IndexView(ListView):
    '''トップページのビュー
    
    投稿記事を一覧表示するのでListViewを継承する
    
    Attributes:
      template_name: レンダリングするテンプレート
      context_object_name: object_listキーの別名を設定
      queryset: データベースのクエリ
    '''
    # index.htmlをレンダリングする
    template_name ='index.html'
    # object_listキーの別名を設定
    context_object_name = 'orderby_records'
    # モデルBlogPostのオブジェクトにorder_by()を適用して
    # BlogPostのレコードを投稿日時の降順で並べ替える
    queryset = BlogPost.objects.order_by('-posted_at')
    # 1ページに表示するレコードの件数を設定
    paginate_by = 4

class BlogDetail(DetailView):
    '''詳細ページのビュー
    
    投稿記事の詳細を表示するのでDetailViewを継承する
     Attributes:
      template_name: レンダリングするテンプレート
      Model: モデルのクラス
    '''
    # post.htmlをレンダリングする
    template_name ='post.html'
    # クラス変数modelにモデルBlogPostを設定
    model = BlogPost

class ScienceView(ListView):
    '''科学(science)カテゴリの記事を一覧表示するビュー
    
    '''
    # science_list.htmlをレンダリングする
    template_name ='science_list.html'
    # クラス変数modelにモデルBlogPostを設定
    model = BlogPost
    # object_listキーの別名を設定
    context_object_name = 'science_records'
    # category='science'のレコードを抽出して
    # 投稿日時の降順で並べ替える
    queryset = BlogPost.objects.filter(
        category='science').order_by('-posted_at')
    # 1ページに表示するレコードの件数
    paginate_by = 2

class DailylifeView(ListView):
    '''日常(dailylife)カテゴリの記事を一覧表示するビュー
    
    '''
    # dailylife_list.htmlをレンダリングする
    template_name ='dailylife_list.html'
    # クラス変数modelにモデルBlogPostを設定
    model = BlogPost
    # object_listキーの別名を設定
    context_object_name = 'dailylife_records'
    # category='dailylife'のレコードを抽出して
    # 投稿日時の降順で並べ替える
    queryset = BlogPost.objects.filter(
        category='dailylife').order_by('-posted_at')
    # 1ページに表示するレコードの件数
    paginate_by = 2

class MusicView(ListView):
    '''音楽(music)カテゴリの記事を一覧表示するビュー
    
    '''
    # music_list.htmlをレンダリングする
    template_name ='music_list.html'
    # クラス変数modelにモデルBlogPostを設定
    model = BlogPost
    # object_listキーの別名を設定
    context_object_name = 'music_records'
    # category='music'のレコードを抽出して
    # 投稿日時の降順で並べ替える
    queryset = BlogPost.objects.filter(
        category='music').order_by('-posted_at')
    # 1ページに表示するレコードの件数
    paginate_by = 2

class ContactView(FormView):
    template_name='contact.html'
    form_class=ContactForm
    success_url=reverse_lazy('blogapp:contact')
    def form_valid(self, form):
        name=form.cleaned_data['name']
        email=form.cleaned_data['email']
        title=form.cleaned_data['title']
        message=form.cleaned_data['message']
        subject='お問い合わせ:{}'.format(title)
        message=\
            '送信者名:{0}\nメールアドレス:{1}\nタイトル:{2}\nメッセージ:\n{3}'\
            .format(name,email,title,message)
        from_email='fko2547054@gmail.com'
        to_list=['fko2547054@gmail.com']
        message=EmailMessage(subject=subject,
                             body=message,
                             from_email=from_email,
                             to=to_list,
                             )
        message.send()
        messages.success(
                self.request,'お問い合わせは正常に送信されました。')
        return super().form_valid(form)
       
