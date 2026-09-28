# System Architecture Diagram

Quizlix follows a simple layered / top-down design: the user interacts
only with the menu layer, which calls logic modules, which in turn go
through a single data-access layer to reach the JSON files.

```mermaid
flowchart TD
    U[User: Student / Admin] --> M[menu.py<br/>Text Menus]
    M --> A[auth.py]
    M --> QM[quiz_manager.py]
    M --> QB[question_bank.py]
    M --> QE[quiz_engine.py]
    M --> RM[result_manager.py]
    M --> RP[reporting.py]

    A --> D[data_manager.py]
    QM --> D
    QB --> D
    RM --> D
    RP --> RM
    RP --> QM

    QE --> QB
    A --> V[validators.py]
    QM --> V
    QB --> V

    D --> J[(JSON files in data/)]
```

**Why this shape?** Only `data_manager.py` touches the file system, so if
storage ever changed (e.g. to a real database) only one file would need
to change. `validators.py` is shared by every module that creates or
edits data, keeping validation rules consistent everywhere.
