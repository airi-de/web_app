from django import forms                   

class QuestionForm(forms.Form):
    name = forms.CharField(label='お名前')
    email = forms.EmailField(label='メールアドレス')
    question_title = forms.CharField(label='質問タイトル')
    question_detail = forms.CharField(label='質問詳細', widget=forms.Textarea)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['name'].widget.attrs['placeholder'] = 'お名前を入力してください'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスを入力してください'
        self.fields['email'].widget.attrs['class'] = 'form-control'

        self.fields['question_title'].widget.attrs['placeholder']='質問タイトルを入力してください'
        self.fields['question_title'].widget.attrs['class']='form-control'
        self.fields['question_detail'].widget.attrs['placeholder']='質問タイトルを入力してください'
        self.fields['question_detail'].widget.attrs['class']='form-control'


                                                           
                                                           

                                                            
                                                           