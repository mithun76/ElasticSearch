### ElaticSearch service

elasticSearch service can be used to handle your database.
This repository contains `es.py`(lambda function) and two required packages `requests`, `requests_aws4auth`

### Installation

## If you want to test your code from local system user the below command

    reuests-aws4auth:
    			pip install requests-aws4auth
    requests:
    			pip install requests

## If you want to upload you function to AWS Lambda,then follow below steps:

# 1 download or clone the packages from this git repository.
# 2 Update code in es.py for your requirment.

### Uploading to Lambda

# 1 Archive(.zip) python file(es.py) along with the packages (files: `requests1,`requests-aws4auth`).[ex: test.zip]

# 2 go to -> aws dashboard-> Lambda -> create function -> enter FunctionName-> runtime(Python 3.8)->create function.

# 3 Once function created goto->code entry type(under function code)-> upload a .zip file->upload(under Function Package)-> upload your `test.zip` file.

# 4 In Handler info(right of the page)-> update your filename_without_extension.main_function_name(ex: `es.es_search_main` in don't add .py to filename).

# 5 If you're handling to many search operations goto->basic settings(scroll down same page)-> increase Timeout[optional]->save
