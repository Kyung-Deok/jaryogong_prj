from django.contrib import admin
from .models import MyBoard,MyMembers,MentalServiceLocation,MemberBoard,MentalBoard

admin.site.register(MyBoard)
admin.site.register(MyMembers)
admin.site.register(MentalServiceLocation)
admin.site.register(MemberBoard)
admin.site.register(MentalBoard)