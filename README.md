<h1>RISHAT API</h1>

<h2>Preprocessing</h2>

1. Change file default_config.yaml - set your secret and public stripe keys
```YAML
  secret_key: "YOUR_STRIPE_SK"
  public_key: "YOUR_STRIPE_SK"
```

2. Install requirements

3. Execute next commands in the console:

    python manage.py makemigrations
  
    python manage.py migrate
  
    python manage.py runserver

<h2>API VIEW</h2>

<h3>GET /payment/items</h3>

Response text/html - page with list of the created items
 
<h3>GET /payment/newitem</h3>
  
Response text/html - page for creation items what we want to buy
  
<h3>GET /payment/item/{item_id}</h3>

Response text/html - page for buying a choosen item

<h3>GET /payment/buy/{item_id}</h3>

Response text/html - returns a string - id of new stripe session
