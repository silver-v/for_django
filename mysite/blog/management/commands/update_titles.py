from django.core.management.base import BaseCommand, CommandError
from blog.models import Article

class Command(BaseCommand):
    help = 'Update'


    def handle(self, *args, **options):
        for article in Article.objects.all():
            article.title = '111'
            article.save()