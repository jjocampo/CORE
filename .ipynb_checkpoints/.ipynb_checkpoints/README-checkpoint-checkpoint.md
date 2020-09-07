# CORE

## About
[Core](https://core.ac.uk/) is the world's largest collection of open access research papers. A [free API](https://core.ac.uk/services/api/) exists that can be utilized within certain terms. The purpose of this project is to work with the CORE API in combination with AWS SageMaker as a personal project. 

##### Update 2020.09.07
* The beginning of this project started on my local machine as I configured API calls to CORE. After initial success, the processing was moved over to AWS.
    * The code that is within the [/Desktop](https://github.com/jjocampo/CORE/tree/master/Desktop) folder stopped at this point. 
* The [/SageMaker](https://github.com/jjocampo/CORE/tree/master/SageMaker) folder contains all current code, including the API call code that was started on my local machine. Progress to date includes:
    * Iterating over four search terms and ingesting ~39,000 JSON files to S3.
    * Iterating over the JSON files in S3 and creating a metadata catalog for serach information returned. 
    * Pre-processing steps for transforming the text data to support modeling (e.g. BlazingText) in development. 