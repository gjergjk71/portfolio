from django.urls import path,include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
	path("api-auth/",include('rest_framework.urls')),
    path("docs/",include_docs_urls(title="Prisma Docs")),
]
