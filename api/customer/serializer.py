from rest_framework import serializers
from api.customer.models import Hobbies ,Profile, Skill

class HobbiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobbies
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
class ProfileSerializer(serializers.ModelSerializer):
    hobbies = HobbiesSerializer(many=True,read_only=True)
    # skills = SkillSerializer(many=True,read_only=True)

    class Meta:
        model = Profile
        fields = ['__all__','hobbies']
    def create(self,validate_data):
        hobbies_data = validate_data.pop('hobbies')
        profile = Profile.objects.create(**validated_data)

        for hobb in hobbies_data:
            Hobbies.objects.create(profile=profile,**hobb)
        return profile
        # for skill in skills_data:
        #     skill.objects.create(profile=profile,**skill)
        # return profile