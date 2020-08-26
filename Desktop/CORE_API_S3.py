import requests
import getpass
import json
import boto3 

search_term = 'artificial intelligence'

bucket_name = 'core0823'

api_key = getpass.getpass("Key: ")
aws_key = getpass.getpass("Key: ")
aws_secret_key = getpass.getpass("Key: ")

s3 = boto3.client('s3',
    region_name = 'us-east-1',
    aws_access_key_id= aws_key,
    aws_secret_access_key = aws_secret_key)


def create_api_param(f_key, f_page, f_pagesize):
    """
    Retunrs formatted dictionary with api parameters.
    """
    f_api_param = {"page": f_page, "pageSize": f_pagesize, "apiKey": f_key, }
    return f_api_param


def get_search_results(f_search_url, f_search_term, f_search_params_dic):
    """
    Make the API call and return JSON data
    """
    try: 
        f_search_term = f_search_term.replace(' ','%20')
        search_url = f_search_url + f_search_term
        search_response = requests.get(search_url, params=f_search_params_dic)
        call_status = search_response.status_code
        if call_status == 200:
            search_json_data = search_response.json()
        
        return search_json_data
    
    except:
        print('Error in API call.')


def main(f_search_term, f_key, f_bucket):
    api_search_url = 'https://core.ac.uk/api-v2/search/'
    pageSize = 100
    page_list = range(1,100,1)
    try:
        for i in page_list:
            print('Page '+str(i))
            api_parm = create_api_param(f_key, i, pageSize)
            tmp_json_data = get_search_results(api_search_url, f_search_term, api_parm)
            file_key = 'Core ' + f_search_term + 'page' + str(i) + '.json'
            s3.put_object(Body=str(tmp_json_data), Bucket=f_bucket, Key=file_key)   
    except:
        pass
        print('error')



if __name__ == "__main__":
    main(search_term, api_key, bucket_name) 

