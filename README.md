# Cocktail Chatbot

### 2021/22 WS Text Technology Final Project
##### Created by Chih-Yi Lin, Kuan-Yu Lin and Tzu-Ju Lin

### Project Idea
We would like to build a chatbot that is able to recommend a suitable cocktail for users who are not sure what they want.
After a few questions, the chatbat will then return a cocktail recepie that is chosen base on the users' input.

### Workflow
* Collect : Plain text from online cocktail recipes
* Prepare: 
  * Phase 1 - Encode the text data to XML file and XML schema
  * Phase 2 - Import the XML into a database
* Access: A chatbot that asks users’ preferences ( taste, base, hashtags, juice, syrup) and access the database with SQL queries created based on users’ input.



### Files included
  * cocktails.xml: xml file for cocktail recipes
  * xml_schema.xml: xml schema for validating cocktails.xml
  * XMLtoDB.py: Python code for extracting and inserting xml data into database
  * cocktail_db.sql: The database of cocktail recipes
  * cocktail.py: Python code for the chatbot using loops and SQL queries
