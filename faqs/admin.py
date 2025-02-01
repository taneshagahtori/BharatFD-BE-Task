from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('question', 'question_hi', 'question_bn')
    search_fields = ('question',)
=======
    list_display = ('question', 'created_at', 'updated_at')
    search_fields = ('question', 'answer')
    readonly_fields = ('created_at', 'updated_at')

>>>>>>> c15f3fd (first commit)
