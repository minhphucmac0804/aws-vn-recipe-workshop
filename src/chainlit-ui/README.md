# Chainlit UI

This folder contains the minimal local UI used by the workshop.

The UI is intentionally small. It sends each chat message to the deployed Lambda Function URL and displays the Lambda response. Historical local-Qdrant and experimental branches are not included here because the submitted workshop focuses on the final Lambda RAG path.

## Requirements

Install the local UI dependencies in your Python environment:

```bash
pip install chainlit requests
```

## Configuration

Set the Lambda Function URL before starting Chainlit:

```bash
export LAMBDA_FUNCTION_URL="<function-url-redacted>"
export RECIPE_API_TIMEOUT="20"
```

Use your own Lambda Function URL. Do not commit real function URLs or API keys.

## Run

From the repository root:

```bash
chainlit run src/chainlit-ui/chainlit_app.py
```

Then open the local URL printed by Chainlit and ask a Vietnamese recipe question, for example:

```text
mon ga thanh dam
```
