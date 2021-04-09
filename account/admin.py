
from django.contrib import admin
from .models import *

admin.site.register(User)

admin.site.register(StudentProfile)
admin.site.register(TeacherProfile)
admin.site.register(Principal)

admin.site.register(Session)
admin.site.register(Batch)
admin.site.register(Course)
admin.site.register(Unit)

admin.site.register(BatchCourse)
admin.site.register(TeacherBatchCourse)
admin.site.register(TrackProgressBatchCourse)
