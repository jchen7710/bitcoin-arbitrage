import logging
from .observer import Observer


class Logger(Observer):
    def opportunity(self, profit, volume, buyprice, kask, sellprice, kbid, perc,
                    weighted_buyprice, weighted_sellprice):
        logging.info("profit: %f USD with volume: %f BTC - buy from %s at %f sell to %s at price %f profit=  ~%.2f%% total= %f" \
        	% (profit, volume, kask, buyprice, kbid, sellprice, perc, buyprice*volume))
