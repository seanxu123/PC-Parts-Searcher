import os
import pytz
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

key = os.getenv("EBAY_API_KEY")

# eBay class for fetching listings
class Ebay(object):
    def __init__(self, key, search_term, max_price):
        self.key = key
        self.search_term = search_term
        self.max_price = max_price
       
    
    def fetch(self):
        listings = [] # List to store fetched listings
        item_count = 0 # Counter for items
        
        # Initialize eBay API connection
        api = Connection(appid=self.key,  config_file=None, siteid ="EBAY-ENCA")
        #You can fetch up to 100 pages of data according to the API documentation
        MAX_PAGE = 100 
        
        try:
            for page_num in range(1, MAX_PAGE + 1):
                # Make API request to eBay
                response = api.execute('findItemsAdvanced', {'keywords': self.search_term, 
                                                            'paginationInput': {'pageNumber': page_num}, 
                                                            "itemFilter": [
                                                                {
                                                                  "name": "MaxPrice",
                                                                  "value": self.max_price,
                                                                  "paramName": "Currency",
                                                                  "paramValue": "CAD",
                                                                }], 
                                                            "outputSelector": ["sellerInfo", "shippingInfo", "condition"]
                                                            })
                

                page_number = response.reply.paginationOutput.pageNumber 
                print("Page Number:", page_number) #Print Page Number
                
                items = response.reply.searchResult.get('item', [])
                #If no items are returned, or reached end of the list, return listings
                if len(items) == 0 or page_num == 101:
                    return listings 


                #Function that checks for duplicate items (items with same title)
                def is_duplicate(title):
                    for item in listings:
                        if item["Title"] == title:
                            return True
                         
                    return False
                
                
                # Process each item in the response
                for item in items:
                    if hasattr(response.reply.searchResult, 'item'):
                      
                        price = item.sellingStatus.convertedCurrentPrice.value
                        shipping_fee = item.shippingInfo.shippingServiceCost.value if hasattr(item.shippingInfo, "shippingServiceCost") else None
                        title = item.title
                        url = item.viewItemURL
                        gmt_start_time = item.listingInfo.startTime 
                        gmt_start_time = pytz.timezone('Etc/GMT').localize(gmt_start_time) #Localize time to GMT
                        atl_start_time = gmt_start_time.astimezone(pytz.timezone('America/Toronto')) #Convert time at EST
                        atl_start_time = atl_start_time.strftime('%Y-%m-%d %H:%M:%S') #Convert time to string
                        condition = item.condition.conditionDisplayName if hasattr(item, 'condition') else None
                        
                        #Adjust total price depending on value of shipping fee
                        if shipping_fee != "N/A":
                            total_price = round(float(price)+ float(shipping_fee) ,2)
                        else:
                            total_price = f"{price} + N/A shipping fee"    
                        
                        # Check condition and duplicate status before adding to listings
                        if condition != "For parts or not working" and is_duplicate(title) == False:
                            item_count += 1
                
                            attributes = {
                                "Item count": item_count,
                                "Title": title,
                                'Price': price,
                                'Shipping fee': shipping_fee,
                                'URL': url,
                                'Condition': condition,
                                'Start Time': atl_start_time
                                'Total Price': total_price

                            }
                            listings.append(attributes)          
            
        except ConnectionError as e:
            print(e)
            print(e.response.dict())


# Function to execute the eBay search
def execute_search(key, items, max_prices):
    return Ebay(key, items, max_prices).fetch()
    


    






