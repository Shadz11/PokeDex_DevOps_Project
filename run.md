# Pokédex Project - Run Instructions

## 🚀 Quick Start Guide

### Prerequisites
- **Docker** (recommended) or **Python 3.11+**
- **Git** for cloning the repository
- **Make** (optional, for using Makefile commands)

### Option 1: Docker (Recommended) 🐳

#### Quick Start with Docker Compose
```bash
# 1. Clone the repository
git clone <your-repository-url>
cd pokemon-pokedex-project

# 2. Start the application
docker-compose up -d

# 3. Access the application
# Open http://localhost:8000/pokemon/ in your browser
```

#### Using Makefile Commands
```bash
# Build and start
make up

# View logs
make logs

# Stop the application
make down

# Clean up Docker resources
make clean
```

#### Manual Docker Commands
```bash
# Build the Docker image
docker build -t pokedex-app .

# Run the container
docker run -d --name pokedex-local -p 8000:8000 pokedex-app

# Check container status
docker ps

# View logs
docker logs pokedex-local

# Stop and remove container
docker stop pokedex-local
docker rm pokedex-local
```

### Option 2: Local Development 💻

#### Setup Local Environment
```bash
# 1. Clone the repository
git clone <your-repository-url>
cd pokemon-pokedex-project

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run migrations
python manage.py migrate

# 6. Start development server
python manage.py runserver
```

#### Using Makefile Commands
```bash
# Install dependencies
make install

# Run migrations
make migrate

# Start development server
make run

# Run tests
make test

# Check Django configuration
make check
```

## 🧪 Testing the Application

### Manual Testing
1. **Main Page**: Visit `http://localhost:8000/pokemon/`
   - Should display all 151 Pokémon in a grid layout
   - Each Pokémon should have an image, ID, and name

2. **Search Functionality**: 
   - Try searching for "pikachu" (by name)
   - Try searching for "25" (by ID - also Pikachu)
   - Try searching for "charizard" (by name)
   - Try searching for "99999" (invalid ID - should show error)

3. **Individual Pokémon Pages**:
   - Click on any Pokémon card
   - Should display detailed information including:
     - Stats (HP, Attack, Defense, etc.)
     - Types (with colored tags)
     - Abilities
     - Height and weight

### Automated Testing
```bash
# Run all tests
make test

# Run specific test file
python manage.py test pokemon.tests

# Run with verbose output
python manage.py test pokemon.tests -v 2
```

### Docker Testing
```bash
# Test Docker image locally
make docker-test

# Test production build
make production-build
make production-run
```

## 🔧 Development Commands

### Django Management
```bash
# Create superuser (if needed)
python manage.py createsuperuser

# Open Django shell
make shell

# Collect static files
make collectstatic

# Check deployment configuration
make check
```

### Docker Operations
```bash
# Build development image
make build

# Build production image
make production-build

# View container logs
make logs

# Clean up Docker resources
make clean
```

### Git Operations
```bash
# Check status
git status

# Add all changes
git add .

# Commit changes
git commit -m "Your commit message"

# Push to repository
git push origin master
```

## 🌐 Accessing the Application

### Local Development
- **Main Page**: http://localhost:8000/pokemon/
- **Admin Panel**: http://localhost:8000/admin/ (if superuser created)

### Docker Deployment
- **Main Page**: http://localhost:8000/pokemon/
- **Health Check**: http://localhost:8000/pokemon/ (should return 200 OK)

### Production Deployment
- **Main Page**: http://your-domain.com/pokemon/
- **Health Check**: http://your-domain.com/pokemon/

## 🔍 Troubleshooting

### Common Issues

#### 1. Port Already in Use
```bash
# Check what's using port 8000
lsof -i :8000

# Use different port
python manage.py runserver 8001
# or
docker run -p 8001:8000 pokedex-app
```

#### 2. Docker Build Issues
```bash
# Clean Docker cache
docker system prune -a

# Rebuild without cache
docker build --no-cache -t pokedex-app .
```

#### 3. Database Issues
```bash
# Reset database
rm db.sqlite3
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

#### 4. Static Files Issues
```bash
# Collect static files
python manage.py collectstatic --noinput

# Check static files configuration
python manage.py check --deploy
```

#### 5. PokeAPI Issues
```bash
# Test PokeAPI connectivity
curl -I https://pokeapi.co/api/v2/pokemon/pikachu/

# Check application logs
docker logs pokemon-pokedex-project-pokedex-app-1
```

### Performance Optimization

#### Docker Optimization
```bash
# Use multi-stage builds (for production)
docker build --target production -t pokedex-app:prod .

# Optimize image size
docker build --no-cache --compress -t pokedex-app:optimized .
```

#### Django Optimization
```bash
# Enable debug toolbar (development only)
pip install django-debug-toolbar

# Profile database queries
python manage.py shell
from django.db import connection
# ... run your code ...
print(connection.queries)
```

## 📊 Monitoring & Logs

### View Application Logs
```bash
# Docker logs
docker logs pokemon-pokedex-project-pokedex-app-1

# Follow logs in real-time
docker logs -f pokemon-pokedex-project-pokedex-app-1

# View last 50 lines
docker logs --tail 50 pokemon-pokedex-project-pokedex-app-1
```

### Health Checks
```bash
# Test application health
curl -I http://localhost:8000/pokemon/

# Test specific Pokémon
curl -I http://localhost:8000/pokemon/pikachu/

# Test error handling
curl -I http://localhost:8000/pokemon/invalid-pokemon/
```

### Performance Monitoring
```bash
# Check container resource usage
docker stats pokemon-pokedex-project-pokedex-app-1

# Monitor network connections
netstat -tulpn | grep 8000
```

## 🚀 Production Deployment

### Environment Variables
```bash
# Set production environment
export DEBUG=False
export DJANGO_SETTINGS_MODULE=pokedex_project.production

# Or use .env file
echo "DEBUG=False" > .env
echo "DJANGO_SETTINGS_MODULE=pokedex_project.production" >> .env
```

### Production Commands
```bash
# Build production image
make production-build

# Run production container
make production-run

# Deploy with Docker Compose (production)
docker-compose -f docker-compose.prod.yml up -d
```

### Security Checklist
- [ ] DEBUG=False in production
- [ ] ALLOWED_HOSTS configured
- [ ] SECRET_KEY is secure
- [ ] HTTPS enabled
- [ ] Security headers configured
- [ ] Database credentials secured

## 📝 Useful Commands Reference

### Makefile Commands
```bash
make help          # Show all available commands
make install       # Install Python dependencies
make test          # Run Django tests
make run           # Start development server
make build         # Build Docker image
make up            # Start with Docker Compose
make down          # Stop Docker Compose
make logs          # View application logs
make clean         # Clean up Docker resources
make migrate       # Run Django migrations
make collectstatic # Collect static files
make shell         # Open Django shell
make check         # Check Django configuration
make docker-test   # Test Docker image locally
make production-build  # Build production image
make production-run    # Run production image
```

### Docker Commands
```bash
docker build -t pokedex-app .                    # Build image
docker run -d -p 8000:8000 pokedex-app          # Run container
docker ps                                        # List containers
docker logs <container_id>                       # View logs
docker stop <container_id>                       # Stop container
docker rm <container_id>                         # Remove container
docker system prune -a                           # Clean up
```

### Django Commands
```bash
python manage.py runserver                       # Start dev server
python manage.py test                            # Run tests
python manage.py migrate                         # Run migrations
python manage.py collectstatic                   # Collect static files
python manage.py shell                           # Open shell
python manage.py check --deploy                  # Check deployment
python manage.py createsuperuser                 # Create admin user
```

---

**Last Updated**: December 2024  
**Application Status**: Production Ready  
**Next Steps**: See [blog.md](blog.md) for development roadmap
