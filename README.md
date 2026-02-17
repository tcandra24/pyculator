# Numerra

Numerra is a modular and extensible CLI calculator built using clean
architecture principles.\
It is designed not only to perform arithmetic operations, but also to
demonstrate structured backend development practices in Python.

Numerra focuses on maintainability, modularity, and production-ready
packaging.

---

## ✨ Features

- Basic arithmetic operations (addition, subtraction, multiplication,
  division)
- Enum-based operator handling
- Persistent calculation history (JSON storage)
- Clear history functionality
- Configurable decimal precision
- Structured logging system
- Modular project architecture
- Unit tested with `pytest`
- Installable via pip
- CLI entry point support

---

## 📦 Installation

### From PyPI

```bash
pip install numerra
```

### Development Mode

```bash
git clone https://github.com/tcandra24/numerra.git
cd numerra
pip install -e .
```

---

## 🚀 Usage

### Run as Installed CLI

```bash
numerra
```

### Run in Development

```bash
python -m numerra
```

### Check Version

```bash
numerra --version
```

---

## 🏗 Project Structure

    numerra/
    ├── config/
    ├── core/
    ├── data/
    ├── enums/
    ├── logs/
    ├── models/
    ├── utilities/
    └── main.py

The project follows a modular structure with separation of concerns
between:

- Core business logic
- Data persistence
- Configuration
- Logging
- Utilities
- CLI interface

---

## ⚙ Configuration

Numerra uses a JSON-based configuration system.

Configurable options include:

- Logging behavior
- Runtime settings

Configuration is loaded before business logic execution to ensure
consistent behavior.

---

## 🧪 Running Tests

```bash
pytest
```

Unit tests cover:

- Arithmetic operations
- History management
- Core calculator logic

---

## 🔄 CI/CD

Numerra supports automated publishing to PyPI via GitHub Actions.\
Releases are triggered using semantic version tags.

Example:

```bash
git tag v0.2.0
git push origin v0.2.0
```

---

## 📄 License

MIT License
