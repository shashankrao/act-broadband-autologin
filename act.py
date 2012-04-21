#!/usr/bin/env python
def main():
    try:
        import time, re, sys, httplib2
    except ImportError:
        print '\xaf [Err] httplib2 Module not found!'
        print '\xaf [Inf] Please install httplib2 module and try again.'
        sys.exit(0)

    print '\xaf [Inf] Logging into ACT Portal...'
    time.sleep(2)

    url     = 'http://portal.acttv.in/newportal/Ajax.php?function=ExecuteLogin&user=<8-Digit-UserID>&pwd=<Your_Password>&remember=true&timestamp=1334843162800'
    headers = { 'Referer': 'http://portal.acttv.in/', \
                'Accept-Language': 'en-in', \
                'Accept-Encoding': 'gzip, deflate', \
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5', \
                'Connection': 'Keep-Alive', \
                'Host': 'portal.acttv.in', \
                'Cookie': 'remember=true; username=<8-Digit-UserID>; password=<Your_Password>; 555c12b67d7c4fc92c79875dd3d3a5b1=664ga1327500ispsuk5c62p4o2' }

    http = httplib2.Http()
    print '\xaf [Inf] Sending authentication request to ACT Gateway...'
    time.sleep(2)

    try:
        response, content = http.request(url, 'GET', headers=headers)
    except httplib2.ServerNotFoundError:
        print '\xaf [Err] Portal.ActTV.in server not reachable.\n\xaf [Inf] Please restart the router and try again.'
        sys.exit(0)

    if re.findall('[0-9]{8}\x20at\x20', content):
        print '\xaf [Inf] Connection unlocked.'
        print '\n\xaf [Chk] Validating if web resources are accessible. Please wait...'
        try:
            url = 'http://www.blackle.com/'
            headers = { 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5', \
                        'Host': 'blackle.com' }

            print '\xaf [Inf] Accessing Host:', url
            response, content = http.request(url, 'GET', headers=headers)
            if int(response['status']) == 200:
                print '\xaf [Inf] Everything looks perfect!'
                print '\xaf [Inf] Connection established successfully!'
                sys.exit(0)
            else:
                print '[Err]  Webpage not accessible.'
        except httplib2.ServerNotFoundError:
            print '\xaf [Err]  External websites inaccessible.'
            print '\xaf [Inf]  Please contact your ISP to troubleshoot the problem.'
            sys.exit(0)
    else:
        print '\xaf [Err]  Sorry, couldn\'t establish connection successfully with the server!'
        print '\xaf [Inf]  Please verify the passed Username//Password. '
        sys.exit(0)

def banner():
    print '''################################################################################
##     Name     :     ActLog                                                  ##
##     Purpose  :     Program to login to ACT Web Gateway                     ##
##     Author   :     Sujit Ghosal (xylux [at] wikisecure [dot] net)          ##
##     Created  :     19-04-2012                                              ##
################################################################################
    '''

if __name__ == '__main__':
    banner() ; main()