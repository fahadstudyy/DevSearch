# from django.db.models import Q
# from .models import Project, Tag

# def searchprojects(request):
#     search_query = ''
#     if request.GET.get('search_query'):
#         search_query = request.GET.get('search_query')

#     tag = Tag.objects.filter(name__icontains=search_query)
#     obj = Project.objects.distinct().filter(
#         Q(title__icontains=search_query) |
#         Q(describe__icontains=search_query) |
#         Q(owner__name__icontains=search_query) |
#         Q(tag__in=tag)
#         )
#     return obj, search_query
