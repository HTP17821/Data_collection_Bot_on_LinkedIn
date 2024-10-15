# Data_collection_Bot_on_LinkedIn

## Introduction
This project focuses on web scraping techniques to extract valuable data from LinkedIn profiles. It automates the process of collecting information such as names, job titles, locations, and profile URLs based on specific search queries. The goal is to enhance the understanding of data engineering concepts while providing a practical tool for data collection.

GitHub Repository: [here](https://github.com/HTP17821/Data_collection_Bot_on_LinkedIn)

## Installation and Running Instructions

| Step | Command/Action |
|------|----------------|
| 1. Clone the Repository | `git clone https://github.com/HTP17821/Data_collection_Bot_on_LinkedIn.git` |
| 2. Navigate to the Project Directory | `cd Data_collection_Bot_on_LinkedIn` |
| 3. Install Required Libraries | `pip install -r requirements.txt` |
| 4. Update Login Information File | Edit the existing `Login_info.txt` file with your LinkedIn credentials in the following format: <br>`your_email@example.com` <br>`your_password` |
| 5. Run the Project | `python Crawl_users.py` |


### Features
1. **Login to LinkedIn**: Automates the login process by reading credentials from the `Login_info.txt` file and submitting them on the LinkedIn login page.
2. **Perform Search**: Enters a fixed search query (e.g., "Data Engineer") in the LinkedIn search bar to find relevant profiles.
3. **Crawl Profile URLs**: Collects URLs of the profiles listed on the search results pages for further data extraction.
4. **Extract Profile Information**: Extracts key information from each LinkedIn profile, such as name, job title, and location.
5. **Save Data to Excel**: Stores the scraped profile data in an Excel file, making it easy to analyze and use later.


## Requirements
- Python 3.x
- Required libraries listed in `requirements.txt`

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
