# Pokédex Project

A modern web application that displays Pokémon information using the PokeAPI. Built with Django, containerized with Docker, and deployed with CI/CD automation.

## 🚀 Quick Start

### Prerequisites
- **Docker** (recommended) or **Python 3.11+**
- **Git**

### Run with Docker (Recommended)
```bash
git clone <repository-url>
cd pokemon-pokedex-project
docker-compose up -d
# Open http://localhost:8000/pokemon/
```

### Run Locally
```bash
git clone <repository-url>
cd pokemon-pokedex-project
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
# Open http://localhost:8000/pokemon/
```

## 📋 Features

- **Pokédex Listing**: Browse all 151 original Pokémon with images and basic info
- **Search**: Find Pokémon by name or ID (case-insensitive)
- **Detailed View**: Complete stats, types, abilities, height (cm), weight (kg)
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Real-time Data**: Fetches live data from PokeAPI

## 🛠️ Development

### Available Commands
```bash
make help          # Show all commands
make test          # Run tests
make up            # Start with Docker
make down          # Stop Docker
make logs          # View logs
make clean         # Clean Docker resources
```

### Project Structure
```
pokemon-pokedex-project/
├── pokedex_project/     # Django project settings
├── pokemon/            # Main app with views, templates
├── requirements.txt    # Python dependencies
├── Dockerfile         # Container configuration
├── docker-compose.yml # Local development setup
├── Makefile          # Development commands
└── .github/          # CI/CD workflows
```

## 🧪 Testing

```bash
# Run all tests
make test

# Test Docker image
make docker-test

# Check configuration
make check
```

## 📚 Documentation

- **[blog.md](blog.md)** - Detailed development journey and technical decisions
- **[run.md](run.md)** - Comprehensive setup and troubleshooting guide
- **[Dockerfile](Dockerfile)** - Container configuration
- **[.github/workflows/ci.yml](.github/workflows/ci.yml)** - CI/CD pipeline

## 🔧 Technology Stack

- **Backend**: Django 5.2.4, Python 3.11
- **Frontend**: Django Templates, CSS Grid
- **API**: PokeAPI (https://pokeapi.co/)
- **Container**: Docker, Gunicorn
- **CI/CD**: GitHub Actions
- **Database**: SQLite (dev), PostgreSQL (prod planned)

## 📈 Project Status

- ✅ **Phase 1**: Application Development (Complete)
- ✅ **Phase 2**: Containerization & CI/CD (Complete)
- 📋 **Phase 3**: Cloud Deployment & Monitoring (Planned)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests: `make test`
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**For detailed development history and technical insights, see [blog.md](blog.md)**
