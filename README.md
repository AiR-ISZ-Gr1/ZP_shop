# Microservices architecture
## Implementation of a management, administration, and sales panel for an e-commerce store supported by a chatbot
## Table of Contents
  
  - [Installation](#installation)
  - [Usage](#usage)
  - [Important informations](#Important_informations)
  - [About](#about)
  - [Features](#features)
## Installation

For running aplication *Docker* is required.

1. Clone the repository:

2. Setup infrastructure:

    If on UNIX based system run:
    ```bash
    . start_compose.sh
    ```
    To shut down the aplication you should:
    ```bash
    . stop_compose.sh
    ```

   
    If on Windows open Docker Desktop as admin and Windows PowerShell as admin and run:
    ```bash
    ./start.bat
    ```
    To shut down the aplication you should:
    ```bash
    ./stop_compose.bat
    ```
  5. Wait till container `databases-startup` goes down.

  6. Everything is set up.

## Important informations
The Chatbot application is not working locally because it is based on the ChatGPT API. To run this, you need to add the API according to the instructions below:
1. Create .env file in `app/processes/chatbot`
2. In .env file create enviromental variable called OPENAI_API_KEY, and assign to it your [openai api key](https://openai.com/index/openai-api/)

Example file is provided `.env.example`.



## Usage

1. Open `localhost:8501` in your website
2. Log-in to test client `TestU` or test admin `TestA`, the password for both accounts is: !234qwert

## About
This project is a modern web application for an e-commerce flower shop, based on a microservices architecture. The aim of the project is to enable users to purchase various flower arrangements through a website, offering a wide range of products such as bouquets, potted plants, wreaths, and occasional arrangements. A key element of the application is the integrated chatbot, which acts as a virtual assistant, helping users choose products, providing advice and answers to questions about orders, and offering personalized recommendations using artificial intelligence algorithms.

## Features

- **User Interface (Frontend)**

Customer: Allows users to browse products, place orders, track transactions, and manage their profiles.
Admin: Provides access to advanced application management features, such as user management, product data editing, order processing, statistics analysis, and report generation.

- **Controllers**

Customer Panel Controller: Manages customer interactions, allowing profile viewing and editing, product recommendations, cart modifications, and purchase transactions.
Admin Panel Controller: Manages administrator interactions, allowing user, product, and order management.

- **Processes**

Product Recommendation: A recommendation system based on the analysis of order history and the user's current cart. The chatbot can also suggest products based on reviews and product descriptions.
Add Opinion: A module that allows adding reviews of purchased products and verifying whether a particular product was purchased by the user.
Order Products: A module that accepts customer orders, checks product availability, and processes orders while updating inventory.

- **Services**

Order Status Change: Allows administrators to update order statuses in response to various events.
User Authentication: The authentication process verifies the identity of users and assigns appropriate permissions.
Product Search: A tool for effectively finding products based on defined criteria.
LLM Services: Utilize advanced AI algorithms to interpret, analyze, and generate responses to natural language queries.

- **Database Interfaces (Database I/O)**

Manages and manipulates data across various databases, supporting requests related to product descriptions, customer reviews, user data, orders, and inventory statuses.

- **Architecture**

The project is based on a microservices architecture, ensuring flexibility and scalability. Each functionality of the store, such as the product catalog, payment system, or user management, is handled by a separate microservice. This allows for easy introduction of new features and scaling of the system as needed. Each microservice operates in an isolated Docker container, ensuring a consistent runtime environment and ease of deployment.
Technologies


