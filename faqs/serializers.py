from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
<<<<<<< HEAD
        fields = ['id', 'question', 'answer', 'question_hi', 'question_bn']
=======
        fields = ['id', 'question', 'answer']

    def to_representation(self, instance):
        lang = self.context['request'].query_params.get('lang', 'en')
        return {
            'id': instance.id,
            'question': instance.get_translated_text('question', lang),
            'answer': instance.get_translated_text('answer', lang),
        }

>>>>>>> c15f3fd (first commit)
