from rest_framework import serializers
from task.models import Language, Border, Details


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


# class SpeakSerializer(serializers.ModelSerializer):
#     name = serializers.PrimaryKeyRelatedField(queryset=Language.objects.all(), many=True)
#     border = serializers.PrimaryKeyRelatedField(queryset=Border.objects.all(), many=True)
#
#     class Meta:
#         model = Speak_language
#         fields = "__all__"
