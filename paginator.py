# -*- coding: utf-8 -*-
'''
Created on 29.01.2018

@author: junaidkokan
'''
import urllib2
import urllib
import time
import json
from datetime import datetime
from retrying import retry
from .exception import (AppAnnieBadRequestException,
                        AppAnnieUnauthorizedException,
                        AppAnnieNoPermissionException,
                        AppAnnieNotFoundException,
                        AppAnnieMethodNotSuppprtedException,
                        AppAnnieTemporaryBlacklistingException,
                        AppAnnieRateLimitExceededException,
                        AppAnnieInternalErrorException,
                        AppAnnieServiceUnavailableException,
                        AppAnnieException
                        )

# HTTP code to retry request
Retry_Codes = [429] #[503, 429]


def exception_from_response(code, message):
    if code == AppAnnieBadRequestException.ERROR_CODE:
        return AppAnnieBadRequestException
    if code == AppAnnieUnauthorizedException.ERROR_CODE:
        return AppAnnieUnauthorizedException
    if code == AppAnnieNoPermissionException.ERROR_CODE:
        return AppAnnieNoPermissionException
    if code == AppAnnieNotFoundException.ERROR_CODE:
        return AppAnnieNotFoundException
    if code == AppAnnieMethodNotSuppprtedException.ERROR_CODE:
        return AppAnnieMethodNotSuppprtedException
    if code == AppAnnieTemporaryBlacklistingException.ERROR_CODE:
        return AppAnnieTemporaryBlacklistingException
    if code == AppAnnieRateLimitExceededException.ERROR_CODE:
        return AppAnnieRateLimitExceededException
    if code == AppAnnieInternalErrorException.ERROR_CODE:
        return AppAnnieInternalErrorException            
    if code == AppAnnieServiceUnavailableException.ERROR_CODE:
        return AppAnnieServiceUnavailableException
    return AppAnnieException(message)
    


# function to check if retry necessary
def retry_condition(result):
    StartRetry = False
    if type(result) is str:
        StartRetry = False
    elif result[0] in Retry_Codes:
        print('Retrying... HTTP Error. Status Code - ' + str(result) + ' Timestamp: ' + str(datetime.now()))
        StartRetry = True
    else:
        StartRetry = False
        raise exception_from_response(result[0], result[1]) 

    return StartRetry


# Class to request data from a website
class BaseRequest(object):
    
    def __init__(self, key):
        self.key = key
        self.last_request_time = time.time()
    
    def jsonify(self, data_str):
        jsn = json.loads(data_str)
        return jsn

    def _add_headers(self, request, headers):
        for key, value in headers.items():
            request.add_header(key, value)
        return request

    @retry(retry_on_result=retry_condition, wait_exponential_multiplier=1000, wait_exponential_max=60000)
    def httpRequestAPI(self, url, data_dict, headers={}, content_type="x-www-form-urlencoded", context=None):

        if content_type == "x-www-form-urlencoded":
            # Encoding parameters
            data_encoded = urllib.urlencode(data_dict)
            if data_encoded == '':
                full_url = url
            else:
                full_url = url + '?' + data_encoded
            req = urllib2.Request(full_url)

        elif content_type == "json":
            full_url = url
            req = urllib2.Request(url, json.dumps(data_dict))

        # Checking for headers and adding to request
        req.add_header("Authorization", 'Bearer %s' %self.key)
        if len(headers) > 0:
            req = self._add_headers(req, headers)

        try:
            while True:
                if ((time.time() - self.last_request_time) > 2.5):
                    self.last_request_time = time.time()
                    if context != None:
                        responseObj = urllib2.urlopen(req, context=context)
                    else:
                        responseObj = urllib2.urlopen(req)
                    break
                else:
                    time.sleep(0.5)
            return responseObj.read()
        except urllib2.HTTPError as e:
            #print str(e)
            return e.code, e.reason


class Paginator(BaseRequest):
    def __init__(self, key): 
        super(Paginator, self).__init__(key)
        
        
        
    def requestAPI(self,  url, data_dict, headers={}, content_type="x-www-form-urlencoded", context=None, union_key=None):
        data_str = self.httpRequestAPI(url, data_dict, headers, content_type, context)
        data_jsn = self.jsonify(data_str)
        
        if data_jsn.get("next_page"):
            if not union_key:
                raise ValueError("union_key not provided to paginate requests")
            self.paginate(data_jsn, union_key)
            keys_to_del = ["next_page", "page_index", "page_num", "page_size", "prev_page"]
            for key in keys_to_del:
                if data_jsn.get(key):
                    data_jsn.pop(key)
        return data_jsn
    
        
    def paginate(self, data_jsn, union_key):
        
        page_num = data_jsn.get("page_num")
        page_index = data_jsn.get("page_index")
        url = "https://api.appannie.com" + data_jsn.get("next_page")
        
        union_result = data_jsn[union_key]
        
        while page_index < page_num - 1:
            
            page_result = self.httpRequestAPI(url, data_dict = {})
            page_result = self.jsonify(page_result)
            
            page_index = page_result.get('page_index')
            page_num = page_result.get("page_num")
            url = "https://api.appannie.com" + page_result.get("next_page")
            
            page_result = page_result.get(union_key, [])
            union_result.extend(page_result)
            
        
        

