from django.contrib import admin
from django.urls import path, include
from . import views
from .import HOD_views, staff_views, student_views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', views.home, name="home"),
	path('contact', views.contact, name="contact"),
	path('login', views.loginUser, name="login"),
	path('logout_user', views.logout_user, name="logout_user"),
	path('registration', views.registration, name="registration"),
	path('doLogin', views.doLogin, name="doLogin"),
	path('doRegistration', views.doRegistration, name="doRegistration"),
	
	# URLS for Student
	path('student_home/', student_views.student_home, name="student_home"),
	path('student_view_attendance/', student_views.student_view_attendance, name="student_view_attendance"),
	path('student_view_attendance_post/', student_views.student_view_attendance_post, name="student_view_attendance_post"),
	path('student_apply_leave/', student_views.student_apply_leave, name="student_apply_leave"),
	path('student_apply_leave_save/', student_views.student_apply_leave_save, name="student_apply_leave_save"),
	path('student_feedback/', student_views.student_feedback, name="student_feedback"),
	path('student_feedback_save/', student_views.student_feedback_save, name="student_feedback_save"),
	path('student_profile/', student_views.student_profile, name="student_profile"),
	path('student_profile_update/', student_views.student_profile_update, name="student_profile_update"),
	path('student_view_result/', student_views.student_view_result, name="student_view_result"),


	# URLS for Staff
	path('staff_home/', staff_views.staff_home, name="staff_home"),
	path('staff_take_attendance/', staff_views.staff_take_attendance, name="staff_take_attendance"),
	path('get_students/', staff_views.get_students, name="get_students"),
	path('save_attendance_data/', staff_views.save_attendance_data, name="save_attendance_data"),
	path('staff_update_attendance/', staff_views.staff_update_attendance, name="staff_update_attendance"),
	path('get_attendance_dates/', staff_views.get_attendance_dates, name="get_attendance_dates"),
	path('get_attendance_student/', staff_views.get_attendance_student, name="get_attendance_student"),
	path('update_attendance_data/', staff_views.update_attendance_data, name="update_attendance_data"),
	path('staff_apply_leave/', staff_views.staff_apply_leave, name="staff_apply_leave"),
	path('staff_apply_leave_save/', staff_views.staff_apply_leave_save, name="staff_apply_leave_save"),
	path('staff_feedback/', staff_views.staff_feedback, name="staff_feedback"),
	path('staff_feedback_save/', staff_views.staff_feedback_save, name="staff_feedback_save"),
	path('staff_profile/', staff_views.staff_profile, name="staff_profile"),
	path('staff_profile_update/', staff_views.staff_profile_update, name="staff_profile_update"),
	path('staff_add_result/', staff_views.staff_add_result, name="staff_add_result"),
	path('staff_add_result_save/', staff_views.staff_add_result_save, name="staff_add_result_save"),
	
	# URL for Admin
	path('admin_home/', HOD_views.admin_home, name="admin_home"),
	path('add_staff/', HOD_views.add_staff, name="add_staff"),
	path('add_staff_save/', HOD_views.add_staff_save, name="add_staff_save"),
	path('manage_staff/', HOD_views.manage_staff, name="manage_staff"),
	path('edit_staff/<staff_id>/', HOD_views.edit_staff, name="edit_staff"),
	path('edit_staff_save/', HOD_views.edit_staff_save, name="edit_staff_save"),
	path('delete_staff/<staff_id>/', HOD_views.delete_staff, name="delete_staff"),
	path('add_course/', HOD_views.add_course, name="add_course"),
	path('add_course_save/', HOD_views.add_course_save, name="add_course_save"),
	path('manage_course/', HOD_views.manage_course, name="manage_course"),
	path('edit_course/<course_id>/', HOD_views.edit_course, name="edit_course"),
	path('edit_course_save/', HOD_views.edit_course_save, name="edit_course_save"),
	path('delete_course/<course_id>/', HOD_views.delete_course, name="delete_course"),
	path('manage_session/', HOD_views.manage_session, name="manage_session"),
	path('add_session/', HOD_views.add_session, name="add_session"),
	path('add_session_save/', HOD_views.add_session_save, name="add_session_save"),
	path('edit_session/<session_id>', HOD_views.edit_session, name="edit_session"),
	path('edit_session_save/', HOD_views.edit_session_save, name="edit_session_save"),
	path('delete_session/<session_id>/', HOD_views.delete_session, name="delete_session"),
	path('add_student/', HOD_views.add_student, name="add_student"),
	path('add_student_save/', HOD_views.add_student_save, name="add_student_save"),
	path('edit_student/<student_id>', HOD_views.edit_student, name="edit_student"),
	path('edit_student_save/', HOD_views.edit_student_save, name="edit_student_save"),
	path('manage_student/', HOD_views.manage_student, name="manage_student"),
	path('delete_student/<student_id>/', HOD_views.delete_student, name="delete_student"),
	path('add_subject/', HOD_views.add_subject, name="add_subject"),
	path('add_subject_save/', HOD_views.add_subject_save, name="add_subject_save"),
	path('manage_subject/', HOD_views.manage_subject, name="manage_subject"),
	path('edit_subject/<subject_id>/', HOD_views.edit_subject, name="edit_subject"),
	path('edit_subject_save/', HOD_views.edit_subject_save, name="edit_subject_save"),
	path('delete_subject/<subject_id>/', HOD_views.delete_subject, name="delete_subject"),
	path('check_email_exist/', HOD_views.check_email_exist, name="check_email_exist"),
	path('check_username_exist/', HOD_views.check_username_exist, name="check_username_exist"),
	path('student_feedback_message/', HOD_views.student_feedback_message, name="student_feedback_message"),
	path('student_feedback_message_reply/', HOD_views.student_feedback_message_reply, name="student_feedback_message_reply"),
	path('staff_feedback_message/', HOD_views.staff_feedback_message, name="staff_feedback_message"),
	path('staff_feedback_message_reply/', HOD_views.staff_feedback_message_reply, name="staff_feedback_message_reply"),
	path('student_leave_view/', HOD_views.student_leave_view, name="student_leave_view"),
	path('student_leave_approve/<leave_id>/', HOD_views.student_leave_approve, name="student_leave_approve"),
	path('student_leave_reject/<leave_id>/', HOD_views.student_leave_reject, name="student_leave_reject"),
	path('staff_leave_view/', HOD_views.staff_leave_view, name="staff_leave_view"),
	path('staff_leave_approve/<leave_id>/', HOD_views.staff_leave_approve, name="staff_leave_approve"),
	path('staff_leave_reject/<leave_id>/', HOD_views.staff_leave_reject, name="staff_leave_reject"),
	path('admin_view_attendance/', HOD_views.admin_view_attendance, name="admin_view_attendance"),
	path('admin_get_attendance_dates/', HOD_views.admin_get_attendance_dates, name="admin_get_attendance_dates"),
	path('admin_get_attendance_student/', HOD_views.admin_get_attendance_student, name="admin_get_attendance_student"),
	path('admin_profile/', HOD_views.admin_profile, name="admin_profile"),
	path('admin_profile_update/', HOD_views.admin_profile_update, name="admin_profile_update"),
	
]