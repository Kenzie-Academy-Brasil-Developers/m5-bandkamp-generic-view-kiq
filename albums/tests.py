from django.test import TestCase
from serializers import serializers
from django.db import models
# Create your tests here.

class FriendSerializer(serializers.Serializer):
    ...
class Friend(models.Model):
    ...

class Student(models.Model):
    id: models.IntegerField()
    username = models.CharField(max_length=27)
    lastname = models.CharField(max_length=54)
    module = models.CharField(max_length=27)
    team = models.CharField(max_length=27)

    friends = models.ManyToManyField('friends.Friend', related_name="students")

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("id", "username", "lastname", "module", "team")

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'username', 'lastname', 'module', 'team', 'friends']

class StudentSerializer(serializers.ModelSerializer):

    friends = FriendSerializer(many=True)
    class Meta:
        model = Student
        fields = ['id', 'username', 'lastname', 'module', 'team']