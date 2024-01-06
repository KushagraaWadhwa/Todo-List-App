
TODOASTIC - Your Fantastic Kanban App

Welcome to TODOASTIC, a simple and intuitive Kanban app designed to keep you organized on the go. Here's a brief overview:

Features:

User-Friendly Homepage: Log in, and a beautiful welcome message guides you to the main page.
Task Management: Add tasks via a form, neatly displayed in a table with creation timestamps.
Task Actions: Each task comes with buttons for Update, Delete, and Mark as Completed.
Technologies Used:

Flask (with SQL Alchemy) for the backend.
Jinja2 templates + Bootstrap for HTML and styling.
SQLite for data storage.
Database Schema:

Columns: SNo (Primary key), Title, Description, Created at.
APIs:

Update, delete, and check progress of tasks.
Architecture:

Main folders: templates, static, scripts.
templates: 7 HTML files using Jinja templates, including a base HTML.
static: Contains the website's brand logo.
scripts: app.py for main functionality.
test.db for data storage.
Configuration in YAML files
