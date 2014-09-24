inc5000_scraper
===============

Requires Requests:
$ pip install requests
$ easy_install requests

Scrape the Inc 5000 list and return a dictionary with values for every company.

Since accessing a company’s JSON file requires only its ID value, every company’s information can be reached iteratively with only the first company’s 
ID.  The last company has no next_id value, so the iteration ends with the 5,000th company.  The data from each company can be added to a large JSON 
database and stored locally.  The JSON database is approximately 5MB.  With a typical internet connection, the entire process takes less than ten 
minutes.  

There are 24 values for each company in the Inc. 5000 database.  Every company has an ID, a name, a description, a location, and a founding date.  They 
have website and Twitter information.  They have revenue and employee data for the previous year and four years ago.  This is the data used to rank the 
5,000 in the list.  Unfortunately there is no further revenue or employee data, so no time series analysis can be performed.  Every company is 
categorized by metro area, industry, and company rankings in these categories.  Finally, there is a dictionary of previous years’ rankings.  Area and 
industry-specific rankings are only available for 2014, but overall rankings can go back to 2007.