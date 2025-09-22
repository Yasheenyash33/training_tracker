from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import User, Program, ProgramTopic, Batch, BatchTrainer, BatchTrainee, Designation, DesignationProgram, TraineeDesignation, ProgressRecord, AuditLog
from .serializers import *
from .permissions import IsAdmin, IsTrainerOrAdmin

class StandardListMixin:
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ()
    ordering_fields = '__all__'
    filterset_fields = ()

class UserViewSet(viewsets.ModelViewSet, StandardListMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]
    search_fields = ('username','email','first_name','last_name')
    ordering_fields = ('id','username','email')

class ProgramViewSet(viewsets.ModelViewSet, StandardListMixin):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [IsAdmin]
    search_fields = ('name','description')
    filterset_fields = ('is_active',)
    ordering_fields = ('name','created_at')

class ProgramTopicViewSet(viewsets.ModelViewSet, StandardListMixin):
    queryset = ProgramTopic.objects.all()
    serializer_class = ProgramTopicSerializer
    permission_classes = [IsAdmin]
    filterset_fields = ('program',)

class BatchViewSet(viewsets.ModelViewSet, StandardListMixin):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    permission_classes = [IsTrainerOrAdmin]
    search_fields = ('name',)
    filterset_fields = ('program','status')
    ordering_fields = ('start_date','end_date')

class BatchTrainerViewSet(viewsets.ModelViewSet, StandardListMixin):
    queryset = BatchTrainer.objects.all()
    serializer_class = BatchTrainerSerializer
    permission_classes = [IsTrainerOrAdmin]

class BatchTraineeViewSet(viewsets.ModelViewSet, StandardListMixin):
    queryset = BatchTrainee.objects.all()
    serializer_class = BatchTraineeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ('batch','trainee','status')
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return BatchTrainee.objects.all()
        if getattr(user,'role','') == 'trainee':
            return BatchTrainee.objects.filter(trainee=user)
        return BatchTrainee.objects.all()

class DesignationViewSet(viewsets.ModelViewSet, StandardListMixin):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    permission_classes = [IsAdmin]

class DesignationProgramViewSet(viewsets.ModelViewSet, StandardListMixin):
    queryset = DesignationProgram.objects.all()
    serializer_class = DesignationProgramSerializer
    permission_classes = [IsAdmin]

class TraineeDesignationViewSet(viewsets.ModelViewSet, StandardListMixin):
    queryset = TraineeDesignation.objects.all()
    serializer_class = TraineeDesignationSerializer
    permission_classes = [IsAdmin]

class ProgressRecordViewSet(viewsets.ModelViewSet, StandardListMixin):
    queryset = ProgressRecord.objects.all()
    serializer_class = ProgressRecordSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ('trainee','batch','status')
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return ProgressRecord.objects.all()
        return ProgressRecord.objects.filter(trainee=user)
    def perform_create(self, serializer):
        user = self.request.user
        if getattr(user,'role','') == 'trainee':
            serializer.save(trainee=user, updated_by=user)
        else:
            serializer.save()

class AuditLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AuditLog.objects.all().order_by('-created_at')
    serializer_class = AuditLogSerializer
    permission_classes = [permissions.IsAdminUser]
