# Wiki Encyclopedia 📚
 
A Django-powered encyclopedia web app where users can browse, search, edit, and create entries written in markdown. *This project was developed as part of the Harvard CS50 Web Programming course.*
  
## Features ✨
 
 
- **Entry Page:**
 
 
  - Displays the contents of a Markdown entry converted to HTML.
 
  - Renders an error page if the requested entry doesn’t exist.
 
  - Includes an Edit button to update existing entries.
 

 
 
- **Index Page:**
 
 
  - Lists all encyclopedia entries.
 
  - Each title is a clickable link to the corresponding entry.
 

 
 
 
- **Search Functionality:**
 
 
  Sidebar search box that supports: 
 
    - Exact match redirect to the entry page.
 
    - Partial match results shown on a dedicated search results page, where clicking a result opens that entry.
 

 
 
 
- **Create New Page:**
 
 
  - Form for users to add a new entry with a title and Markdown content.
 
  - Shows an error if a new entry is submitted with a title that already exists.
 
  - Redirects to the new entry page upon successful save.
 

 
 
 
- **Edit Page:**
 
 
  - Pre-populated textarea with current Markdown content.
 
  - Allows users to modify and update the entry.
 
  - Redirects to updated entry after saving.
 

 
 
 
- **Random Page:**
 
 
  Instantly opens a randomly selected encyclopedia entry from the list.
 

 
 
 
- **Markdown to HTML Rendering:**
 
 
  - Converts Markdown to HTML using a custom parser (no external libraries).
 
  - Supports: 
 
    - Headings (`#` to `######`)
 
    - Bold text (`**text**`)
 
    - Unordered lists (`* item`)
 
    - Links (`[text](url)`)
 
    - Paragraphs
 

 
 

 
 

  
## Usage 🚀
 
 
1.  Run the development server: `python3 manage.py runserver ` 
 
2.  Navigate to `http://localhost:8000` to use the Wiki.
 
3.  Use the sidebar to navigate, search, or create entries.
 
4.  Click on any entry to read or edit its content.
 
 

  
## Technologies 🛠️
 
 
- Python 3
 
- Django
 
- HTML5

- CSS3

- Markdown (custom parser with RegEx)
 

  
## Notes ⚠️
 
 
- Markdown parsing does not rely on third-party packages like `markdown2`.
 
- The app is fully functional offline and does not require an external API.
 
- All content is stored in `.md` files in the `/entries` directory.
 

  
## Author 👩‍💻
 
**Shreya Raj** 
GitHub: [shreyax-r](https://github.com/shreyax-r) 
Email: rshreya2024@gmail.com
