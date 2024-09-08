# EasySearch - A simple and sophisticated search tool
![thumbnail](https://github.com/user-attachments/assets/eb112106-a2eb-4b10-8bbd-cc5f59992aa1)

[Click here to see a video about this work](https://youtu.be/yBqtIaDNA5k)


A simple and sophisticated search tool to help you get information fast and efficiently.

## Introduction
**EasySearch** is a AI-powered search tool designed to provide quick and accurate responses by utilizing several state-of-the-art APIs, such as **Wikipedia, Arxiv, DuckDuckGo, and Google Serper** for image search. The app uses **Groq's Large Language Model (LLM)** capabilities to interact with users in natural language, offering a streamlined search experience. The tool is built with **Streamlit** to provide a friendly user interface, allowing users to explore a variety of search queries with ease.

Whether you're searching for academic papers, general information, or images, EasySearch efficiently handles user queries, thanks to its integration with multiple tools and APIs.

## Documentation


This README file serves as the main documentation for the EasySearch project. For detailed API documentation, refer to the API Reference section below.
## Installation

Clone the repository:

```bash
  git clone https://github.com/Skrasool1197/EasySearch-LLM
```
Install the required dependencies:

```bash
  pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```
## API Reference




| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `groq_api_key` | `string` | **Required**. Your API key |
`serper_api_key` | `string`| **Required**. Your API key|

 






## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`GROQ_API_KEY`

`SERPER_API_KEY`



## Screenshots


- Home Page
![front](https://github.com/user-attachments/assets/3997df5c-d0b7-4852-a5fd-7b31b920e7f8)



- Chat Interface
![chat](https://github.com/user-attachments/assets/756e29ed-4b14-42ce-9a9d-3e436bc43ec8)


## Features

- **AI-powered Search:** Powered by Groq's Large Language Model (LLM), EasySearch can handle natural language input and provide detailed, relevant information.

- **Image Search Integration:** Uses Google Serper API to provide image results for your queries.

- **User-Friendly Interface:** The application is built with Streamlit, offering a seamless, chat-based interface where users can type their queries and receive responses.

- **Expandable for Multiple Use Cases:** EasySearch can be customized to use different LLM models, making it suitable for various purposes like academic research, general knowledge, and media searches.

- **Multimodal Query Support:**

 1)**Wikipedia:** Fetches concise and relevant information.
 
 2) **Arxiv:** Retrieves academic papers and research summaries.
  
 3) **DuckDuckGo:** Returns general web search results.






## Experimentation 
The versatility of EasySearch allows users to experiment with different types of queries. Below are a few example use cases:

- **General Information:** Ask questions like "What is quantum computing?" or "Who won the Nobel Prize in Physics in 2023?" and get concise answers from Wikipedia and DuckDuckGo.

- **Academic Research:** Queries such as "Explain Reinforcement Learning" or "Latest research on Neural Networks" will return summaries from Arxiv.

- **Image Search:** Users can search for images related to their queries, for instance, "Images of quantum circuits" or "Photos of the Milky Way Galaxy."

The app uses advanced language models to process and understand these queries, ensuring accuracy and relevance.
## Conclusion
**EasySearch** is a flexible, efficient, and user-friendly tool that brings together multiple sources of information under one platform. With its AI-powered natural language understanding and integration with powerful APIs, EasySearch helps users find relevant text and image data effortlessly.

**I hope you find this project useful and look forward to your contributions and feedback!**
