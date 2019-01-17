# Scheduling DynamoDB Backups

<https://cloudcraft.linuxacademy.com/#/labs/details/36f2b226-5a94-4e3e-8243-4c4474003cba?courseId=313>

## Test Locally

Use [`python-lambda-local`](https://github.com/HDE/python-lambda-local)

```sh
python-lambda-local -f lambda_handler lambda_function.py event.json -e environment_variables.json
```
