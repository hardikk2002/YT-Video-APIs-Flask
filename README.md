This app simply fetches videos using Youtube APIs based on the keyword enter in the search field.

Tech stack/frameworks: 
  - Python  
  - Flask
  - Bootstrap


### Live demo: [here](https://yt-videos-flask.herokuapp.com/)

<br>

## Setup project in Local:
---
1. Clone
    ```bash
    git clone https://github.com/hardikk2002/YT-Video-APIs-Flask.git
    ```
2. Cd to the directory
    ```bash
    cd YT-Video-APIs-Flask/
    ```
3. Copy `.env.sample` file and create `.env` file

    ```bash
    cp .env.sample .env
    ```
4. Open current folder in Code Editor (vs code)
    ```bash
    code .
    ```
5. Edit `.env` file with your credentials

<br>






## Run on local machine:

---



  1. Create a `virtual environment` and activate it. This is where dependencies for the project will be installed.

      ```bash
      virtualenv venv
      ```
      ```bash
      source ./venv/bin/activate
      ```      
      > Note: **If the virtualenv command fails**, you need to install it globally with pip.

      ```
      pip install virtualenv
      ```

  2. After activating the project virtual environment, `install project dependencies`.

      ```
      pip install -r requirements.txt
      ```
  3. Run the server, and visit the site at `http://127.0.0.1:5000/`.

      ```
      python app.py
      ```