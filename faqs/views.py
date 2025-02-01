<<<<<<< HEAD
=======
from django.core.cache import cache
>>>>>>> c15f3fd (first commit)
from rest_framework import viewsets
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer

<<<<<<< HEAD
from django.core.cache import cache

class FAQViewSet(viewsets.ModelViewSet):
=======
class FAQViewSet(viewsets.ReadOnlyModelViewSet):
>>>>>>> c15f3fd (first commit)
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def list(self, request, *args, **kwargs):
        lang = request.query_params.get('lang', 'en')
<<<<<<< HEAD
        faqs = FAQ.objects.all()
        for faq in faqs:
            faq.question = faq.get_translated_question(lang)
        serializer = FAQSerializer(faqs, many=True)
        return Response(serializer.data)



def get_cached_translation(faq, lang):
    cache_key = f"faq_{faq.id}_{lang}"
    translation = cache.get(cache_key)
    if not translation:
        translation = faq.get_translated_question(lang)
        cache.set(cache_key, translation, timeout=60*15)  # Cache for 15 minutes
    return translation
=======
        cache_key = f'faq_list_{lang}'
        cached_data = cache.get(cache_key)

        if cached_data is None:
            response = super().list(request, *args, **kwargs)
            cache.set(cache_key, response.data, timeout=3600)  # Cache for 1 hour
            return response

        return Response(cached_data)

>>>>>>> c15f3fd (first commit)
