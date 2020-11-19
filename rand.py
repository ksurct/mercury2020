import requests

def main():
    ## we define a request object that is equal to requests.get('API')
    req = requests.get('http://10.132.16.56:8000/sendjson')
    'http://192.168.1.61:8080/api/call'

    ## we then print out the http status_code that was returned on making this request
    ## you should see a successfull '200' code being returned.
    print(req.status_code)

if __name__ == '__main__':
    main()