# data-structures
Data-structure traversal and algorithm behavior backend visualization service in graphql

## Steps to Run
### Docker
1. Build - `make build`
1. Run - `make run` 

### Local
1. `uvicorn src.server.app:app --reload --workers 1 --host 0.0.0.0 --port 5050`
