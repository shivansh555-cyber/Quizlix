# Process Flow / Workflow Diagram

## Overall flow

```mermaid
flowchart LR
    Start([Start]) --> Login[Login / Register]
    Login --> Role{Role?}
    Role -->|Student| SList[View Quiz List]
    Role -->|Admin| AManage[Manage Quizzes & Questions]
    SList --> Select[Select Quiz]
    Select --> LoadQ[Load Questions]
    LoadQ --> Attempt[Attempt Quiz]
    Attempt --> Submit[Submit Answers]
    Submit --> Evaluate[Evaluate & Score]
    Evaluate --> Save[Save Result]
    Save --> Display[Display Result / History]
    AManage --> ViewResults[View Summary / Export CSV]
```

## Student workflow

```
Login -> Student Menu -> View Quizzes -> Select Quiz ->
Answer Questions -> Submit -> Result -> History
```

## Admin workflow

```
Login -> Admin Menu -> Create/View/Delete Quiz ->
Manage Questions -> View Results Summary / Export CSV
```
