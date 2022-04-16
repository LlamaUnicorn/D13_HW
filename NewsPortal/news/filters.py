from django_filters import FilterSet #, DateFilter
from .models import Post


# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.


class PostFilter(FilterSet):
    class Meta:
        # В Meta классе мы должны указать Django модель,
        # в которой будем фильтровать записи.
        model = Post
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.
        fields = {
            # поиск по названию
            'title': ['icontains'],
            'dateCreation': ['lt', 'gt'],
            'postCategory': ['exact'],
        }


# class PostFilter(FilterSet):
#     time_in = DateFilter(
#         lookup_expr='gt',
#         widget=django.forms.DateInput(
#             attrs={
#                 'type': 'date'
#             }
#         )
#     )
#
#     class Meta:
#         model = Post
#         fields = {
#             'heading': ['icontains'],
#             'author__name': ['exact'],
#             'category': ['exact'],
#
#         }