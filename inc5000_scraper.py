from requests import get
 
# scrape the Inc 5000 list and return a dictionary with values for every company
def inc5000_scraper():
	# dictionary of every company
	# the key for each company is its id (determined internally by Inc)
	company_dictionary = {}
	# Fuhu is first on the Inc 5000 list and has id 22890
	current_company_id = 22890
	 
	# loop through the Inc 5000
	# company number 5000 has no next_id value, thus terminating the loop
	while current_company_id:
		# json data for one specific company converted to temporary dictionary current_company
		current_company = get('http://www.inc.com/rest/inc5000company/' + str(current_company_id) + '/full_list').json()
		# company data added to company_dictionary
		company_dictionary[current_company['data']['id']] = current_company['data']
		# change current_company_id to next_id (current_company value) and iterate loop
		current_company_id = current_company['data']['next_id']
	 
	return company_dictionary