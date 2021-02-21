import requests
import json
import urllib


max_results = 500 
hapikey = "2b0cbf32-bc72-40b6-8953-c40aeebeec07"
count = 20
contact_list = []
property_list = []
get_all_contacts_url = "https://api.hubapi.com/contacts/v1/lists/all/contacts/all?"
parameter_dict = {'hapikey': hapikey, 'count': count}
headers = {}

# Paginate your request using offset
has_more = True
while has_more:
	parameters = urllib.urlencode(parameter_dict)
	get_url = get_all_contacts_url + parameters
	r = requests.get(url= get_url, headers = headers)
	response_dict = json.loads(r.text)
	has_more = response_dict['has-more']
	contact_list.extend(response_dict['contacts'])
	parameter_dict['vidOffset']= response_dict['vid-offset']
	if len(contact_list) >= max_results: # Exit pagination, based on whatever value you've set your max results variable to. 
		print('maximum number of results exceeded')
		break
print('loop finished')

list_length = len(contact_list) 

print("You've succesfully parsed through {} contact records and added them to a list".format(list_length))