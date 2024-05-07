# Wiki Encyclopedia with Django

This repository contains a Django-based Wiki Encyclopedia application, designed to allow users to create, search, and view encyclopedia entries using HTML, CSS, Python, and Django.

## Overview

The application leverages Django's powerful backend features to manage encyclopedia entries stored as Markdown files. The project includes a set of pre-created encyclopedia entries and the functionality to add, edit, and search entries dynamically.

## Features

- **Entry Page:** Access encyclopedia entries by navigating to `/wiki/TITLE`, where `TITLE` is the title of the entry. If the entry exists, its content is displayed; otherwise, a not found error page is shown.
- **Index Page:** The main page lists all encyclopedia entries, which are clickable and direct the user to the specific entry page.
- **Search Functionality:** Includes a search box that filters entries based on user queries. If the query matches an entry's name exactly, the user is directed to that entry's page. Otherwise, a search results page shows all entries that partially match the query.
- **Create New Page:** Users can create new encyclopedia entries using a simple form that accepts Markdown content. The application checks for duplicate titles and alerts the user if an entry already exists.
- **Edit Page:** Each entry can be edited by navigating to a specific edit page where users can modify the Markdown content.
- **Random Page:** A feature to navigate randomly to any encyclopedia entry, enhancing user exploration.
- **Markdown to HTML Conversion:** Implements markdown2 library for converting Markdown content to HTML, ensuring content is web-friendly and styled appropriately.

## Technologies Used

- **Django:** A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Python:** Used for backend logic and utilities, including file handling and text processing.
- **HTML/CSS:** For structuring and styling the web interface.
- **Markdown2:** A Python library used to convert Markdown files to HTML.

## Setup and Installation

To run this project locally:
1. Clone this repository.
2. Ensure Python and Django are installed.
3. Navigate to the project directory and run `python manage.py runserver` to start the Django development server.
4. Open your web browser and go to `http://127.0.0.1:8000` to view the application.

## Contribution

Contributions to this project are welcome.
