from rest_framework import serializers
from descriptions.models import Description

class CreateDescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Description
        fields = (
            'title',
            'description',
            'emoji',
            'id'
        )
        extra_kwargs = {
            'id': {'read_only': True}
        }


    def create(self, validated_data):
        #get user from request
        user = self.context['request'].user
        validated_data['user_id'] = user.id
        description = Description.objects.create(**validated_data)
        return description