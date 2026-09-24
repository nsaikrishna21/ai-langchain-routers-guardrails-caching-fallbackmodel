# README

## Create Virtual Environment
To create a virtual environment in Windows, open your terminal and run the following command:
```bash
python -m venv venv
```
This will create a new virtual environment named `venv` in your current directory.

## Activate Virtual Environment
To activate the virtual environment, run the following command:
```bash
venv\Scripts\activate
```
You should now see the name of the virtual environment printed on your terminal, indicating that it is active.

## Install FastAPI and Uvicorn
To install FastAPI and Uvicorn, run the following command:
```bash
pip install fastapi uvicorn
```
This will install the necessary packages for your FastAPI application.

## Create FastAPI App
To create a new FastAPI application, create a new file named `main.py` and add the following code:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
```
This code creates a new FastAPI application with a single endpoint at the root URL.

## Run FastAPI App with Uvicorn
To run the FastAPI application with Uvicorn, run the following command:
```bash
uvicorn api.main:app --reload
```
This will start the development server and make your application available at `http://localhost:8000`. You can now access your application by visiting this URL in your web browser.

## Access Documentation
To access the documentation for your FastAPI application, visit `http://localhost:8000/docs` in your web browser.

## Commits

### Commit 1: Initial Commit
This commit initializes the repository and sets up the basic structure for the project. The following files were created:
- `.env.example`: This file contains environment variables for the project, such as database connections and API keys.
- `.gitignore`: This file specifies files and directories that should be ignored by Git, such as node_modules and build directories.
- `app1.py`, `app2.py`, `app3.py`, `app4.py`: These files contain the initial code for the project, including the main application logic and routes.
- `evaluation/prompt_evaluation_report.csv` and `evaluation/rewrite_test_cases.csv`: These files contain data for evaluating prompts and rewriting test cases, respectively.
- `long_text.txt`: This file contains a long piece of text used for testing and demonstration purposes.
- `models/summary.py`: This file contains a model for summarizing text, including functions for extracting keywords and generating summaries.
- `prompts/extract_keywords.txt`, `prompts/extract_keywords_v2.txt`, `prompts/headline.txt`, `prompts/headline_v2.txt`, `prompts/rewrite_few_shot.txt`, `prompts/rewrite_zero_shot.txt`, `prompts/structured_summary.txt`, `prompts/summarize_v1.txt`, `prompts/summarize_v2.txt`, `prompts/summarize_v3.txt`: These files contain prompts for extracting keywords, creating headlines, rewriting text, and summarizing text, respectively.
- `requirements.txt`: This file contains dependencies for the project, including libraries and frameworks used in the code.
- `services/content_pipeline.py` and `services/json_service.py`: These files contain code for the content pipeline and JSON service, respectively, which are used for processing and generating content.
- `single_prompt.py`: This file contains a single prompt for testing and demonstration purposes.

### Commit 2: Initial Commit - No LLM Invocation
This commit adds the initial code for the project, but does not include any LLM invocation. The following files were created:
- `api/main.py`: This file contains the main API logic, including routes and handlers for the application.
- `models/task.py`: This file contains a model for tasks, including functions for creating, reading, updating, and deleting tasks.
- `router.py`: This file contains the router for the application, which maps URLs to handlers and routes.
- `services/prompt_loader.py`: This file contains code for loading prompts, including functions for reading and parsing prompt files.
- `requirements.txt`: This file contains dependencies for the project, including libraries and frameworks used in the code.

### Commit 3: LLM Invocation & Retuning Response
This commit adds the LLM invocation and response handling code to the project. The following files were created:
- `api/main2.py`: This file contains the updated API logic, including routes and handlers for the application.
- `models/task2.py`: This file contains the updated task model, including functions for creating, reading, updating, and deleting tasks.
- `router2.py`: This file contains the updated router for the application, which maps URLs to handlers and routes.
- `services/task_service.py`: This file contains code for the task service, including functions for creating, reading, updating, and deleting tasks.

### Commit 4: Multi LLM Invocation
This commit adds the multi-LLM invocation feature to the project, allowing for multiple LLMs to be invoked simultaneously. The following files were created:
- `api/main3.py`: This file contains the updated API logic, including routes and handlers for the application.
- `config.py`: This file contains configuration for the project, including settings for the LLMs and other components.
- `router3.py`: This file contains the updated router for the application, which maps URLs to handlers and routes.
- `services/llm_factory.py`: This file contains code for the LLM factory, which creates and manages LLM instances.
- `services/task_service2.py`: This file contains the updated task service, including functions for creating, reading, updating, and deleting tasks.

### Commit 5: Multi LLM Invocation with Model Abstraction Layer
This commit adds a model abstraction layer to the multi-LLM invocation feature, improving the scalability and maintainability of the code. The following files were created:
- `api/main4.py`: This file contains the updated API logic, including routes and handlers for the application.
- `router4.py`: This file contains the updated router for the application, which maps URLs to handlers and routes.
- `services/model_selector.py`: This file contains code for the model selector, which selects the appropriate LLM model for a given task.
- `services/task_service3.py`: This file contains the updated task service, including functions for creating, reading, updating, and deleting tasks.

### Commit 6: Adding i/p o/p Guardrails
This commit adds input/output guardrails to the project, ensuring that the inputs and outputs are validated and sanitized. The following files were created:
- `api/main5.py`: This file contains the updated API logic, including routes and handlers for the application.
- `models/task3.py`: This file contains the updated task model, including functions for creating, reading, updating, and deleting tasks.
- `prompts/headline_v3.txt`, `prompts/keypoints.txt`, `prompts/rewrite_v3.txt`, `prompts/summarize_v4.txt`: These files contain prompts for creating headlines, extracting keywords, rewriting text, and summarizing text, respectively.
- `services/guardrails.py`: This file contains code for the guardrails, which validate and sanitize inputs and outputs.
- `services/task_service4.py`: This file contains the updated task service, including functions for creating, reading, updating, and deleting tasks.

### Commit 7: Adding pydantic validation on each task
This commit adds pydantic validation to each task in the project, ensuring that the data is validated and consistent. The following files were created:
- `api/main6.py`: This file contains the updated API logic, including routes and handlers for the application.
- `models/task4.py`: This file contains the updated task model, including functions for creating, reading, updating, and deleting tasks.
- `prompts/headline_v4.txt`, `prompts/keypoints_v2.txt`, `prompts/rewrite_v4.txt`, `prompts/summarize_v5.txt`: These files contain prompts for creating headlines, extracting keywords, rewriting text, and summarizing text, respectively.
- `router5.py`: This file contains the updated router for the application, which maps URLs to handlers and routes.
- `services/output_validator.py`: This file contains code for the output validator, which validates the output of each task.
- `services/task_service5.py`: This file contains the updated task service, including functions for creating, reading, updating, and deleting tasks.

### Commit 8: Implement cache layer
This commit adds a cache layer to the project, improving the performance and reducing the load on the system. The following files were created:
- `api/main7.py`: This file contains the updated API logic, including routes and handlers for the application.
- `models/task5.py`: This file contains the updated task model, including functions for creating, reading, updating, and deleting tasks.
- `services/cache.py`: This file contains code for the cache layer, which stores and retrieves cached data.
- `services/task_service6.py`: This file contains the updated task service, including functions for creating, reading, updating, and deleting tasks.

### Commit 9: Added Fallback model & Retry mechanism
This commit adds a fallback model and retry mechanism to the project, ensuring that the system can recover from failures and exceptions. The following files were created:
- `.env.example`: This file contains environment variables for the project, including settings for the fallback model and retry mechanism.
- `api/main8.py`: This file contains the updated API logic, including routes and handlers for the application.
- `config2.py`: This file contains configuration for the project, including settings for the fallback model and retry mechanism.
- `models/task6.py`: This file contains the updated task model, including functions for creating, reading, updating, and deleting tasks.
- `router6.py`: This file contains the updated router for the application, which maps URLs to handlers and routes.
- `services/llm_factory2.py`: This file contains code for the LLM factory, which creates and manages LLM instances.
- `services/model_selector2.py`: This file contains code for the model selector, which selects the appropriate LLM model for a given task.
- `services/retry_handler.py`: This file contains code for the retry handler, which handles retries and fallbacks for failed tasks.
- `services/task_service7.py`: This file contains the updated task service, including functions for creating, reading, updating, and deleting tasks.
