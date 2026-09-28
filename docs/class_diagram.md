# Class / Component Diagram

Quizlix is written with plain functions and dictionaries rather than
custom classes (to match the beginner-level, function-based syllabus),
so this diagram shows the main **data records** (their fields) and which
**module** owns each one, which plays the same role a class diagram would
in an object-oriented design.

```mermaid
classDiagram
    class User {
        +string username
        +string password
        +string role
    }
    class Quiz {
        +int quiz_id
        +string title
        +string category
        +list~int~ questions
    }
    class Question {
        +int question_id
        +int quiz_id
        +string question
        +list~string~ options
        +string answer
        +string difficulty
    }
    class Result {
        +string username
        +int quiz_id
        +string quiz_title
        +int score
        +int total
        +float percentage
        +string timestamp
    }

    User "1" --> "many" Result : attempts
    Quiz "1" --> "many" Question : contains
    Quiz "1" --> "many" Result : produces
```
