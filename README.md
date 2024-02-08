# Please choose 2 out of the 3 following tasks and complete them:
---
### Task 1) Please list at least 5 public tenders awarded from the following regions - Europe (EU-level, or any European country) and The United States. At least 2 of the 5 awarded companies should be a publicly listed company.
- Please send excel/google sheet file with the following information: country, tender title/short description, awarded company name, if the awarded company is publicly listed - its ticker, main stock exchange and ISIN number, and link to the tender award notice.
For more information about the awarded public tenders, you can read the Alerts section on the TenderAlpha website.
---
### Task 2) Please extract the awarded contracts information from the official UK public procurement website following the steps:
Visit the website:
https://www.contractsfinder.service.gov.uk/Search/Results
Create a search with the following parameters:
- Keywords: financial or database or data
- Procurement Stage: Awarded contract
- Date range: 31/10/2022 – 04/11/2022
  
Download the data as .xml file
  
Read the .xml file and extract the following data from the notices:
- Publish date
- Date of award
- Title
- Short description
- Awarded company
- Awarded company address
- Awarded value 
- url
  
Save the output in .excel file

---
### Task 3) Scrape the quotes from http://quotes.toscrape.com/ (all pages) and save the output in csv, json or whatever format you prefer. Each entity should have:
-	 text - quote text (required)
-	 author - the author of the quote (required)
-	 tags - string with the tags of the quote separated with ';' (if they exists)
-	 url - the url where you can find the quote


### Example of quote entity:
- {
-	'text'	: 'The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.',
-	'author': 'Albert Einstein',
-	'tags'	: 'change;deep-thoughts;thinking;world',
-    'url'.  : 'http://quotes.toscrape.com/'
- }
