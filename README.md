# Daily Cloud Predict API

## Brief Description

The Daily Cloud Predict API provides an API for predicting whether a journal has been diagnosed with depression or not, from Natural Language Processing (NLP) models.

## Table of Contents



## Tech Stack

1. [Python](https://www.python.org/)
2. [Flask](https://flask.palletsprojects.com/en/2.3.x/)
3. [Tensorflow](https://www.tensorflow.org/)
4. [Docker](https://www.docker.com/)
5. [Google Cloud Run](https://cloud.google.com/run)

## Tools

1. [Visual Studio Code](https://code.visualstudio.com/)
2. [Postman](https://www.postman.com/)

## Todos

- [x] Initialize Project
- [x] Install Dependencies
- [x] Create Server
- [x] Predict API
  - [x] Routes
  - [x] Predict Function
- [x] Deploy Development API
- [x] Testing and Debugging
- [x] Deploy Production API
- [x] Create Documentation

## Installation

### Run on Local Environment

This project using [Python v3.11](https://www.python.org/) and venv

1. Clone this repository

   ```bash
   git clone https://github.com/daily-cloud/daily-cloud-predict-api.git

   cd daily-cloud-predict-api
   ```

2. Create virtual environment

   ```bash
   python3 -m venv .venv
   ```

3. Activate the environment

    Linux

   ```bash
   . .venv/bin/activate
   ```
   
   or Windows
   ```powershell
   .venv\Scripts\activate
   ```

4. Run the Server
    ```bash
    # development
    flask --app main run --debug

    # with gunicorn 
    gunicorn --workers 1 --threads 8 --timeout 0 main:app
    ```

### Run on Docker

Make sure you have Docker installed on your local computer

1. Clone this repository

   ```bash
   git clone https://github.com/daily-cloud/daily-cloud-predict-api.git
   cd daily-cloud-predict-api
   ```

2. Build docker image

   ```bash
   docker build -t daily-cloud-predict-api .
   ```

3. Run the image
   ```bash
   docker run -p 8080:8080 --name daily-cloud-predict-api-app daily-cloud-predict-api
   ```

## Author

- [C141DSX0721 – Fahrul Zaman – Bale Bandung University](https://www.linkedin.com/in/fhrlzmn/)
- [C032DKY4321 – Maya Septiani Br Simbolon – Harapan Bangsa Institute of Technology](https://www.linkedin.com/in/mayaseptianibrsimbolon/)

## Thank You

- Bangkit Academy led by Google, GoTo, & Traveloka
- Daily Cloud Capstone Team

## [back to top](#daily-cloud-predict-api)
