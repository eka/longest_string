`pip install -r requirements.txt`

`./manage.py runserver`


how to test via web: go to http://localhost:8000/

how to test via API: 

* create a file called test.txt with the following content:

```
data=aaa bbb ccc
bbb
ccc
ddd ffff gg bbba
```

* execute curl as:

`curl -H 'Accept: application/json; indent=4' -u admin:admin http://127.0.0.1:8000/api/v1.0/resource/ --data-binary @./test.txt`

