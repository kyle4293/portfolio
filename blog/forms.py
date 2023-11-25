from django import forms
from blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # 사용할 모델
        fields = ['title', 'content']  # PostForm에서 사용할 Post 모델의 속성
        labels = {
            'title': '제목',
            'content': '내용',
        }

