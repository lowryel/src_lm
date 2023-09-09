### LM ESTATES MANAGER

- LM Estate Manager is a multi-tenant real estate web application where you can list your property for sale or rent.
- We have buyers who are ready to patronize your properties.
- You have equal advantage at selling or renting a property.

----------------------------------
- This website is made with you in mind. You don't have to create an account to buy or rent a property
- However, to sell a property, you need to create an account as a user since you have to list your property.
- You can speak to any agency who will assign you an agent to assist you in finding your next property.

- We are working on getting an agent to sale your property for you. This requires a lot of trust hence why it is        taking time.
- We want to make it secure and trustworthy to deal on this platform

- favicon - the image that appears on the browser tab `<link rel="icon" href="{% static './img/dream-house.jpg' %}" type="png">`


- Make a rolling update to your application without any downtime
`kubectl set image deployments/nginx nginx=nginx:v0.21`
Also, rollback to the previous app version with this command
`kubectl rollout undo deployments/nginx`

- Command to start gunicorn config
`gunicorn -c conf/gunicorn_config.py lm.asgi`

hint: 
hint:   git config pull.rebase false  # merge
hint:   git config pull.rebase true   # rebase
hint:   git config pull.ff only       # fast-forward only
hint: 

* "The Django admin /django/contrib/admin/templates/ directory contains two template folders:
admin and registration. Copy them to a project directory that’s part of a DIRS folder of the TEMPLATES/DIRS
variable in settings.py."



