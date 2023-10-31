from rest_framework import serializers
from users.models import User, GeneralSettings

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

        # def to_representation(self, instance):
        #   data = super().to_representation(instance)
        #   del data['password']


class GeneralSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralSettings
        fields = ['user', 'e_lock_enabled', 'e_lock_enabled_date', 'e_lock_updated_date', 'debit_card_limit']

class UserAndGeneralSettingsSerializer(serializers.Serializer):
    user = UserSerializer()
    general_settings = GeneralSettingsSerializer()

    class Meta:
        fields = ['user', 'general_settings']
