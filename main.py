from datamodel import OrderDepth, UserId, TradingState, Order
from typing import List
import string

class ExponentialMovingAverage:
    def __init__(self, size):
        self.size = size
        self.prices = []
        oldEMA = 0;
    
    def calculateSMA(self):
        
        oldEMA = sum(self.prices) / len(self.prices) if self.prices else 0

    def update(self, price):
        self.prices.append(price)
        if (len(self.prices) > self.size):
            self.prices.pop(0)
        
    def calculateEMA(self, price):
        return 2*(len(self.prices)+1)*price + (1-len(self.prices)+1) * self.oldEMA
        # return sum(self.prices) / len(self.prices) if self.prices else 0





class Trader:

        
    
    def run(self, state: TradingState):
        print("traderData: " + state.traderData)
        print("Observations: " + str(state.observations))

				# Orders to be placed on exchange matching engine
        result = {}
        for product in state.order_depths:
            order_depth: OrderDepth = state.order_depths[product]
            orders: List[Order] = []
            acceptable_price = 10  # Participant should calculate this value
            # print("Acceptable price : " + str(acceptable_price))
            # print("Buy Order depth : " + str(len(order_depth.buy_orders)) + ", Sell order depth : " + str(len(order_depth.sell_orders)))
            shortMA = ExponentialMovingAverage(50)
            longMA = ExponentialMovingAverage(400)

            


            if (state.timestamp >= 50):
                shortMA.update()
            if (state.timestamp >= 400):
                longMA.update()


            if len(order_depth.sell_orders) != 0:
                best_ask, best_ask_amount = list(order_depth.sell_orders.items())[0]
                if int(best_ask) < acceptable_price:
                    print("BUY", str(-best_ask_amount) + "x", best_ask)
                    orders.append(Order(product, best_ask, -best_ask_amount))
    
            if len(order_depth.buy_orders) != 0:
                best_bid, best_bid_amount = list(order_depth.buy_orders.items())[0]
                if int(best_bid) > acceptable_price:
                    print("SELL", str(best_bid_amount) + "x", best_bid)
                    orders.append(Order(product, best_bid, -best_bid_amount))
            
            result[product] = orders
    
		    # String value holding Trader state data required. 
				# It will be delivered as TradingState.traderData on next execution.
        traderData = "SAMPLE" 
        
				# Sample conversion request. Check more details below. 
        conversions = 1
        return result, conversions, traderData