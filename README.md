API

###login
	/login
		return : 0---login failed
				 1---login success	

###register
	/register
		return : 0---server failed
				 1---register success
				 2---register failed, already exists an account with the same username

###results
	/results/evaluateResults
		#get: return : objects of all the evaluateResults
		#post: return : 1---success

###records
	/records/diabeteRecords_get
		#get: return : objects of all the diabeteRecords
	/records/diabeteRecords_add
		#post: return : 1---success
	/records/diabeteRecords_update
		need: {product_id: string/number, value: array}
		#post: return : 1---success
	/records/dietRecords_get
		#get: return : objects of all the dietRecords
	/records/dietRecords_add	
		#post: return : 1---success
	/records/dietRecords_update
		need: {product_id: string/number, value: array}
		#post: return : 1---success
	/records/bmiRecords_get
		#get: return : objects of all the bmiRecords
	/records/bmiRecords_add
		#post: return : 1---success
	/records/bmiRecords_update
		need: {product_id: string/number, value: array}
		#post: return : 1---success

###reminders
	/reminders/medicineReminder_get
		#get: return : objects of all the medicineReminder
	/reminders/medicineReminder_add
		#post: return : 1---success
	/reminders/medicineReminder_update
		need: {product_id: string/number, value: array}
		#post: return : 1---success
	/reminders/medicineReminder_delete
		need: {product_id: string/number, value: array}
		#post: return : 1---success
	/reminders/sportsReminder_get
		#get: return : objects of all the sportsReminder
	/reminders/sportsReminder_add
		#post: return : 1---success
	/reminders/sportsReminder_update
		need: {product_id: string/number, value: array}
		#post: return : 1---success
	/reminders/sportsReminder_delete
		need: {product_id: string/number, value: array}
		#post: return : 1---success
	/reminders/measurementReminder_get
		#get: return : objects of all the measurementReminder
	/reminders/measurementReminder_add
		#post: return : 1---success
	/reminders/measurementReminder_update
		need: {product_id: string/number, value: array}
		#post: return : 1---success
	/reminders/measurementReminder_delete
		need: {product_id: string/number, value: array}
		#post: return : 1---success
