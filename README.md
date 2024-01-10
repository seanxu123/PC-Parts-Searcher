# Computer-Parts-Searcher
This project is a web scraper designed to search for computer parts (or any other item) on eBay using their official API. Users can input any number of items and their maximum prices via a web form. The scraper will then fetch all items matching the criteria and display the results on the webpage, including details such as item title, price, shipping fee, and URL. The program also continuously searches for items throughout the day and sends SMS notifications to the user whenever a matching item is found.

## Example
1. Enter items and their max prices on a web form
<img width="1466" alt="Screenshot 2024-01-02 at 4 53 50 PM" src="https://github.com/seanxu123/PC-Parts-Searcher/assets/146236984/ae04e014-e071-4c0d-9063-6d920e513d85">

2. Receive detailed search results
<img width="1467" alt="Screenshot 2024-01-02 at 4 58 33 PM" src="https://github.com/seanxu123/PC-Parts-Searcher/assets/146236984/483169cf-ece6-4699-93e4-bef5e15686ed">

3. Receive instant SMS notifications whenever a matching item is found
<img width="1466" alt="Screenshot 2024-01-02 at 4 53 50 PM" src="https://github.com/seanxu123/PC-Parts-Searcher/assets/146236984/a852a686-f7e4-4019-9d80-a1b6a5c2d5bb">

## Inspiration Behind the Project
The inception of this project stems from a conversation with a close friend who runs a computer business. He shared the challenges of constantly scouring online platforms for the best deals on computer parts, a process that consumed a significant amount of his time. Recognizing the need for a more efficient solution, I conceptualized this program to improve the search process for computer parts or any other item of interest. The primary objective is to help individuals like my friend focus on critical aspects of their business, rather than getting entangled in the intricacies of online deal hunting.

## Features
- Real-time SMS Notifications: Stay informed about the best deals without constantly checking the website. Receive instant SMS notifications whenever the program identifies a matching item within your specified criteria.
- High-Capacity Search: The program is designed to process up to 10,000 items per search. This ensures comprehensive coverage and increases the likelihood of finding the most relevant deals.
- Dynamic Search: Users can input any number of items and their maximum prices to find relevant computer parts.
- User-Friendly Interface: The web-based form simplifies the search process, providing an intuitive experience for users.
- Detailed Results: The scraper retrieves and displays comprehensive details about each item, including its title, price, shipping fee, and URL.

## How was it Built?
Tech stack used: HTML, CSS, JavaScript, Python, Flask

**Why did I choose this stack:**
For this project's front-end, I chose to use the classic trio of HTML, CSS and JavaScript, as they work well in tandem to create simple yet elegant webpages. In particular, HTML helps set the foundtational structure of the webpage, with CSS providing the visual styling, while JavaScript enables user interactions. On the backend, Python with the Flask framework offer a robust foundation and a vast array of libraries, allowing for efficient data processing, API interactions, and server-side functionalities.  

## How this application could be improved
Here are some of the features we are currently working on to improve the product:
- Reduce delay times between subsequent searches 
- Increase the number of websites to extract data from
- Allow users to sort through results
- Implement a more sophisticated item filter system

## Installation
To set up the project locally, follow these steps:

1. Clone the repository
```
git clone https://github.com/seanxu123/PC-Parts-Searcher.git
```
2. Navigate to the project directory
```
cd PC-Parts-Searcher
```
3. Install the required packages:
   
Ex: Installing pytz package
```
pip3 install pytz
```
List of packages to install:
- Flask
- dotenv
- twilio
- pytz
- ebaysdk

4. Get your necessary keys and credentials:
   
Checklist:
- Ebay API production key (Sign up with the Ebay developer's program)
- Twilio account sin (Create a Twilio account)
- Twilio account auth_num
- Twilio phone number

## Usage
1. Run the application in the terminal
```
python3 app.py
```
2. Open your web browser and navigate to http://localhost:5000.
3. Enter the item names and maximum prices in the provided form fields.
4. Click the "Search" button to initiate the search.
5. View the results displayed on the webpage, including the item title, price, shipping fee, and URL.
6. Receive SMS notifications throughout the day whenever a new matching item is found.

## Contributors:
Sean Xu
- Linkedin: https://www.linkedin.com/in/sean-xu-688957247/ 
- Email: seanxu419@gmail.com

Hamza Chaudry:
- Linkedin: https://www.linkedin.com/in/hamzachaudhry5/
- Email: hamza.chaudhry5@outlook.com

