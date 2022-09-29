# Flask App for signup and signin

### Initialise Application
```flask init_app```

### Run the Application
```flask run```

### Table Structure (`users`)
| Column  | Type|
| ------------- | ------------- |
| `id`  | `INTEGER PRIMARY KEY AUTOINCREMENT` |
| `username`  | `TEXT NOT NULL`  |
| `password`  | `TEXT NOT NULL`  |


`SQLite` is used for the database.
`SHA 384` algorithm is used for hashing passwords
`uuid4` is used for generating the secret key
