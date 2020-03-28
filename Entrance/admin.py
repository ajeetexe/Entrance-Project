from django.contrib import admin
from .models import UserInfoModel, QualificationModel, DocumentUploadModel, PreferenceModel

# Register your models here.

admin.site.register(QualificationModel)
admin.site.register(UserInfoModel)
admin.site.register(DocumentUploadModel)
admin.site.register(PreferenceModel)
