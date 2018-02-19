# -*- coding: utf-8 -*-
'''
Created on 29.01.2018

@author: junaidkokan
'''



from .paginator import Paginator
from .app_market_data import AppMarketData
from .market_intelligence import MarketDataIntelligence





class AppAnnie(object):
    
    def __init__(self, key):
        self.key = key
    
    def requestClient(self):
        return Paginator(self.key)
        
    def marketDataIntelligence(self):
        return MarketDataIntelligence(self.requestClient())
    
    def appMarketData(self, vertical = None, market = None, asset = None,
                      product_id = None):
        return AppMarketData(self.requestClient(), vertical = vertical,
                             market = market, asset = asset,
                             product_id = product_id)
        
        




        
