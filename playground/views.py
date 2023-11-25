from django.shortcuts import render
from django.http import HttpResponse

def homepageView(request):
    return render(request, 'button.html')

def lieu1(request):
     return render(request, 'lieu1.html')

def lieu2(request):
    return render(request, 'lieu2.html')
def article_list(request):
    articles = [
        {
            'id': 1,
            'title': 'Tantsilong',
            'description': 'Tatsilong, étoile brillante de nos vies, ton héritage rayonne toujours. Ton amour et ta sagesse illuminent nos jours, éternellement gravés dans nos souvenirs.',
            'image_url': 'https://actucameroun.com/wp-content/uploads/2020/07/olivier-bibou-nissack-e1593778917400-300x200.jpg.webp',
            'link': 'https://location-du-deuil.vercel.app/playground/adresse1/',
        },
        {
            'id': 2,
            'title': 'Article 2',
            'description': 'Description for Article 2...',
            'image_url': 'https://actucameroun.com/wp-content/uploads/2019/11/cava-yeguie-djibril-ngaoundere-300x200.jpg.webp',
            'link': 'https://example.com/article2/',
        },
        {
            'id': 3,
            'title': 'Article 3',
            'description': 'Description for Article 3...',
            'image_url': 'https://actucameroun.com/wp-content/uploads/2023/11/claudel-noubissie-2-300x200.jpg.webp',
            'link': 'https://example.com/article3/',
        },
    ]

    return render(request, 'article_list.html', {'articles': articles})
