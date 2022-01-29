# Card Board App

This App is distributed majorly in four parts:

* Front-end
* Back-end
* Database
* Dockerizing

1) Back-end: 
- Let's start with creating our backend.
- We would use FastAPI as our backend framework.
- Let's start with configuring our env variables.

 ![Alt text](screenshots/os-config.PNG)

- Now let's create function to get db sessions.

 ![Alt text](screenshots/db-session.PNG)
- Next, we need to add models and schemas.

 ![Alt text](screenshots/model.PNG)

 ![Alt text](screenshots/schema.PNG)
- Let's add router to our app now.

 ![Alt text](screenshots/router.PNG)
- Ok,so as we've everything set, let's run the backend with : 
```sh
  uvicorn main:app --reload --port 6969
  ```
- If we now open ```localhost:6969/docs```, we would see documentation of our backend. 

 ![Alt text](screenshots/docs.PNG)

2) Front-end :
- React.js is used for building the front end side.
- Let's start with creating a project with command : 
 ```sh
  npx create-react-app front-end
  ```
- We are going to need following :
    * Home Page, where our cards and placeholders would be render
    * Cards, which would be movable.
    * Placeholders, where cards would be stored/located.
    * API service, to fetch and update data.
    * Modal component, to overlay image on screen when clicked.
    * Docker file, to dockerize the app.

- Our home page would be rendered in App component,that is App.js.

- Cards and Placeholders are inserted and return in App.js only.

- This is how our Home page would look in beginning (With no Cards).

  ![Alt text](screenshots/init-homepage.PNG)

- Now let's hit some API's to fetch our cards data

 ![Alt text](screenshots/add-cards.PNG)

- We're going to write api-service which would contain all api-related functionality.

- Now as cards are loaded, our home page would look like this.

 ![Alt text](screenshots/after-homepage.PNG)

- Now let's add some cardswap logic.

 ![Alt text](screenshots/on-drag-end.PNG)

 ![Alt text](screenshots/swap-cards.PNG)

- As almost everything is done, Let's add Image Modal to display image as overlay.

 ![Alt text](screenshots/image-modal.PNG)

- Okay ! Our Front-end is ready too.

3) Let's dockerize our app.

- Let's create Dockerfile for our frontend and backend.
- For Frontend :

 ![Alt text](screenshots/docker-frontend.PNG)

- For Backend : 

 ![Alt text](screenshots/docker-backend.PNG)

- Let's now create docker-compose.yml to initiate our containers : 

 ![Alt text](screenshots/docker-compose.PNG)


Run this command to run the App 

```sh
  docker-compose up
  ```