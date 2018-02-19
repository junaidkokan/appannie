# -*- coding: utf-8 -*-
'''
Created on 29.01.2018

@author: junaidkokan
'''


class AppMarketData(object):
    
    APP_DETAILS_ENDPOINT = "https://api.appannie.com/v1.2/{vertical}/{market}/{asset}/{product_id}/details"
    APP_RANK_HISTORY = "https://api.appannie.com/v1.2/{vertical}/{market}/{asset}/{product_id}/ranks"
    APP_REWIEWS_ENDPOINT = "https://api.appannie.com/v1.2/{vertical}/{market}/{asset}/{product_id}/reviews"
    APP_RATINGS_ENDPOINT = "https://api.appannie.com/v1.2/{vertical}/{market}/{asset}/{product_id}/ratings"

    def __init__(self, requestClient, **kwargs):
        self.request_client = requestClient
        self.vertical = kwargs.get("vertical")
        self.market =  kwargs.get("market")
        self.asset =  kwargs.get("asset")
        self.product_id =  kwargs.get("product_id")
    
    def appFeaturedAPIs(self):
        return AppFeatured(request_client = self.request_client)
    
    def appDetails(self):
        '''
        https://support.appannie.com/hc/en-us/articles/115014439588-1-App-Details-
        '''
        url = self.APP_DETAILS_ENDPOINT.format(vertical = self.vertical, market = self.market,
                                               asset = self.asset, product_id = self.product_id
                                               )
        data = self.request_client.requestAPI(url, {})
        return data
    
    def appRankHistory(self, start_date, end_date, interval, countries, category,
                       feed, device):
        '''
        https://support.appannie.com/hc/en-us/articles/115014440748-2-App-Rank-History
        '''
        url = self.APP_RANK_HISTORY.format(vertical = self.vertical,
                                           market = self.market,
                                           asset = self.asset,
                                           product_id = self.product_id
                                           )
        data_dict = {"start_date": start_date, "end_date": end_date,
                     "interval": interval, "countries": countries,
                      "feed": feed, "device": device, "category": category
                      }
        data = self.request_client.requestAPI(url, data_dict)
        return data
    
    def  appReviews(self, start_date, end_date, version = "all",
                    countries = "", rating = "1+2+3+4+5", page_index = 0,
                    page_size = 100):
        '''
        https://support.appannie.com/hc/en-us/articles/115014521228-3-App-Reviews-
        '''
        url = self.APP_REWIEWS_ENDPOINT.format(vertical = self.vertical,
                                               market = self.market,
                                               asset = self.asset,
                                               product_id = self.product_id
                                               )
        data_dict = {"start_date": start_date, "end_date": end_date,
                     "countries": countries, "page_index": page_index,
                     "page_size": page_size, "version": version,
                     "rating":rating }
        data = self.request_client.requestAPI(url, data_dict)
        return data
    
    def appRating(self, page_index = 0):
        '''
        https://support.appannie.com/hc/en-us/articles/115014521908-4-App-Ratings-
        '''
        url = self.APP_RATINGS_ENDPOINT.format(vertical = self.vertical,
                                               market = self.market,
                                               asset = self.asset,
                                               product_id = self.product_id
                                               )
        data_dict = {"page_index": page_index}
        data = self.request_client.requestAPI(url, data_dict)
        return data
    


class AppFeatured(object):
    
    FEATURED_METADATA_PLACEMENT_CATEGORIES_ENDPOINT = "https://api.appannie.com/v1.2/meta/feature/categories"
    FEATURED_METADATA_PLACEMENT_TYPES_ENDPOINT = "https://api.appannie.com/v1.2/meta/feature/types"
    DAILY_FEATURES_ENDPOINT = "https://api.appannie.com/v1.2/{vertical}/{market}/{asset}/{product_id}/featured"
    FEATURE_HISTORY_ENDPOINT = "https://api.appannie.com/v1.2/{vertical}/{market}/{asset}/{product_id}/featured_history"
     
    def __init__(self, request_client, **kwargs):
        self.request_client = request_client
    
    def featuredMetaDataPlacementCategories(self, market, countries):
        '''
        https://support.appannie.com/hc/en-us/articles/115014397947-5-App-Featured
        '''
        url = self.FEATURED_METADATA_PLACEMENT_CATEGORIES_ENDPOINT
        data_dict = {"market": market,
                     "countries": countries
                     }
        data = self.request_client.requestAPI(url, data_dict)
        return data
    
    def featuredMetaDataPlacementTypes(self, market):
        '''
        https://support.appannie.com/hc/en-us/articles/115014397947-5-App-Featured#categories
        '''
        url = self.FEATURED_METADATA_PLACEMENT_TYPES_ENDPOINT
        data_dict = {"market": market
                     }
        data = self.request_client.requestAPI(url, data_dict)
        return data
    
    def dailyFeatures(self, vertical, market, asset, product_id, start_date,
                      end_date, device, countries, categories, types, page_size):
        url = self.DAILY_FEATURES_ENDPOINT.format(vertical = vertical, market = market, asset = asset, product_id = product_id)
        data_dict = { "start_date": start_date,
                      "end_date": end_date,
                      "device": device,
                      "countries":countries,
                      "categories": categories,
                      "types": types,
                      "page_size": page_size
            }
        data = self.request_client.requestAPI(url, data_dict, union_key = "daily_features")
        return data
    
    def featuredHistory(self, vertical, market, asset, product_id, start_date,
                        end_date, device, country, category, types, page_size):
        url = self.FEATURE_HISTORY_ENDPOINT.format(vertical = vertical, market = market, asset = asset, product_id = product_id)
        data_dict = { "start_date": start_date,
                      "end_date": end_date,
                      "device": device,
                      "country": country,
                      "category": category,
                      "type": types,
                      "page_size": page_size
                      }
        data = self.request_client.requestAPI(url, data_dict, union_key = "feature_history")
        return data
    
    
