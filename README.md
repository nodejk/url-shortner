# Finn URL Shortner Service 🚗✨

## Design Choices 🤓

1. I have used hash maps (aka dictionary in Python) in order to shorten the url.

2. It maps the url to random alphabets (caps and lower case, in total 52 characters) and digits (0-9) and uses 6 places to encode url. This gives us enough space to encode 56.8 Billion urls (62^6).

3. It uses two hash maps, one used to store mappings from encoded to decoded url and second one from decoded url to encoded url. First one is used to decode url from encoded urls. Second one is used to check if encoded

4. To realize this algo in production, we can think of these hash map as DynamoDB, we have to store these mappings in 2 DynamoDBs.

5. Any additional services related to Finn can be added under Finn folder (say, a new file compressor) and any external service can be added in a new directory under app as External.

6. Request and Response validations are supported out of the box using pydantic and are automatically documented at http://localhost:8080/docs. If a wrong request is given by the user, it will return validation errors at individual fields. In this case, ShortLink is the schema model that I have created for validating and returning the encoded/decoded response.

7. Further api can be versioned in [AppSettings.py](/app/Core/Settings/AppSettings.py) setting environment variable "VERSION" using git tags.

8. I have used FastApi instead of Flask as it generates automated documentation for the api. Addtionally, it allows the user to try the api using a web interface.

---

## Running the Application 🖥️

1. Make sure docker is installed and running on your system.
2. Go to the root directory in CLI, and run the following command:

    ```bash
    docker-compose up --build
    ```

3. After running the command, it will run the application in Dev Mode. Visit page (http://localhost:8080/docs) on your browser to try out the api.

**Note**: This application runs on DEV mode. to run the application in production, change the environment variable to **PROD** in the .env file.

---

## Workflow ⚒️

Check out [link](https://app.tango.us/app/workflow/Workflow-with-Finn-Url-Shortner-Api-145be00fef6a43c8b015892b0593d9d3) to know about the workflow of the api.

---

## Running Tests 🧪

1. Firstly, login to the docker container using the following command:

    ```bash
    docker exec -it default-python-vvndpa-app-1 /bin/bash
    ```

2. After logging in the container, run the following commands to run all the tests:

    ```bash
    make test
    ```

---

## Additional features for Devs 💻✨

1. To automatically check the formatting of your code after developing, run following command (it also checks for unused imports and variables as well):

    ```bash
    make check-format
    ```

2. To remove all unused imports and variables, run the following command:

    ```bash
    make format
    ```

3. To remove all the py/mypy cache, run the following command:

    ```bash
    make clean
    ```

4. For type checking, run the following command:

    ```bash
    make mypy
    ```

5. To run type checking and tests altogether, run the following command:

    ```bash
    make all
    ```

---

## Note 🗒️

mypy apparently has some issues while working with some pydantic attributes (HttpUrl) and string, hence they are ignored in mypy type checking.

---

## Naming Conventions 📝

| Type | Naming Convention |
| :---:   | :---: |
| Class Modules | Pascal Case |
| Method Modules | Kebab Case |
| Variable/Functions | Kebab Case |
| Application Directories | Pascal Case |

---

## Folder Structure 📂

```bash
├── app
│   ├── Core
│   │   └── Settings
│   ├── Enums
│   ├── Errors
│   ├── Finn
│   │   └── ShortLink
│   │       ├── Controllers
│   │       └── Models
│   ├── Middleware
│   ├── Routes
│   └── Utils
├── scripts
└── tests
    ├── E2E
    └── Unit
```
