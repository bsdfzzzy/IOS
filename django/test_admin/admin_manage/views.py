from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from django.views import generic
from model.models import Admin, User, Contact, Event, RecommendEvent
import json, datetime

def index(request):
	return render(request, 'admin_manage/login.html')
def login(request):
	if request.method == 'POST':
		data = request.POST
		try:
			a = Admin.objects.get(name=data['name'])
			if a.password == data['password']:
				if request.META.has_key('HTTP_X_FORWARDED_FOR'):  
    					ip =  request.META['HTTP_X_FORWARDED_FOR'] 
    					request.session['admin_ip'] = ip
    					if a.admin_ip != ip:
    						a.admin_ip = ip
    						a.save()
				else:  
    					ip = request.META['REMOTE_ADDR'] 
    					request.session['admin_ip'] = ip
    					if a.admin_ip != ip:
    						a.admin_ip = ip
    						a.save()
				request.session['admin_id'] = a.id
				return HttpResponseRedirect('/admin_manage/users')
			else:
				context = {'code' : 2}
				return render(request, 'admin_manage/login.html', context)
		except Admin.DoesNotExist:
			context = {'code' : 1}
			return render(request, 'admin_manage/login.html', context)
	else:
		return render(request, 'admin_manage/login.html')
def logout(request):
	del request.session['admin_id']
	return HttpResponseRedirect('/admin_manage/login')
def users(request):
	users = User.objects.all()
	if 'admin_ip' in request.session:
		ip = request.session['admin_ip']
		if 'admin_id' in request.session:
			admin = Admin.objects.get(id=request.session['admin_id'])
			if admin.admin_ip != ip:
				del request.session['admin_id']
				return HttpResponseRedirect('/admin_manage/login')
			else:
				for user in users:
					events = user.event_set.all()
					user.all_events_num = len(events)
					now = datetime.datetime.now()
					seven_days_ago = now + datetime.timedelta(days = -7)
					recent_seven_days_events = user.event_set.filter(start_time__range=(seven_days_ago, now))
					user.recent_seven_days_events_num = len(recent_seven_days_events)
				context = {'choice' : 1, 'users' : users, 'admin' : admin}
				return render(request, 'admin_manage/users.html', context)
		else:
			return HttpResponseRedirect('/admin_manage/login')
	else:
		return HttpResponseRedirect('/admin_manage/login')
def users_id(request, id):
	admin = Admin.objects.get(id=request.session['admin_id'])
	user = User.objects.get(id=id)
	events = user.event_set.all()
	user.all_events_num = len(events)
	now = datetime.datetime.now()
	seven_days_ago = now + datetime.timedelta(days = -7)
	recent_seven_days_events = user.event_set.filter(start_time__range=(seven_days_ago, now))
	user.recent_seven_days_events_num = len(recent_seven_days_events)
	linkmans = user.contact_set.all()
	for linkman in linkmans:
		q = User.objects.get(email=linkman.email, phone=linkman.phone)
		if q :
			linkman['is_user'] = 'Y'
		else:
			linkman['is_user'] = 'N'
	for event in events:
		groups = event.groupmember_set.all()
		invite = len(groups)
		join_in = 0
		maybe = 0
		no = 0
		for group in groups:
			if group.STATUS_CHOICES == 'Y':
				join_in += 1
			elif group.STATUS_CHOICES == 'M':
				maybe += 1
			else :
				no += 1
		event['invite'] = invite
		event['join_in'] = join_in
		event['maybe'] = maybe
		event['no'] = no
	contacts = ''
	context = {'choice' : 1, 'user' : user, 'events' : events, 'linkmans' : linkmans, 'contacts' : contacts, 'admin' : admin}
	return render(request, 'admin_manage/user.html', context)
def admins(request):
	if 'admin_ip' in request.session:
		ip = request.session['admin_ip']
		if 'admin_id' in request.session:
			admin = Admin.objects.get(id=request.session['admin_id'])
			if admin.admin_ip != ip:
				del request.session['admin_ip']
				return HttpResponseRedirect('/admin_manage/login')
			else:
				admins = Admin.objects.all()
				context = {'choice' : 4, 'admins' : admins, 'admin' : admin}
				return render_to_response('admin_manage/admins.html', context)
		else:
			return HttpResponseRedirect('/admin_manage/login')
	else:
		return HttpResponseRedirect('/admin_manage/login')
def admin_add_account(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		#this should judge if the user is super
		new_admin = Admin(name=data['name'], password=data['password'], admin_type=data['type'])
		new_admin.save()
		code = JsonResponse({'code' : 1})
		return(code)
def admin_delete_account(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		delete_admin = Admin.objects.get(id=data['id'])
		delete_admin.delete()
		code = JsonResponse({'code' : 1})
		return(code)
def admin_power(request):
	if request.method == 'GET':
		if 'admin_id' in request.session:
			admin = Admin.objects.get(id=request.session['admin_id'])
			admins = Admin.objects.all()
			context = {'choice' : 4 , 'admins' : admins, 'admin' : admin}
			return render_to_response('admin_manage/admin-power.html', context)
		else:
			return HttpResponseRedirect('/admin_manage/login')
	if request.method == 'POST':
		data = json.loads(request.body)
		p = Admin.objects.get(id=data['id'])
		p.admin_type = data['type']
		p.save()
		code = JsonResponse({'code': 1})
		return (code)
def admin_daily(request, id):
	if 'admin_id' in request.session:
		admin = Admin.objects.get(id=id)
		dailys = admin.admindaily_set.all()
		context = {'choice' : 4, 'admin' : admin, 'dailys' : dailys}
		return render_to_response('admin_manage/admin-daily.html', context)
	else:
		return HttpResponseRedirect('/admin_manage/login')
def recommends(request):
	if 'admin_ip' in request.session:
		ip = request.session['admin_ip']
		if 'admin_id' in request.session:
			admin = Admin.objects.get(id=request.session['admin_id'])
			if admin.admin_ip != ip:
				del request.session['admin_ip']
				return HttpResponseRedirect('/admin_manage/login')
			else:
				recommends = RecommendEvent.objects.all()
				for recommend in recommends:
					if recommend.publish_admin_id:
						recommend.publish_name = Admin.objects.get(id=recommend.publish_admin_id).name
					if recommend.check_admin_id:
						recommend.check_name = Admin.objects.get(id=recommend.check_admin_id).name
				context = {'choice' : 2, 'recommends' : recommends, 'admin' : admin}
				return render(request, 'admin_manage/recommends.html', context)
		else:
			return HttpResponseRedirect('/admin_manage/login')
	else:
		return HttpResponseRedirect('/admin_manage/login')
def recommends_id(request, id):
	admin = Admin.objects.get(id=request.session['admin_id'])
	recommend = RecommendEvent.objects.get(id=id)
	context = {'choice' : 2, 'recommend' : recommend, 'admin' : admin}
	return render(request, 'admin_manage/recommend.html', context)
def filter_user(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		addresses = data['addresses']
		events = data['events']
		date = data['date']
		users = []
		for number in events:
			if number == 0:
				now = datetime.datetime.now()
				seven_days_ago = now + datetime.timedelta(days = -7)
				users_ = User.objects.all()
				for user in users_:
					events = user.event_set.filter(start_time__range=(seven_days_ago, now))
					if len(events) == 0:
						users.append(user)
			elif number == 1:
				now = datetime.datetime.now()
				seven_days_ago = now + datetime.timedelta(days = -7)
				users_ = User.objects.all()
				for user in users_:
					events = user.event_set.filter(start_time__range=(seven_days_ago, now))
					if len(events) == 1:
						users.append(user)
			elif number == 2:
				now = datetime.datetime.now()
				seven_days_ago = now + datetime.timedelta(days = -7)
				users_ = User.objects.all()
				for user in users_:
					events = user.event_set.filter(start_time__range=(seven_days_ago, now))
					if len(events) >= 2 and len(events) <= 5:
						users.append(user)
			elif number == 3:
				now = datetime.datetime.now()
				seven_days_ago = now + datetime.timedelta(days = -7)
				users_ = User.objects.all()
				for user in users_:
					events = user.event_set.filter(start_time__range=(seven_days_ago, now))
					if len(events) >= 6 and len(events) <= 10:
						users.append(user)
			elif number == 4:
				now = datetime.datetime.now()
				seven_days_ago = now + datetime.timedelta(days = -7)
				users_ = User.objects.all()
				for user in users_:
					events = user.event_set.filter(start_time__range=(seven_days_ago, now))
					if len(events) >= 10 and len(events) <= 20:
						users.append(user)
			else:
				now = datetime.datetime.now()
				seven_days_ago = now + datetime.timedelta(days = -7)
				users_ = User.objects.all()
				for user in users_:
					events = user.event_set.filter(start_time__range=(seven_days_ago, now))
					if len(events) >20:
						users.append(user)
		if date.has_key('year'):
			if date['year'] == '0':
				start_date = datetime.date(2016,1,1)
				end_date = datetime.date(2020,12,31)
				users_ = User.objects.filter(create_time__range=(start_date, end_date))
				for user in users_:
					users.append(user)
			else:
				if date['month'] == '0':
					year = date['year']
					start_date = datetime.date(int(year),1,1)
					end_date = datetime.date(int(year),12,31)
					users_ = User.objects.filter(create_time__range=(start_date, end_date))
					for user in users_:
						users.append(user)
				else:
					if date['day'] == '0':
						year = date['year']
						month = data['month']
						start_date = datetime.date(int(year),int(month),1)
						end_date = datetime.date(int(year),int(month),31)
						users_ = User.objects.filter(create_time__range=(start_date, end_date))
						for user in users_:
							users.append(user)
					else:
						year = date['year']
						month = date['month']
						day = date['day']
						start_date = datetime.date(int(year),int(month),int(day))
						end_date = datetime.date(int(year),int(month),int(day))
						users_ = User.objects.filter(create_time__range=(start_date, end_date))
						for user in users_:
							users.append(user)
		for user in users:
			events = user.event_set.all()
			user.all_events_num = len(events)
			now = datetime.datetime.now()
			seven_days_ago = now + datetime.timedelta(days = -7)
			recent_seven_days_events = user.event_set.filter(start_time__range=(seven_days_ago, now))
			user.recent_seven_days_events_num = len(recent_seven_days_events)
		context = JsonResponse({'choice' : 1, 'users' : users})
		return context
def filter_recommend(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		addresses = data['addresses']
		categorys = data['categorys']
		date = data['date']
		recommends = []
		for number in categorys:
			if number == 1:
				recommends_ = RecommendEvent.objects.filter(category__category_id='1')
				for recommend in recommends_:
					recommends.append(recommend)
			elif number == 2:
				recommends_ = RecommendEvent.objects.filter(category__category_id='2')
				for recommend in recommends_:
					recommends.append(recommend)
			elif number == 3:
				recommends_ = RecommendEvent.objects.filter(category__category_id='3')
				for recommend in recommends_:
					recommends.append(recommend)
			elif number == 4:
				recommends_ = RecommendEvent.objects.filter(category__category_id='4')
				for recommend in recommends_:
					recommends.append(recommend)
			elif number == 5:
				recommends_ = RecommendEvent.objects.filter(category__category_id='5')
				for recommend in recommends_:
					recommends.append(recommend)
			elif number == 6:
				recommends_ = RecommendEvent.objects.filter(category__category_id='6')
				for recommend in recommends_:
					recommends.append(recommend)
			elif number == 7:
				recommends_ = RecommendEvent.objects.filter(category__category_id='7')
				for recommend in recommends_:
					recommends.append(recommend)
			elif number == 8:
				recommends_ = RecommendEvent.objects.filter(category__category_id='8')
				for recommend in recommends_:
					recommends.append(recommend)
			elif number == 9:
				recommends_ = RecommendEvent.objects.filter(category__category_id='9')
				for recommend in recommends_:
					recommends.append(recommend)
			else:
				recommends_ = RecommendEvent.objects.filter(category__category_id='10')
				for recommend in recommends_:
					recommends.append(recommend)
		if date.has_key('year'):
			if date['year'] == '0':
				start_date = datetime.date(2016,1,1)
				end_date = datetime.date(2020,12,31)
				recommends_ = RecommendEvent.objects.filter(start_time__range=(start_date, end_date))
				for recommend in recommends_:
					recommends.append(recommend)
			else:
				if date['month'] == '0':
					year = date['year']
					start_date = datetime.date(int(year),1,1)
					end_date = datetime.date(int(year),12,31)
					recommends_ = RecommendEvent.objects.filter(start_time__range=(start_date, end_date))
					for recommend in recommends_:
						recommends.append(recommend)
				else:
					if date['day'] == '0':
						year = date['year']
						month = data['month']
						start_date = datetime.date(int(year),int(month),1)
						end_date = datetime.date(int(year),int(month),31)
						recommends_ = RecommendEvent.objects.filter(start_time__range=(start_date, end_date))
						for recommend in recommends_:
							recommends.append(recommend)
					else:
						year = date['year']
						month = date['month']
						day = date['day']
						start_date = datetime.date(int(year),int(month),int(day))
						end_date = datetime.date(int(year),int(month),int(day))
						recommends_ = RecommendEvent.objects.filter(start_time__range=(start_date, end_date))
						for recommend in recommends_:
							recommends.append(recommend)
		context = JsonResponse({'choice' : 1, 'recommends' : recommends})
		return context
def filter_by_address(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		users = User.objects.get(address=data['id'])
		context = {'choice' : 1, 'users' : users}
		return render(request, 'admin_manage/users.html', context)
def filter_by_time(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		if data['year'] == 0:
			start_date = datetime.date(2016,1,1)
			end_date = datetime.date(2020,12,31)
			users = User.objects.filter(create_time__range=(start_date, end_date))
			context = {'choice' : 1, 'users' : users}
			return render(request, 'admin_manage/users.html', context)
		else:
			if data['month'] == 0:
				year = data['year']
				start_date = datetime.date(year,1,1)
				end_date = datetime.date(year,12,31)
				users = User.objects.filter(create_time__range=(start_date, end_date))
				context = {'choice' : 1, 'users' : users}
				return render(request, 'admin_manage/users.html', context)
			else:
				if data['day'] == 0:
					year = data['year']
					month = data['month']
					start_date = datetime.date(year,month,1)
					end_date = datetime.date(year,month,31)
					users = User.objects.filter(create_time__range=(start_date, end_date))
					context = {'choice' : 1, 'users' : users}
					return render(request, 'admin_manage/users.html', context)
				else:
					year = data['year']
					month = data['month']
					start_date = datetime.date(year,month,day)
					end_date = datetime.date(year,month,day)
					users = User.objects.filter(create_time__range=(start_date, end_date))
					context = {'choice' : 1, 'users' : users}
					return render(request, 'admin_manage/users.html', context)
def filter_by_event(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		number = data['id']
		users = []
		if number == 0:
			now = datetime.datetime.now()
			seven_days_ago = now + datetime.timedelta(days = -7)
			users_ = User.objects.all()
			for user in users_:
				events = user.event_set.filter(start_time__range=(seven_days_ago, now))
				if len(events) == 0:
					users.append(user)
		elif number == 1:
			now = datetime.datetime.now()
			seven_days_ago = now + datetime.timedelta(days = -7)
			users_ = User.objects.all()
			for user in users_:
				events = user.event_set.filter(start_time__range=(seven_days_ago, now))
				if len(events) == 1:
					users.append(user)
		elif number == 2:
			now = datetime.datetime.now()
			seven_days_ago = now + datetime.timedelta(days = -7)
			users_ = User.objects.all()
			for user in users_:
				events = user.event_set.filter(start_time__range=(seven_days_ago, now))
				if len(events) >= 2 and len(events) <= 5:
					users.append(user)
		elif number == 3:
			now = datetime.datetime.now()
			seven_days_ago = now + datetime.timedelta(days = -7)
			users_ = User.objects.all()
			for user in users_:
				events = user.event_set.filter(start_time__range=(seven_days_ago, now))
				if len(events) >= 6 and len(events) <= 10:
					users.append(user)
		elif number == 4:
			now = datetime.datetime.now()
			seven_days_ago = now + datetime.timedelta(days = -7)
			users_ = User.objects.all()
			for user in users_:
				events = user.event_set.filter(start_time__range=(seven_days_ago, now))
				if len(events) >= 10 and len(events) <= 20:
					users.append(user)
		else:
			now = datetime.datetime.now()
			seven_days_ago = now + datetime.timedelta(days = -7)
			users_ = User.objects.all()
			for user in users_:
				events = user.event_set.filter(start_time__range=(seven_days_ago, now))
				if len(events) >20:
					users.append(user)
		context = {'choice' : 1, 'users' : users}
		return render(request, 'admin_manage/users.html', context)
def order_by_letter(request):
	if request.method == 'POST':
		users = User.objects.order_by("name")
		context = {'choice' : 1, 'users' : users}
		return render(request, 'admin_manage/users.html', context)
def order_by_number(request):
	if request.method == 'POST':
		users = User.objects.order_by("id")
		context = {'choice' : 1, 'users' : users}
		return render(request, 'admin_manage/users.html', context)
def order_by_time(request):
	if request.method == 'POST':
		users = User.objects.order_by("create_time")
		context = {'choice' : 1, 'users' : users}
		return render(request, 'admin_manage/users.html', context)
def count(request):
	if 'admin_ip' in request.session:
		ip = request.session['admin_ip']
		if 'admin_id' in request.session:
			admin = Admin.objects.get(id=request.session['admin_id'])
			if admin.admin_ip != ip:
				del request.session['admin_ip']
				return HttpResponseRedirect('/admin_manage/login')
			else:
				context = {'choice' : 3, 'a' : "abc", 'admin' : admin}
				return render(request, 'admin_manage/count.html', context)
		else:
			return HttpResponseRedirect('/admin_manage/login')
	else:
		return HttpResponseRedirect('/admin_manage/login')
def check_event(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		event = RecommendEvent.objects.get(id=data['id'])
		event.check_state = '1'
		event.check_time = datetime.datetime.now()
		admin = Admin.objects.get(id=request.session['admin_id'])
		event.check_admin = admin
		event.check_admin_id = admin.id
		event.save()
		event.admin_set.check_num += 1
		code = JsonResponse({'code' : 1})
		return(code)
def publish_event(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		event = RecommendEvent.objects.get(id=data['id'])
		event.publish_state = '1'
		event.publish_time = datetime.datetime.now()
		admin = Admin.objects.get(id=request.session['admin_id'])
		event.publish_admin_id = admin.id
		event.save()
		event.admin_set.publish_num += 1
		code = JsonResponse({'code' : 1})
		return(code)
def add_event(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		event = RecommendEvent(author_id=request.session['admin_id'], title=data['title'], content=data['content'], address=data['address'], start_time=data['start_time'], end_time=data['end_time'], latitude=200, longitude=200, pic_url=data['pic_url'], category_id=data['category'])
		event.save()
		code = JsonResponse({'code' : 1})
		return(code)
def recommends_search(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		if data['search_term'] == '1':
			recommends = RecommendEvent.objects.filter(address__contains=data['search_detail'])
			admin = Admin.objects.get(id=request.session['admin_id'])
			context = {'choice' : 2, 'recommends' : recommends, 'admin' : admin}
			return render(request, 'admin_manage/recommends.html', context)
		elif data['search_term'] == '2':
			recommends = RecommendEvent.objects.filter(title__contains=data['search_detail'])
			admin = Admin.objects.get(id=request.session['admin_id'])
			context = {'choice' : 2, 'recommends' : recommends, 'admin' : admin}
			return render(request, 'admin_manage/recommends.html', context)
		elif data['search_term'] == '3':
			recommends = RecommendEvent.objects.filter(source__name__contains=data['search_detail'])
			admin = Admin.objects.get(id=request.session['admin_id'])
			context = {'choice' : 2, 'recommends' : recommends, 'admin' : admin}
			return render(request, 'admin_manage/recommends.html', context)
		elif data['search_term'] == '4':
			recommends = RecommendEvent.objects.filter(category__name__contains=data['search_detail'])
			admin = Admin.objects.get(id=request.session['admin_id'])
			context = {'choice' : 2, 'recommends' : recommends, 'admin' : admin}
			return render(request, 'admin_manage/recommends.html', context)