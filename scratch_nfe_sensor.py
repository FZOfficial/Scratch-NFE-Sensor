import requests
import bs4
def get_projects(user):
	number = 1
	projects = []
	while True:
		request = requests.get('https://scratch.mit.edu/users/{}/projects/?page={}'.format(user, number))
		if request.status_code == 404: break
		else:
			page = bs4.BeautifulSoup(request.text, 'html.parser')
			for p in page.select('li.project span.title a'):
				projects.append(int(p['href'].split('/')[2]))
		number = number + 1
	return projects
for project in get_projects('Zro716'):
	page = bs4.BeautifulSoup(requests.get('https://scratch.mit.edu/projects/{}/'.format(project)).text)
	nfe = ('<meta content="noindex" name="robots"/>' in [str(m) for m in page.find_all('meta')])
	if nfe: print page.title.get_text().split('on Scratch')[0]
