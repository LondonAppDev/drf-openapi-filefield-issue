from rest_framework import (
    viewsets,
    serializers,
    parsers,
)

from sample import models


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Profile
        fields = ['id', 'image']
        read_only_fields = ['id']


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = models.Profile.objects.all()
    parser_classes = [parsers.FileUploadParser, parsers.MultiPartParser]
