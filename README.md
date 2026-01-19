# Books Read - RAG Application

A Retrieval-Augmented Generation (RAG) application that allows you to query and get answers from book texts using OpenAI's language models and embeddings.

## Setup

### 1. Get an OpenAI API Key

1. Sign up for an account at [OpenAI](https://platform.openai.com/)
2. Navigate to the API keys section and create a new API key

### 2. Configure Environment Variables

Create a `.env` file in the root directory of the project and add your OpenAI API key:

```
OPENAI_API_KEY="your-openai-api-key"
```

**Note:** Make sure to add `.env` to your `.gitignore` file to keep your API key secure.

### 3. Create a Virtual Environment

Create a virtual environment to isolate the project dependencies:

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

### 5. Install Dependencies

Install the required packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 6. Add Your Book Text

Open `main.py` and pass in any text you want into the `book` variable (or create a new variable for your book text).

## Running the Application

Once everything is set up, run the application:

```bash
python main.py
```

The application will:
1. Process the book text(s) you've provided
2. Split them into chunks
3. Create embeddings and store them in a vector store
4. Perform a similarity search based on the query
5. Generate an answer using the relevant book excerpts

## How It Works

This application uses:
- **LangChain** for orchestration
- **OpenAI GPT-4o** for generating answers
- **OpenAI text-embedding-3-large** for creating embeddings
- **InMemoryVectorStore** for storing and searching embeddings
- **RecursiveCharacterTextSplitter** for splitting text into manageable chunks

You can modify the query in `main.py` to ask different questions about your book content.
