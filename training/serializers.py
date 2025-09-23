from rest_framework import serializers
from django.conf import settings
from django.contrib.auth.password_validation import validate_password
from .models import User, Program, ProgramTopic, Batch, BatchTrainer, BatchTrainee, Designation, DesignationProgram, TraineeDesignation, ProgressRecord, AuditLog, PasswordResetToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','first_name','last_name','phone','role','is_active_flag']

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    role = serializers.ChoiceField(choices=User.ROLE_CHOICES, default='trainee')

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'first_name',
                 'last_name', 'phone', 'role')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("No user found with this email address.")
        return value

class PasswordResetSerializer(serializers.Serializer):
    token = serializers.CharField()
    new_password = serializers.CharField(write_only=True, validators=[validate_password])
    new_password2 = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs['new_password'] != attrs['new_password2']:
            raise serializers.ValidationError({"new_password": "Password fields didn't match."})

        # Validate token
        try:
            reset_token = PasswordResetToken.objects.get(
                token=attrs['token'],
                is_used=False
            )
            if reset_token.is_expired():
                raise serializers.ValidationError({"token": "Token has expired."})
        except PasswordResetToken.DoesNotExist:
            raise serializers.ValidationError({"token": "Invalid token."})

        attrs['reset_token'] = reset_token
        return attrs

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
