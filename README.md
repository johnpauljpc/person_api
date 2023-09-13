# Person API (HNGx stage II task)
## Introduction
**This is a simple REST API capable of CRUD operations on a resource, say, a "person". In other words, This REST API is capable of doing the following:**
- Adding a new person
- Fetching details of a person
- Modifying details of an existing person 
- Removing a person


## Project Setup
**1. Ensure you have Python and Django installed on your system.**

```
   python --version
```
```
   django-admin --version
```

**2. Clone this repository to your local machine:**
```
      git clone https://github.com/johnpauljpc/person_api.git
```    
```
        cd person_api
```
       
**3. Create a virtual environment (optional but recommended):**

```
   python mkvirtualenv venv
```
```
  workon venv  # to activate it any other time
```
**4. Install project dependencies:** 

```
 pip install -r requirements.txt
```
**5. Migrate the database:**
        
```
python manage.py migrate
```


## Run the API

To start the Django development server and run the API, run the command below:

```bash
python manage.py runserver
```

The API will be accessible at `http://localhost:8000/`.


## API Endpoints

- List and Create Persons:
  - **URL**: `/api/`
  - **HTTP Methods**: GET (list), POST (create)
  - **Description**: Use this endpoint to list all persons and create new persons.

- Retrieve, Update, and Delete a Person:
  - **URL**: `/api/<int:pk>/`
  - **HTTP Methods**: GET (retrieve), PUT (update), DELETE (delete)
  - **Description**: Use this endpoint to retrieve, update, or delete a specific person by their primary key (pk).




## Examples of Requests

**List all persons (GET)**

```bash
curl http://localhost:8000/api/
```
**Create a new person (POST)**

```
curl -X POST http://localhost:8000/api/ -d "name=John Paul"
```

**Retrieve a person by ID (GET)**


```
curl http://localhost:8000/api/1/
```

**Update a person by ID (PUT)**
```
curl -X PUT http://localhost:8000/api/1/ -d "name=Updated Name"
```

**Delete a person by ID (DELETE)**

```
curl -X DELETE http://localhost:8000/api/1/
```


## API Documentation
You can access this &#9758; `http://localhost:8000/swagger/` for interactive documentation.<br>

## Additional Notes

- Ensure that you have the necessary permissions to access the API endpoints.
- Secure your API in production using proper authentication and authorization mechanisms.
- Customize the Django settings in `settings.py` as per your project requirements.



