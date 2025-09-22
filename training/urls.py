from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'programs', views.ProgramViewSet)
router.register(r'program-topics', views.ProgramTopicViewSet)
router.register(r'batches', views.BatchViewSet)
router.register(r'batch-trainers', views.BatchTrainerViewSet)
router.register(r'batch-trainees', views.BatchTraineeViewSet)
router.register(r'designations', views.DesignationViewSet)
router.register(r'designation-programs', views.DesignationProgramViewSet)
router.register(r'trainee-designations', views.TraineeDesignationViewSet)
router.register(r'progress-records', views.ProgressRecordViewSet)
router.register(r'audit-logs', views.AuditLogViewSet)
urlpatterns = router.urls
