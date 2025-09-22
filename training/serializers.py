from rest_framework import serializers
from django.conf import settings
from .models import User, Program, ProgramTopic, Batch, BatchTrainer, BatchTrainee, Designation, DesignationProgram, TraineeDesignation, ProgressRecord, AuditLog

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','first_name','last_name','phone','role','is_active_flag']

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'

class ProgramTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramTopic
        fields = '__all__'

class ProgramSerializer(serializers.ModelSerializer):
    topics = ProgramTopicSerializer(many=True, read_only=True)
    class Meta:
        model = Program
        fields = '__all__'

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'

class BatchTrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BatchTrainer
        fields = '__all__'

class BatchTraineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BatchTrainee
        fields = '__all__'

class DesignationProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesignationProgram
        fields = '__all__'

class TraineeDesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TraineeDesignation
        fields = '__all__'

class ProgressRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressRecord
        fields = '__all__'

class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
        fields = '__all__'
        read_only_fields = ('created_at',)
