# Agentic AI System

This project implements a modular Agentic AI system accessible via a FastAPI interface. The agent is designed to plan and execute tasks using a set of tools (file operations, text analysis, etc.) and memory.

## Project Structure

```
.
├── executor.py         # Core agent orchestrator
├── planner.py          # Planning logic
├── memory.py           # Agent memory
├── file_tools.py       # File operations
├── text_tools.py       # Text analysis
├── logger.py           # Logging utility
└── app_api.py          # FastAPI application entry point
```

## Installation

1.  **Clone the repository** (if applicable) or download the source code.
2.  **Install dependencies**:
    ```bash
    pip install fastapi uvicorn
    ```

## Usage

### 1. Start the API Server

Run the FastAPI server using `uvicorn`:

```bash
uvicorn app_api:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

### 2. Run the Agent

You can trigger the agent by sending a POST request to `/run-agent`.

**Endpoint**: `POST /run-agent`

**Request Body**:
```json
{
  "goal": "Summarize the document",
  "input_file": "data/sample.txt"
}
```

**Example using Curl**:
```bash
curl -X POST "http://127.0.0.1:8000/run-agent" \
     -H "Content-Type: application/json" \
     -d '{"goal": "Summarize the document", "input_file": "data/sample.txt"}'
```

## Features

-   **Planner**: Decomposes high-level goals into executable steps.
-   **Memory**: Stores context and intermediate results.
-   **Tools**:
    -   `read_file`: Reads content from local files.
    -   `write_file`: Saves results to files.
    -   `summarize_text`: (Mock) Summarizes input text.
    -   `analyze_text`: (Mock) Provides word and character counts.
