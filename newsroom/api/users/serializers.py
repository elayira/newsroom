from rest_framework import serializers
from .models import User, Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        read_only=True,
        lookup_field='username'
    )
    url = serializers.HyperlinkedIdentityField(
        view_name='profile-detail',
        lookup_field='pk'
    )

    class Meta:
        model = Profile
        fields = ('bio', 'user', 'url')


class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='user-detail',
        lookup_field='username'
    )
    profile = ProfileSerializer(required=False)

    def create(self, validated_data):
        # call create_user on user object. Without this
        # the password will be stored in plain text.
        try:
            profile_data = validated_data.pop('profile')
        except KeyError:
            profile_data = {}

        user = User.objects.create_user(**validated_data)
        for key, value in profile_data.items():
            setattr(user.profile, key, value)
        user.save()
        return user

    def update(self, instance, validated_data):
        try:
            profile_data = validated_data.pop('profile')
        except KeyError:
            profile_data = {}

        for key, value in profile_data.items():
            setattr(instance.profile, key, value)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('password', 'first_name', 'username', 'last_name', 'email', 'profile', 'url', 'id')
        extra_kwargs = {'password': {'write_only': True}, 'url': {'lookup_field': 'username'}}
