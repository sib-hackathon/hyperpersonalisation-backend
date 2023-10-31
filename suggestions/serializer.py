from rest_framework import serializers

class ButtonSerializer(serializers.Serializer):
    button_id = serializers.IntegerField(source='button__id')
    button_name = serializers.CharField(source='button__name')
    count = serializers.IntegerField()
