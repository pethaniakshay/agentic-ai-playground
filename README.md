# My CrewAI Project

This project demonstrates the use of CrewAI for multi-agent systems to research and write articles.

## Setup

1.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set your OpenAI API Key:**
    *   **Option A (Recommended):** Set an environment variable named `OPENAI_API_KEY` with your actual key.
    *   **Option B:** Open `src/my_project_name/utils.py` and replace `"YOUR_OPENAI_API_KEY"` with your actual key.

## Running the Application

To run the main application for Lesson 2:

```bash
python src/crewai_lessons/l2_article_writer/main.py
```

## Project Structure

```
.
├── .gitignore
├── README.md
├── requirements.txt
├── pyproject.toml
├── src/
│   └── crewai_lessons/
│       ├── __init__.py
│       └── l2_article_writer/
│           ├── __init__.py
│           ├── main.py
│           └── utils.py
│   └── notebooks/
│       └── L2_research_write_article.ipynb
└── tests/
    └── test_placeholder.py
```
