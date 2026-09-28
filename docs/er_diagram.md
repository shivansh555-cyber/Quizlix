# ER Diagram / Data Design

Quizlix stores data as JSON files rather than SQL tables, but the same
relationships apply. Each JSON file below acts like one "table".

```mermaid
erDiagram
    USER ||--o{ RESULT : attempts
    QUIZ ||--o{ QUESTION : contains
    QUIZ ||--o{ RESULT : "produces"

    USER {
        string username PK
        string password
        string role
    }
    QUIZ {
        int quiz_id PK
        string title
        string category
    }
    QUESTION {
        int question_id PK
        int quiz_id FK
        string question
        string options
        string answer
        string difficulty
    }
    RESULT {
        string username FK
        int quiz_id FK
        string quiz_title
        int score
        int total
        float percentage
        string timestamp
    }
```

**Files:** `data/users.json` → USER, `data/quizzes.json` → QUIZ (with an
embedded list of question IDs), `data/questions.json` → QUESTION,
`data/results.json` → RESULT.
