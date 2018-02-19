# -*- coding: utf-8 -*-
'''
Created on 29.01.2018

@author: junaidkokan
'''



class MarketDataIntelligence(object):
    
    def __init__(self, requestClient):
        self.request_client = requestClient
        
    def crossAppUsageAndDemographicsDataAPIs(self, vertical, market, product_id):
        return CrossAppUsageAndDemographicsDataAPI(request_client = self.request_client,
                                                   vertical = vertical,
                                                   market = market,
                                                   product_id = product_id)
        
    def downloadsAndRevenueDataAPIs(self, vertical, market):
        return DownloadsAndRevenueDataAPI(request_client = self.request_client,
                                          vertical = vertical,
                                          market = market)
    
    def usageAndEngagementDataAPIs(self, vertical, market):
        return UsageAndEngagementDataAPIs(request_client = self.request_client,
                                          vertical = vertical,
                                          market = market)
    
    def userAcquisitionAdvertisingDataAPIs(self, vertical, market):
        return UserAcquisitionAdvertisingDataAPIs(request_client = self.request_client,
                                                  vertical = vertical,
                                                  market = market)
    
    def appStoreFeaturedAppsAPI(self, vertical, market):
        return AppStoreFeaturedAppsAPI(request_client = self.request_client,
                                       vertical = vertical,
                                       market = market)
    
    def appStoreOptimizationAPIs(self, vertical, market):
        return AppStoreOptimizationAPIs(request_client = self.request_client,
                                       vertical = vertical,
                                       market = market)
    
    def appStoreRankingTopChartsAPIs(self, vertical, market):
        return AppStoreRankingTopChartsAPIs(request_client = self.request_client,
                                            vertical = vertical,
                                            market = market)
    
    def companyAndPublisherDetailsAPIs(self, org_level, detail_type):
        return CompanyAndPublisherDetailsAPIs(request_client = self.request_client,
                                              org_level = org_level,
                                              detail_type = detail_type)
    
    

class AppStoreFeaturedAppsAPI(object):
    APP_STORE_FEATURED_APPS_ENDPOINT = "https://api.appannie.com/v1.3/{vertical}/{market}/featured_apps"
    
    def __init__(self, request_client, **kwargs):
        self.request_client = request_client
        self.vertical = kwargs.get("vertical")
        self.market = kwargs.get("market")
    
    def featuredApps(self, device, countries, start_date, end_date,
                     product_ids, featured_tab, page_size = 100, page_index = 0):
        '''
        https://support.appannie.com/hc/en-us/articles/360000142788-App-Store-Featured-Apps-API
        '''
        url = self.APP_STORE_FEATURED_APPS_ENDPOINT.format(vertical = self.vertical,
                                                           market = self.market)
        data_dict = {"device": device, "countries": countries,
                     "start_date": start_date, "end_date": end_date,
                     "product_ids": product_ids, "featured_tab": featured_tab,
                      "page_size": page_size, "page_index": page_index
                      }
        data = self.request_client.requestAPI(url, data_dict, union_key = "features")
        return data
    
    
class AppStoreOptimizationAPIs(object):
    KEYWORD_EXPLORER_ENDPOINT = "https://api.appannie.com/v1.2/{vertical}/{market}/keywords/explorer"
    PRODUCT_RANKED_KEYWORDS_ENDPOINT = "https://api.appannie.com/v1.2/{vertical}/{market}/{asset}/{product_id}/keywords/ranked"
    PRODUCT_KEYWORD_PERFORMANCE_ENDPOINT = "https://api.appannie.com/v1.2/{vertical}/{market}/app/{product_id}/keywords/ranks"
    KEYWORD_MANAGEMENT_ENDPOINT = "https://api.appannie.com/v1.2/user/keywords/list"
    ADD_CUSTOMER_KEYWORDS_ENDPOINT = "https://api.appannie.com/v1.2/user/keywords/add"
    REMOVE_CUSTOMER_KEYWORDS_ENDPOINT = "https://api.appannie.com/v1.2/user/keywords/delete"
    
    def __init__(self, request_client, **kwargs):
        self.request_client = request_client
        self.vertical = kwargs.get("vertical")
        self.market = kwargs.get("market")
    
    def keywordExplorer(self, keyword, date, country, device):
        url = self.KEYWORD_EXPLORER_ENDPOINT.format(vertical = self.vertical,
                                                    market = self.market)
        data_dict = {"keyword": keyword, "date": date,
                     "country": country, "device": device
                     }
        data = self.request_client.requestAPI(url, data_dict)
        return data        
    
    def productRankedKeywords(self, product_id, asset, date, country, device):
        url = self.PRODUCT_RANKED_KEYWORDS_ENDPOINT.format(vertical = self.vertical,
                                                           market = self.market,
                                                           asset = asset,
                                                           product_id = product_id)
        data_dict = {"date": date, "country": country,
                     "device": device
                     }
        data = self.request_client.requestAPI(url, data_dict)
        return data           
    
    def productKeywordPerformance(self, product_id, keywords, start_date,
                                  end_date, country, device):
        url = self.PRODUCT_KEYWORD_PERFORMANCE_ENDPOINT.format(vertical = self.vertical,
                                                           market = self.market,
                                                           product_id = product_id)
        data_dict = {"keywords": keywords,
                     "start_date": start_date, "end_date": end_date,
                     "country": country, "device": device
                     }
        data = self.request_client.requestAPI(url, data_dict)
        return data          
    
    def keywordManagement(self):
        url = self.KEYWORD_MANAGEMENT_ENDPOINT
        data_dict = {}
        data = self.request_client.requestAPI(url, data_dict)
        return data        
    
    def addCustomerKeywords(self, product_id, keywords, country):
        url = self.ADD_CUSTOMER_KEYWORDS_ENDPOINT
        data_dict = {"product_id": product_id, "keywords": keywords,
                     "country": country}
        data = self.request_client.requestAPI(url, data_dict)
        return data         
    
    def removeCustomerKeywords(self, product_id, keywords, country):
        url = self.REMOVE_CUSTOMER_KEYWORDS_ENDPOINT
        data_dict = {"product_id": product_id, "keywords": keywords,
                     "country": country}
        data = self.request_client.requestAPI(url, data_dict)
        return data
    
    
        

class CompanyAndPublisherDetailsAPIs(object):
    COMPANY_DETAILS_ENDPOINT = "https://api.appannie.com/v1.2/{org_level}/{company_id}/{detail_type}"
    PUBLISHER_DETAILS_ENDPOINT = "https://api.appannie.com/v1.2/{org_level}/{market}/{publisher_id}/{detail_type}"
    
    def __init__(self, request_client, **kwargs):
        self.request_client = request_client
        self.org_level = kwargs.get("vertical")
        self.detail_type = kwargs.get("market")
    
    def companyDetails(self, company_id, page_size, page_index):
        url = self.COMPANY_DETAILS_ENDPOINT.format(org_level = self.org_level,
                                                   detail_type = self.detail_type,
                                                   company_id = company_id)
        data_dict = {"page_size": page_size, "page_index": page_index}
        data = self.request_client.requestAPI(url, data_dict)
        return data
    
    def publisherDetails(self, market, publisher_id, page_size, page_index):
        url = self.PUBLISHER_DETAILS_ENDPOINT.format(org_level = self.org_level,
                                                     market = market,
                                                     publisher_id = publisher_id,
                                                     detail_type = self.detail_type
                                                     )
        data_dict = {"page_size": page_size, "page_index": page_index}
        data = self.request_client.requestAPI(url, data_dict)
        return data    
        


class UserAcquisitionAdvertisingDataAPIs(object):
    CREATIVES_ENDPOINT = "https://api.appannie.com/v1.2/intelligence/{vertical}/{market}/creatives"
    ADVERTISERS_ENDPOINT = "https://api.appannie.com/v1.2/intelligence/{vertical}/{market}/advertisers"
    AD_MONETIZATION_ENDPOINT = "https://api.appannie.com/v1.2/intelligence/{vertical}/{market}/ad-monetization"
    AD_PLATFORMS_ENDPOINT = "https://api.appannie.com/v1.2/intelligence/{vertical}/{market}/ad-platforms"
    ADVERTISER_APP_OVERVIEW_ENDPOINT = "https://api.appannie.com/v1.2/intelligence/{vertical}/{market}/app/{product_id}/advertiser"
    ADVERTISER_APP_SEEN_IN_ENDPOINT = "https://api.appannie.com/v1.2/intelligence/{vertical}/{market}/app/{product_id}/advertiser_seen_in"

    def __init__(self, request_client, **kwargs):
        self.request_client = request_client
        self.vertical = kwargs.get("vertical")
        self.market = kwargs.get("market")
        
    def creatives(self, device, countries, categories, ad_platform, ranks,
                  granularity, start_date, end_date, filter_by,
                  product_id, format_creative, dimension, min_days_active):
        '''
        https://support.appannie.com/hc/en-us/articles/115014422047-User-Acquisition-Advertising-Data-APIs#seen-in
        '''
        url = self.CREATIVES_ENDPOINT.format(vertical = self.vertical,
                                             market = self.market)
        data_dict = {"device": device, "countries": countries,
                     "categories": categories, "ad_platform": ad_platform,
                     "ranks": ranks, "granularity": granularity,
                     "start_date": start_date, "end_date": end_date,
                     "filter_by": filter_by, "product_id": product_id,
                     "format": format_creative, "dimension": dimension,
                     "min_days_active": min_days_active
                     }
        data = self.request_client.requestAPI(url, data_dict)
        return data
    
    def advertisers(self, device, countries, categories, ad_platform,
                    ranks, granularity, start_date, end_date):
        '''
        https://support.appannie.com/hc/en-us/articles/115014422047-User-Acquisition-Advertising-Data-APIs#advertisers
        '''
        url = self.ADVERTISERS_ENDPOINT.format(vertical = self.vertical,
                                             market = self.market)
        data_dict = {"device": device, "countries": countries,
                     "categories": categories, "ad_platform": ad_platform,
                     "ranks": ranks, "granularity": granularity,
                     "start_date": start_date, "end_date": end_date,
                     }
        data = self.request_client.requestAPI(url, data_dict)
        return data
    
    def adMonetization(self, device, countries, categories, ad_platform, ranks,
                        granularity, start_date, end_date):
        url = self.AD_MONETIZATION_ENDPOINT.format(vertical = self.vertical,
                                             market = self.market)
        data_dict = {"device": device, "countries": countries,
                     "categories": categories, "ad_platform": ad_platform,
                     "ranks": ranks, "granularity": granularity,
                     "start_date": start_date, "end_date": end_date,
                     }
        data = self.request_client.requestAPI(url, data_dict)
        return data
    
    def adPlatforms(self, countries, categories, ad_platform, ranks,
                     granularity, start_date, end_date):
        url = self.AD_PLATFORMS_ENDPOINT.format(vertical = self.vertical,
                                             market = self.market)
        data_dict = {"countries": countries, "categories": categories,
                     "ad_platform": ad_platform, "ranks": ranks,
                     "granularity": granularity, "start_date": start_date,
                     "end_date": end_date,
                     }
        data = self.request_client.requestAPI(url, data_dict)
        return data        
    
    def advertiserAppOverview(self, product_id, device, countries,
                                granularity, start_date, end_date):
        url = self.ADVERTISER_APP_OVERVIEW_ENDPOINT.format(vertical = self.vertical,
                                             market = self.market,
                                             product_id = product_id)
        data_dict = { "product_id": product_id, "device": device,
                      "countries": countries, "granularity": granularity,
                      "start_date": start_date, "end_date": end_date,
                     }
        data = self.request_client.requestAPI(url, data_dict)
        return data           
    
    def advertiserAppSeenIn(self, product_id, device, countries,
                               categories, ad_platform, ranks, granularity,
                               start_date, end_date):
        url = self.ADVERTISER_APP_SEEN_IN_ENDPOINT.format(vertical = self.vertical,
                                             market = self.market,
                                             product_id = product_id)
        data_dict = { "product_id": product_id, "device": device,
                      "countries": countries, "categories": categories,
                      "ad_platform": ad_platform, "ranks": ranks,
                      "granularity": granularity, "start_date": start_date,
                      "end_date": end_date,
                     }
        data = self.request_client.requestAPI(url, data_dict)
        return data     
    
    
    

class AppStoreRankingTopChartsAPIs(object):
    TOP_CHARTS_API = "https://api.appannie.com/v1.2/{vertical}/{market}/ranking"
    
    def __init__(self, request_client, **kwargs):
        self.request_client = request_client
        self.vertical = kwargs.get("vertical")
        self.market = kwargs.get("market")
    
    def topCharts(self, countries, categories, feeds, date, device,
                  ranks):
        '''
        https://support.appannie.com/hc/en-us/articles/115014439368-App-Store-Rankings-Top-Charts-API
        '''
        url = self.TOP_CHARTS_API.format(vertical = self.vertical, market = self.market)
        data_dict = {"countries": countries, "categories": categories,
                     "feeds": feeds, "date": date, "device": device,
                    "ranks": ranks}
        data = self.request_client.requestAPI(url, data_dict)
        return data
    
    
class CrossAppUsageAndDemographicsDataAPI(object):
    
    CROSS_APP_USAGE_ENDPOINT= "https://api.appannie.com/v1.2/intelligence/{vertical}/{market}/app/{product_id}/cross_app_usage"
    APP_DEMOGRAPHICS_ENDPOINT = "https://api.appannie.com/v1.2/intelligence/{vertical}/{market}/app/{product_id}/demographics"

    def __init__(self, request_client, **kwargs):
        self.request_client = request_client
        self.vertical = kwargs.get("vertical")
        self.market = kwargs.get("market")
        self.product_id = kwargs.get("product_id")
        
    def crossAppUsage(self, countries, categories, start_date, end_date):
        url = self.CROSS_APP_USAGE_ENDPOINT.format(vertical = self.vertical, market = self.market, product_id = self.product_id)
        data_dict = {"countries": countries, "categories": categories, "start_date": start_date, "end_date": end_date
                     }
        data = self.request_client.requestAPI(url, data_dict)
        return data
    
    
    def appDemographics(self, countries, start_date, end_date):
        url = self.APP_DEMOGRAPHICS_ENDPOINT.format(vertical = self.vertical, market = self.market, product_id = self.product_id)
        data_dict = {"countries": countries, "start_date": start_date, "end_date": end_date
                    }
        data = self.request_client.requestAPI(url, data_dict)
        return data
    


class DownloadsAndRevenueDataAPI(object):
    
    TOP_APPS_ENDPOINT = "https://api.appannie.com/v1.2/intelligence/{vertical}/{market}/ranking"
    APP_HISTORY_ENDPOINT = "https://api.appannie.com/v1.2/intelligence/{vertical}/{market}/app/{product_id}/history"
    TOP_PUBLISHERS_ENDPOINT = "https://api.appannie.com/v1.2/intelligence/{vertical}/{market}/publisher-ranking"
    PUBLISHER_HISTORY_ENDPOINT = "https://api.appannie.com/v1.2/intelligence/{vertical}/{market}/publisher/{publisher_id}/history"
    
    def __init__(self, request_client, **kwargs):
        self.request_client = request_client
        self.vertical = kwargs.get("vertical")
        self.market = kwargs.get("market")
    
    def topApps(self, device, countries, categories, feeds, ranks, granularity, start_date, end_date):
        url = self.TOP_APPS_ENDPOINT.format(vertical = self.vertical,
                                            market = self.market)
        data_dict = { "countries": countries, "categories": categories,
                      "feeds": feeds, "device": device,
                      "ranks": ranks, "granularity": granularity,
                      "start_date": start_date, "end_date": end_date
                    }
        data = self.request_client.requestAPI(url, data_dict)
        return data
    
    def appHistory(self, product_id, countries, feeds, device, granularity,
                   start_date, end_date, page_index = 0):
        url = self.APP_HISTORY_ENDPOINT.format(vertical = self.vertical,
                                               market = self.market,
                                               product_id = product_id)
        data_dict = {"countries": countries, "feeds": feeds,
                     "device": device, "granularity": granularity,
                     "start_date": start_date, "end_date": end_date,
                     "page_index": page_index
                    }
        data = self.request_client.requestAPI(url, data_dict)
        return data
    
    def topPublishers(self, device, countries, categories, feeds,
                      ranks, granularity, start_date, end_date,
                      page_index = 0):
        url = self.TOP_PUBLISHERS_ENDPOINT.format(vertical = self.vertical,
                                                  market = self.market
                                                  )
        data_dict = {"device": device, "countries": countries, 
                     "categories": categories, "feeds": feeds,
                     "ranks": ranks, "granularity": granularity,
                     "start_date": start_date, "end_date": end_date,
                     "page_index": page_index
                     }
        data = self.request_client.requestAPI(url, data_dict)
        return data
    
    def publisherHistory(self, publisher_id, countries, categories, feeds,
                         device, granularity, start_date, end_date,
                         page_index):
        url = self.PUBLISHER_HISTORY_ENDPOINT.format(vertical = self.vertical,
                                                     market = self.market,
                                                     publisher_id = publisher_id
                                                     )
        data_dict = {"publisher_id": publisher_id,
                     "countries": countries,
                     "categories": categories,
                     "feeds": feeds,
                     "device": device,
                     "granularity": granularity,
                     "start_date": start_date,
                     "end_date": end_date,
                     "page_index": page_index
                    }
        data = self.request_client.requestAPI(url, data_dict)
        return data


class UsageAndEngagementDataAPIs(object):
    
    USAGE_TOP_APPS_ENDPOINT = "https://api.appannie.com/v1.2/intelligence/{vertical}/{market}/usage-ranking"
    USAGE_APP_HISTORY = "https://api.appannie.com/v1.2/intelligence/{vertical}/{market}/app/{product_id}/usage-history"
    USER_RETENTION_ENDPOINT = "https://api.appannie.com/v1.2/intelligence/{vertical}/{market}/app/{product_id}/user-retention"
    
    def __init__(self, request_client, **kwargs):
        self.request_client = request_client
        self.vertical = kwargs.get("vertical")
        self.market = kwargs.get("market")
    
    def usageTopApps(self, device, countries, categories, segment, ranks,
                     granularity, start_date, end_date):
        url = self.USAGE_TOP_APPS_ENDPOINT.format(vertical = self.vertical,
                                                  market = self.market)
        data_dict = {"device": device,
                     "countries": countries,
                     "categories": categories,
                     "segment": segment,
                     "ranks": ranks,
                     "granularity": granularity,
                     "start_date": start_date,
                     "end_date": end_date
                     }
        data = self.request_client.requestAPI(url, data_dict)
        return data
    
    def usageAppHistory(self, product_id, countries, device, segment,
                        granularity, start_date, end_date,
                        page_index = 0):
        url = self.USAGE_APP_HISTORY.format(vertical = self.vertical,
                                            market = self.market
                                            )
        data_dict = {"product_id": product_id,
                     "countries": countries,
                     "device": device,
                     "segment": segment,
                     "granularity": granularity,
                     "start_date": start_date,
                     "end_date": end_date,
                     "page_index": page_index
                     }
        data = self.request_client.requestAPI(url, data_dict)
        return data        
        
    def userRetention(self, product_id, countries, device, start_date,
                      end_date):
        url = self.USER_RETENTION_ENDPOINT.format(vertical = self.vertical,
                                                  market = self.market,
                                                  product_id = product_id
                                                  )
        data_dict = {#"product_id": product_id,
                     "countries": countries,
                     "device": device,
                     "start_date": start_date,
                     "end_date": end_date}
        data = self.request_client.requestAPI(url, data_dict)
        return data         
        
        