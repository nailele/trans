
---

# Translation Service

## Overview

The Translation Service is a microservice that provides a JSON API for working with word definitions and translations obtained from Google Translate. It supports storing translations in a Redis database to reduce the number of requests to Google Translate.

## Features

- Retrieve details about a given word, including definitions, synonyms, translations, and examples.
- Get a list of words stored in the database with pagination, sorting, and filtering capabilities.
- Delete a word from the database.

## Technologies Used

- Python 3.11
- FastAPI 0.54
- Redis
- Docker
- Poetry for dependency management

## Project Structure

```
translation_service/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── services.py
│   └── utils.py
├── .env
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── poetry.lock
└── pyproject.toml
```

## Setup Instructions

### Prerequisites

- Docker
- Docker Compose
- Python 3.11

### Step-by-Step Guide

1. **Clone the repository**

   ```sh
   git clone <repository_url>
   cd translation_service
   ```

2. **Create and configure the environment variables**

   Copy `.env.example` to `.env` and adjust the variables as needed.

   ```sh
   cp .env.example .env
   ```

3. **Install dependencies using Poetry**

   ```sh
   poetry install
   ```

4. **Run the application with Docker Compose**

   ```uvicorn app.main:app
   ```

5. **Access the API**

   The API will be available at `http://localhost:8000`.

## API Endpoints

### Get Word Details

- **URL:** `/word/{word}`
- **Method:** `GET`
- **Description:** Retrieve translation details for a given word.
- **Response:**
  ```json
  {
    "word": "example",
    "definitions": ["пример", "образец"],
    "synonyms": ["образец", "пример"],
    "translations": ["пример"],
    "examples": ["This is an example."]
  }
  ```

### Get List of Words

- **URL:** `/words`
- **Method:** `GET`
- **Description:** Get a list of translated words with pagination.
- **Response:**
  ```json
  [
    {
      "word": "example",
      "definitions": ["пример", "образец"],
      "synonyms": ["образец", "пример"],
      "translations": ["пример"],
      "examples": ["This is an example."]
    },
    ...
  ]
  ```

### Delete Word

- **URL:** `/word/{word}`
- **Method:** `DELETE`
- **Description:** Delete a translation entry from the database.
- **Response:**
  ```json
  {
    "detail": "Word deleted"
  }
  ```

## Development

### Run Tests

To run the tests, use the following command:

```sh
poetry run pytest
```

## Challenges and Solutions

### Tool Selection

- **Challenge:** Finding a reliable tool for interacting with Google Translate.
- **Solution:** After evaluating multiple options, `googletrans` was chosen despite its deprecated status due to its suitability for our needs.

### Dependency Conflicts

- **Challenge:** `googletrans` required an older version of `httpx` (0.13), which conflicted with the latest FastAPI dependencies.
- **Solution:** Downgraded FastAPI to version 0.54 to maintain compatibility with `httpx 0.13`.

### Dynamic Response Parsing

- **Challenge:** Parsing the dynamic structure of the response from Google Translate.
- **Solution:** Implemented robust parsing logic to extract and store synonyms, definitions, and pronunciations.

## Future Improvements

- **Tool Update:** Explore updated libraries or APIs for more stable and maintained solutions.
- **Error Handling:** Enhance error handling for edge cases in API responses and database interactions.
- **Scalability:** Optimize the application for scalability and performance under higher loads.

## Acknowledgements

Thank you for the opportunity to work on this project. I look forward to any feedback or further discussion regarding the project.

