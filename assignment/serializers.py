from rest_framework import serializers
from django.contrib.auth import authenticate
from task.models import Language, Border, Details
from rest_framework.exceptions import AuthenticationFailed


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def authenticate(self, **kwargs):
        return authenticate(self.context['request'], **kwargs)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        usr = self.authenticate(username=username, password=password)

        if not usr:
            raise AuthenticationFailed('Invalid User')
        attrs['user'] = usr
        return attrs


class LanguageSerializer(serializers.ModelSerializer):
    borders = serializers.PrimaryKeyRelatedField(queryset=Border.objects.all(), many=True)

    class Meta:
        model = Language
        fields = "__all__"


class BorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Border
        fields = "__all__"


class DetailsSerializer(serializers.ModelSerializer):
    languages = serializers.PrimaryKeyRelatedField(queryset=Language.objects.all())
    borders = serializers.PrimaryKeyRelatedField(queryset=Border.objects.all(), many=True)
    border_detail = serializers.SerializerMethodField()

    def get_border_detail(self, obj):
        serializer = BorderSerializer(obj.borders)
        return serializer.data

    class Meta:
        model = Details
        fields = "__all__"
