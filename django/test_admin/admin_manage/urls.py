from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'users/(\d+)', views.users_id, name='users_id'),
	url('users', views.users, name='users'),
	url('recommends/add_event', views.add_event, name='add_event'),
	url('recommends/check_event', views.check_event, name='check_event'),
	url('recommends/publish_event', views.publish_event, name='publish_event'),
	url('admins/admin_power', views.admin_power, name='admin_power'),
	url('admins/admin', views.admins, name='admins_admin'),
	url(r'admins/daily/(\d+)', views.admin_daily, name='admin_daily'),
	url('add_account', views.admin_add_account, name='add_account'),
	url('delete_account', views.admin_delete_account, name='delete_account'),
	url(r'recommends/(\d+)', views.recommends_id, name='recommends_id'),
	url('recommends/search', views.recommends_search, name='recommends_search'),
	url('recommends', views.recommends, name='recommends'),
	url('login', views.login, name='login'),
	url('logout', views.logout, name='logout'),
	url('filter_user', views.filter_user, name='filter_user'),
	url('filter_recommend', views.filter_recommend, name='filter_recommend'),
	url('order_by_letter', views.order_by_letter, name='order_by_letter'),
	url('order_by_number', views.order_by_number, name='order_by_number'),
	url('order_by_time', views.order_by_time, name='order_by_time'),
	url('count', views.count, name='count'),
]