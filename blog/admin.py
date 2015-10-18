from django.contrib import admin
from blog.models import Categorie, Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date', 'apercuContenu')
    list_filter = ('auteur', 'categorie')
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('titre', 'contenu')
    #fields = ('titre', 'auteur', 'categorie', 'contenu') #Either fields or fieldsets
    fieldsets = (
    # Fieldset 1 : meta-info (titre, auteur…)
   ('Général', {
        'classes': ['collapse',],
        'fields': ('titre', 'auteur', 'categorie')
    }),
    # Fieldset 2 : contenu de l'article
    ('Contenu de l\'article', {
       'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
       'fields': ('contenu', )
    }),
)
    
    def apercuContenu(self, article):
        text = article.contenu[0:40]
        if len(article.contenu) > 40:
            return '%s...' % text
        else:
            return text
            
    apercuContenu.short_description = 'Apercu du contenu'
    

admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)