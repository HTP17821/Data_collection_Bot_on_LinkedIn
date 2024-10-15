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
 - task 1. **Login to LinkedIn**: Automates the login process by reading credentials from the `Login_info.txt` file and submitting them on the LinkedIn login page.
 - task 2. **Perform Search**: Enters a fixed search query (e.g., "Data Engineer") in the LinkedIn search bar to find relevant profiles.
 - task 3. **Crawl Profile URLs**: Collects URLs of the profiles listed on the search results pages for further data extraction.
 - task 4. **Extract Profile Information**: Extracts key information from each LinkedIn profile, such as name, job title, and location.
 - task 5. **Save Data to Excel**: Stores the scraped profile data in an Excel file, making it easy to analyze and use later.


### Note
- **Sleep() Function**: The `Sleep()` function is utilized to throttle the bot's operation speed, helping to avoid account bans by LinkedIn due to excessive requests.
- **Data Scraping Challenges**: In Task 4, the data scraping function was not optimally implemented. As a result, the bot collects not only the URLs of the target user profiles but also the URLs of their connections. This issue leads to duplicated entries across multiple pages, resulting in an output that exceeds the actual number of unique profiles saved to the output file.
- **Proposed Solution**: To address this, I plan to implement an ETL process that will loop through the output file to eliminate duplicate entries before saving the refined data into a data mart. (This enhancement will be developed and uploaded at a later stage. ^^)


## Requirements
- Python 3.x
- Required libraries listed in `requirements.txt`

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
