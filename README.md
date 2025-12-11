# fast-api-user-demo

## Setup & Installation

1.  **Clone the repository** (if you haven't already):
    ```bash
    git clone <repository_url>
    cd UserAPI
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

To start the server, run the following command from the root directory:

```bash
uvicorn main:app --reload --app-dir Application
```

The application will be available at `http://127.0.0.1:8000`.

## Using the API

You can interact with the API using the automatic query documentation provided by Swagger UI:

1.  Open your browser and navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
2.  You will see a list of available endpoints.
3.  Click on an endpoint to expand it, then click "Try it out" to send requests.

## Stopping the Application

To stop the running server, simply press `Ctrl+C` in the terminal where the application is running.
