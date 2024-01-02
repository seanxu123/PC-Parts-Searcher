from flask import Flask, render_template, request
import web_scraper
import threading
import json
import os
import time
import datetime
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
twilio_num = os.getenv("twilio_num")
phone_num = os.getenv("phone_num")
key = os.getenv("EBAY_API_KEY")

# Global flags for search control
is_new_search = False
search_ongoing = False

app = Flask(__name__)

@app.route('/')
def index():
     """Render the main index.html page."""
     return render_template('index.html') 

@app.route('/', methods=['POST'])
def get_value():
    """Handle form submission and initiate the search."""
    global is_new_search
    
    # Collect form data for items and max prices
    filled_elements = [v for k, v in request.form.items() if v] 
  
    items = []
    max_prices = []
    
    # Split the collected data into items and max_prices lists
    for index, value in enumerate(filled_elements):
        if index % 2 == 0:
            items.append(value)
        else:
            max_prices.append(value)
    
    #Function to send a notification message
    def send_message(listing):
        client = Client(account_sid, auth_token)
        text = "New listing detected:\n" + listing["Title"] + "\n" + "Price: " + listing["Price"] + "\n" + listing["URL"]
        
        message = client.messages.create(
            body = text,
            from_=twilio_num,
            to=phone_num
        )
        
        print("Sent messsage:", message.body)        
        
    
    # Continuous search function looking for listings every 30 seconds
    def cont_search():
        global is_new_search
        global search_ongoing
        
        print("Continously searching...")
        
        search_ongoing = True
        item_detected = False
        checkpoint_time = datetime.datetime.now() 
        
        while is_new_search == False: #While the user hasn't submitted a new form        
            time.sleep(30)
            
            for i in range(len(items)): 
                print("Searching for", str(items))
                listings = web_scraper.execute_search(key, items[i], max_prices[i])
                
                for listing in listings:
                    listing_time = datetime.datetime.strptime(listing["Start Time"], "%Y-%m-%d %H:%M:%S")
                    
                    #If listing was posted later than checkpoint_point, notify user
                    if listing_time >= checkpoint_time: 
                        item_detected = True
                        print("New listing detected!")
                        print(listing)
                        send_message(listing)
                
            if item_detected == False:
                print("No new item detected")
            else:
                item_detected = False
                checkpoint_time = datetime.datetime.now()

            if is_new_search: #If user submitted new form, stop executing function
                    search_ongoing = False
                    break
                
             
    try:
       print('Returning results to front end')
       total_results = []
      
       for i in range(len(items)):
           item_results = web_scraper.execute_search(key, items[i], max_prices[i])
           total_results.append(item_results)
      
       is_new_search = True
       #Display search results in webpage
       return render_template('tabs_opener.html', total_results=total_results, items = items)

    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error occurred" 
    
    finally:
         # Ensure previous search thread has completed before starting a new one
        while search_ongoing: 
            time.sleep(1)
            
        is_new_search = False
        threading.Thread(target=cont_search).start() #Start background_search
        



if __name__ == "__main__":
    app.run(debug=True)
    
    
    

   
    
     