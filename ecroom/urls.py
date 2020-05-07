"""ecroom URL Configuration

"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

from account.api import views as accountViews
from student.api import views as studentViews
from school.api import views as schoolViews
from department.api import views as departmentViews
from dptclass.api import views as dptclassViews
from course.api import views as courseViews
from lesson.api import views as lessonViews
from assessment.api import views as assessmentViews
#from note.api import views as noteViews
#from video.api import views as videoViews
from question.api import views as questionViews
from book.api import views as bookViews
from teacher.api import views as teacherViews
from institute.api import views as instituteViews

from rest_framework_nested import routers
from rest_framework.routers import DefaultRouter

from account.views import (

    registration_view,
    login_view,
    logout_view,
    list_std,
    detail_std,
    load_schools,
    load_depts,
    load_deptcls,
    
)

from institute.views import (

    list_inst, 
    list_sch, 
    list_dept,
    list_dptcls,
    list_crse,
    detail_crse,
    
)

router = DefaultRouter()

# REST FRAMEWORK URLS APIV2

# router = routers.SimpleRouter()

router.register(r'accounts', accountViews.AccountViewSet, basename='accounts')
router.register(r'account/unregistered', accountViews.UnregStudentViewSet, basename='unreg-accounts')
router.register(r'account/students', accountViews.AccountStudentViewSet, basename='astudents')
router.register(r'students', studentViews.StudentViewSet, basename='students')
router.register(r'schools', schoolViews.SchoolViewSet)
router.register(r'departments', departmentViews.DepartmentViewSet, basename='departments')
router.register(r'deptclass', dptclassViews.DptClassViewSet, basename='deptclass')
router.register(r'questions', questionViews.QuestionViewSet, basename='questions')
router.register(r'courses', courseViews.CourseViewSet, basename='courses')
router.register(r'lessons', lessonViews.LessonViewSet, basename='lesson')
router.register(r'assessments', assessmentViews.AssessmentViewSet, basename='assessment')
#router.register(r'notes', noteViews.NoteViewSet, basename='notes')
#router.register(r'videos', videoViews.VideoViewSet, basename='videos')
router.register(r'books', bookViews.BookViewSet, basename='books')
router.register(r'teachers', teacherViews.TeacherViewSet, basename='teachers')
router.register(r'institutes', instituteViews.InstituteViewSet, basename='institute')


# Student Mobile API
router.register(r'student', studentViews.PStudentViewSet, basename='student')
student_router = routers.NestedDefaultRouter(router, r'student', lookup='student')
student_router.register(r'course', courseViews.SCourseViewSet, basename='student-course')
course_router = routers.NestedDefaultRouter(student_router, r'course', lookup='course')
course_router.register(r'record', studentViews.SCRecordViewSet, basename='student-course-record')
course_router.register(r'lesson', lessonViews.SCLessonViewSet, basename='student-course-lesson')
course_router.register(r'assessment', assessmentViews.SCAssessViewSet, basename='student-course-ssessment')
lesson_router = routers.NestedDefaultRouter(course_router, r'lesson', lookup='lesson')


# Teacher API
teacher_course_router = routers.NestedDefaultRouter(router, r'teachers', lookup='teacher_id')
teacher_course_router.register(r'courses', teacherViews.TCourseViewSet, basename='teacher')


# Backend Institute API
router.register(r'inst', instituteViews.DInstViewSet, basename='inst')
inst_router = routers.NestedDefaultRouter(router, r'inst', lookup='inst')
inst_router.register(r'sch', schoolViews.ISchoolViewSet, basename='inst-sch')
sch_router = routers.NestedDefaultRouter(inst_router, r'sch', lookup='sch')
sch_router.register(r'dept', departmentViews.IDeptViewSet, basename='sch-dept')
dept_router = routers.NestedDefaultRouter(sch_router, r'dept', lookup='dept')
dept_router.register(r'dptcls', dptclassViews.IDptclsViewSet, basename='dept-dptcls')
dptcls_router = routers.NestedDefaultRouter(dept_router, r'dptcls', lookup='dptcls')
dptcls_router.register(r'crse', courseViews.ICrseViewSet, basename='dptcls-crse')
crse_router = routers.NestedDefaultRouter(dptcls_router, r'crse', lookup='crse')
crse_router.register(r'lsn', lessonViews.ILessonViewSet, basename='crse-lsn')
crse_router.register(r'ass', assessmentViews.IAssessViewSet, basename='crse-ass')
lsn_router = routers.NestedDefaultRouter(crse_router, r'lsn', lookup='lsn')


# Backend Student API
router.register(r'binst', accountViews.BSInstViewSet, basename='binst')
binst_router = routers.NestedDefaultRouter(router, r'binst', lookup='binst')
binst_router.register(r'bsch', accountViews.BSSchoolViewSet, basename='binst-bsch')
bsch_router = routers.NestedDefaultRouter(binst_router, r'bsch', lookup='bsch')
bsch_router.register(r'bdept', accountViews.BSDeptViewSet, basename='bsch-bdept')
bdept_router = routers.NestedDefaultRouter(bsch_router, r'bdept', lookup='bdept')
bdept_router.register(r'bdptcls', accountViews.BSDptclsViewSet, basename='bdept-bdptcls')
bdptcls_router = routers.NestedDefaultRouter(bdept_router, r'bdptcls', lookup='bdptcls')



# REST FRAMEWORK URLS APIV1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', include('account.api.urls', 'account_api')),
    path('member/register/', registration_view, name="register"),
    path('member/login/', login_view, name="login"),
    path('member/logout/', logout_view, name="logout"),
    path('api/', include(router.urls)),
    path('api/', include(student_router.urls)),
    path('api/', include(course_router.urls)),
    path('api/', include(lesson_router.urls)),
    path('api/', include(inst_router.urls)),
    path('api/', include(sch_router.urls)),
    path('api/', include(dept_router.urls)),
    path('api/', include(dptcls_router.urls)),
    path('api/', include(crse_router.urls)),
    path('api/', include(lsn_router.urls)),
    path('api/', include(binst_router.urls)),
    path('api/', include(bsch_router.urls)),
    path('api/', include(bdept_router.urls)),
    path('api/', include(bdptcls_router.urls)),
    path('', list_inst, name="list_inst"),
    path('institute/<id>/schools/', list_sch, name="list_sch"),
    path('institute/<id>/schools/<sid>/departments/', list_dept, name="list_dept"),
    path('institute/<id>/schools/<sid>/departments/<did>/classes/', list_dptcls, name="list_dptcls"),
    path('institute/<id>/schools/<sid>/departments/<did>/classes/<dcid>/courses/', list_crse, name="list_crse"),
    path('institute/<id>/schools/<sid>/departments/<did>/classes/<dcid>/courses/<cid>/cdetail/', detail_crse, name="detail_crse"),
    path('ourstudents', list_std, name="list_std"),
    path('stdprofile/<id>/', detail_std, name="detail_std"),
    #path('student/', list_std, name="list_std"),
    #path('teacher/', list_tch, name="list_tch"),
    #path('test/', list_test, name="list_test"),
    path('ajax/load_schools/', load_schools,name='ajax_load_schools'),
    path('ajax/load_depts/', load_depts,name='ajax_load_depts'),
    path('ajax/load_deptcls/', load_deptcls,name='ajax_load_deptcls'),

    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),
]
