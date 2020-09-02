import requests
import sys
from termcolor import colored, cprint 
  
cprint("\nAnonymous Email via anonymouse.org" 'green')
cprint("made by triumphforchaos" 'green')
to = raw_input('to: ')
subject = raw_input('insert subject: ')
message = raw_input('insert message: ')

user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
sess = requests.Session()
email_req = sess.post('http://anonymouse.org/cgi-bin/anon-email.cgi', headers={
	'Host': 'anonymouse.org',
	'User-Agent': user_agent,
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate',
	'Referer': 'http://anonymouse.org/anonemail.html',
        'Connection': 'close',
        'Upgrade-Insecure-Requests':'1',
        'Content-Type':'application/x-www-form-urlencoded'
}, data={
	'to': to,
	'subject': subject,
	'text': message
})

if 'The e-mail has been sent' in email_req.text:
    cprint("[*] EMAIL HAS BEEN SENT" 'red')
    cprint("[*] for more privacy brought to you by triumph for chaos the email will be sent in 12 hours " 'red')
 
