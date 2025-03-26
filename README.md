# AI-Powered Search Engine Chatbot

This project is a **Streamlit-based AI chatbot** that enables users to **search the web using DuckDuckGo, Wikipedia, and Arxiv** while leveraging **Groq's Mixtral-8x7B model** for intelligent responses.

## Features

- **Real-time Web Search**: Fetches relevant results from DuckDuckGo.
- **Wikipedia & Arxiv Integration**: Retrieves articles and papers for enhanced information.
- **Conversational Memory**: Maintains chat history for a seamless search experience.
- **Groq LLM Integration**: Uses **Mixtral-8x7B** for natural language understanding and response generation.
- **Interactive Chat UI**: Built with **Streamlit** for an intuitive user experience.

## Tech Stack

- **Python**
- **Streamlit**
- **LangChain**
- **Groq (Mixtral-8x7B model)**
- **DuckDuckGoSearchResults API**
- **WikipediaAPIWrapper**
- **ArxivAPIWrapper**

## Installation

### Prerequisites

- Python 3.8+
- Groq API Key

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/PrinceGupta8/Search-engine-with-langchain-Tools-and-agents.git
   cd Search-engine-with-langchain-Tools-and-agents
   ```
2. **Create a virtual environment**
   ```bash
   python -m venv venv
   svenv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the application**
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Enter your Groq API Key** in the Streamlit input box.
2. **Ask a search query** (e.g., "What is Quantum Computing?").
3. **The chatbot fetches results** from Wikipedia, Arxiv, and DuckDuckGo.
4. **AI-generated responses** are displayed using Groq’s LLM.

## Example

**Input:**

```
What are the latest advancements in AI?
```

**Output:**

```
1. DuckDuckGo: "Recent breakthroughs in AI include..."
2. Wikipedia: "AI has evolved significantly with..."
3. Arxiv: "A recent paper discusses...
```

## API Keys

- Get your **Groq API Key** from [Groq](https://groq.com/).
- Set it as an environment variable (`groq_api_key`) or input it in the Streamlit UI.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.

---

**Experience AI-powered real-time search with conversational memory!**

