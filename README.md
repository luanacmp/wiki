# CS50-Project1-WIKI


The aim of this project was to build a Wikipedia-like online encyclopedia using the Python Django framework. Users can view available article entries, as well as search for entries on the site. New entries can be created by users, and existing entries can be edited. There is also a 'random page' function that selects and displays a page of the encyclopedia at random.


## Youtube short Video
In a brief video: [https://youtu.be/eS77gFwXCPY](https://www.youtube.com/watch?v=CQIvu1EJshQ&t=5s&ab_channel=Luana)
I will walk you through the essential specifications for the project. This video aims to provide a concise overview of the required elements and guidelines, ensuring clarity on what is expected for the successful completion of the assignment.

## Technologies:
**Back-end:**

Python
Django

**Front-end:**

HTML (with Django templating)
CSS (with some Bootstrap Components)

## Project Summary:
**Entry Page:** Accessing /wiki/TITLE, where TITLE represents the title of an encyclopedia entry, should generate a page displaying the content of that specific entry.
The view should retrieve the content of the encyclopedia entry by invoking the appropriate utility function.
In the event an entry is requested but does not exist, the user should encounter an error page indicating that the requested page was not found.
Conversely, if the requested entry does exist, the user should be presented with a page showcasing the content of the entry, with the title of the page reflecting the name of the entry.

**Index Page:** Update index.html to enable users to click on any entry name, redirecting them directly to the corresponding entry page.

**Search Functionality:** Enable users to input a query into the search box in the sidebar to search for a specific encyclopedia entry.
If the query matches the name of an encyclopedia entry, the user should be directed to that entry’s page.
If the query does not match any existing encyclopedia entry, the user should be directed to a search results page displaying a list of all encyclopedia entries containing the query as a substring. For example, if the search query were "Py", then "Python" should appear in the search results.
Clicking on any entry name within the search results page should lead the user to that entry’s page.

**New Page Creation:** Clicking “Create New Page” in the sidebar should redirect the user to a page where they can author a new encyclopedia entry.
Users should be able to input a title for the page and, within a textarea, enter the Markdown content for the page.
A button should be provided for users to save their new page.
Upon saving the page, if an encyclopedia entry already exists with the provided title, the user should be presented with an error message.
Otherwise, the new encyclopedia entry should be saved, and the user should be directed to the page for the newly created entry.

**Edit Page:** Each entry page should include a link allowing users to navigate to a page where they can edit the Markdown content of that entry within a textarea.
The textarea should be pre-filled with the existing Markdown content of the page.
A button should be available for users to save the changes made to the entry.
After saving, the user should be redirected back to that entry’s page.

**Random Page:** Clicking “Random Page” in the sidebar should redirect the user to a randomly selected encyclopedia entry.
Markdown to HTML Conversion: Prior to displaying any entry page, any Markdown content within the entry file should be converted to HTML. The python-markdown2 package may be used for this purpose, which can be installed via pip3 install markdown2.


## Usage Instructions:
**Requirements:** Python(3) and the Python Package Installer (pip)

**Installation:** Install requirements (Django) using the command: 
```
pip install -r requirements.txt
```
Run the application locally: Execute the command: 
```
python manage.py runserver
```
