from rest_framework import viewsets, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response

from courses import serializers, paginatior
from courses.models import Category, Course


class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all();
    serializer_class = serializers.CategorySerializer


class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.objects.filter(active=True)
    serializer_class = serializers.CourseSerializer
    pagination_class = paginatior.ItemPaginator

    def get_queryset(self):
        queryset = self.queryset

        kw = self.request.query_params.get('kw')
        if kw:
            queryset = queryset.filter(subject__icontains=kw)

        cate_id = self.request.query_params.get('category_id')
        if cate_id:
            queryset = queryset.filter(category_id=cate_id)

        return queryset


    @action(methods=['get'], url_path='lessons', detail=True)
    def get_lessons(self, request, pk):
        return Response(status=status.HTTP_200_OK)