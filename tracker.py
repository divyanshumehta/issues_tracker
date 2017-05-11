import requests
import os

main_api =  'https://api.github.com/'
org = input('Enter organization name:')
repo = input('Enter repositoryname:')
url = main_api + 'repos/' + org + '/' + repo + '/issues'
print(url)
response = requests.get(url)
data = response.json()
#print(data[0]['body'])


if not os.path.exists('log.txt'):
	os.system('touch log.txt')

if os.stat('log.txt').st_size == 0 :
	#File is empty
	file = open('log.txt','w')
	for comment in data:
		file.write('Issue Number: '+ '%d'%comment['number'] + '\t')
		file.write('Issue Title:' + comment['title'] + '\t')
		file.write('Labels: ')
		for label in comment['labels']:
			file.write(label['name'] + ',')
		file.write('\tAuthor: ' + comment['user']['login'] + '\t')

		file.write('Created at:' +  '\n')
else:
	# print('file is not empty')
	file = open('log.txt','r+')
	issue = file.readline()
	# print(issue)
	words = issue.split()
	print('Latest Issue Number: ' + words[2])
