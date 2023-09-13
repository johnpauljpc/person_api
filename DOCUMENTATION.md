# Person API Documentation (HNGx stage II task)

## Standard Request and Response Formats

### List and Create Persons (`/api/`)

**Create** Request Format (POST)
- Endpoint: `/api/`
- Method: POST
- Content-Type: application/json

**Request Body:**

```json
{
  "name": "John Paul"
}

```

**Response Format (GET)**
- Endpoint: `/api/`
- Method: GET
- Content-Type: application/json

<b>Response Body (List of Persons):</b>

```
[
  {
    "id": 1,
    "name": "John Paul"
  },
  {
    "id": 2,
    "name": "Mikel Essien"
  }
]

```

**Retrieve, Update, and Delete a Person (`/api/<int:pk>/`)**
Response Format (GET)
- Endpoint: **/api/<code><</code>int:pk<code>></code>/**
- Method: GET
- Content-Type: application/json


Response Body for **retrieving** a Single Person:
```json
    {
      "id": 1,
      "name": "John Paul"
    }
```


Request Format for **updating** a single person (PUT)
- Endpoint: **/api/<code><</code>int:pk<code>></code>/**
- Method: PUT 
- Content-Type: application/json 


<b>Request Body:</b>
```json
  {
    "name": "Updated Name"
  }
```

Request Format for **deleting** a single person (PUT)
- Endpoint: **/api/<code><</code>int:pk<code>></code>/**
- Method: DELETE
- Content-Type: application/json


<b>Request Body:</b>
```
{}
```


<h2>Sample Usage</h2>
<h3>List all persons (GET)</h3>
<b>Request:</b>

```
curl http://localhost:8000/api/
```
<b>Response:</b>
```
[
  {
    "id": 1,
    "name": "John Paul"
  },
  {
    "id": 2,
    "name": "Mike Essien"
  }
]
```

<h3>Create a new person (POST)</h3>
<b>Request:</b>

```
curl -X POST http://localhost:8000/api/ -d "name=Johnson"
```
<b>Response:</b>

```
{
  "id": 3,
  "name": "Johnson"
}
```

<h3>Retrieve a person by ID (GET)</h3>
<b>Request:</b>

```
curl http://localhost:8000/api/1/
```

<b>Response:</b>

```
{
  "id": 1,
  "name": "John Paul"
}
```

<h3>Update a person by ID (PUT)</h3>
<b>Request:</b>

```
curl -X PUT http://localhost:8000/api/1/ -d "Johnpaul (Updated)"
```

<b>Response:</b>

```
{
  "id": 1,
  "name": "Johnpaul (Updated)"
}
```

<h3>Delete a person by ID (DELETE)</h3>
<b>Request:</b>

```
curl -X DELETE http://localhost:8000/api/1/
```

<b>Response:</b>

```
{} #empty upon sucessful deletion
```

You can access the interactive documentation at `http://localhost:8000/swagger/` to play around with the endpionts.<br>

<h2> Known Limitations and Assumptions </h2>
<li> This API assumes that each person's name is unique.</li>
<li> The API does not implement authentication or authorization for simplicity. In a production environment, you should add proper security measures.</li>

<h2> Setting Up and Deploying the API </h2>

<h4> Local Setup </h4>
1. clone repository

```bash
git clone https://github.com/johnpauljpc/person_api.git
```

```
cd person_api
```

2. Create a virtual environment:
```
python -m venv venv 
```
```
venv\Scripts\activate
```

3. Install project dependencies:
```
pip install -r requirements.txt
```
4. Migrate the database:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
5. Run the API:
```
python manage.py runserver
```
5. Access the API at `http://localhost:8000/`.

## Deployment
<li>Deploy the Django project to a production server (e.g., using a web server like Apache or Nginx).</li>
<li>Set up a production-ready database (e.g., PostgreSQL/MySQL).</li>
<li>Configure environment variables for production settings (e.g., DEBUG, SECRET_KEY, DATABASE_URL).</li>
<li>Ensure proper security measures, including authentication and authorization, are implemented for your API.</li>
<li>Monitor and maintain your deployed API as needed for your application's requirements.</li>
