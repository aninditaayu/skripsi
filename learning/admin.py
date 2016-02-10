from django.contrib import admin
from learning.models import Bab, Materi, Soal, Jawaban, UserProfile, UserProfileKey



class BabAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('nama',)}

class MateriAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('judul_materi',)}

admin.site.register(UserProfile)
admin.site.register(UserProfileKey)
admin.site.register(Bab, BabAdmin)
admin.site.register(Materi, MateriAdmin)
admin.site.register(Soal)
admin.site.register(Jawaban)
