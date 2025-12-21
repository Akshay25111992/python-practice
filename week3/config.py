# Database Configuration
# Update these values according to your database setup

DATABASE_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "fastapi_db",
    "username": "postgres",
    "password": "password"
}

# For PostgreSQL
DATABASE_URL = f"postgresql://{DATABASE_CONFIG['username']}:{DATABASE_CONFIG['password']}@{DATABASE_CONFIG['host']}:{DATABASE_CONFIG['port']}/{DATABASE_CONFIG['database']}"

# For MySQL (uncomment if using MySQL instead)
# DATABASE_URL = f"mysql+pymysql://{DATABASE_CONFIG['username']}:{DATABASE_CONFIG['password']}@{DATABASE_CONFIG['host']}:{DATABASE_CONFIG['port']}/{DATABASE_CONFIG['database']}"

# JWT Configuration
SECRET_KEY = "your-secret-key-change-this-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

