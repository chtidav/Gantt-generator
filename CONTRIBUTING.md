# Contributing to Gantt Chart Generator

We welcome contributions to the Gantt Chart Generator! This document provides guidelines for contributing to the project.

## 🤝 How to Contribute

### Reporting Issues

1. **Search existing issues** first to avoid duplicates
2. **Use the issue template** when creating new issues
3. **Provide detailed information** including:
   - Operating system and Python version
   - Steps to reproduce the problem
   - Expected vs actual behavior
   - Screenshots if applicable

### Suggesting Features

1. **Check the roadmap** in the main README
2. **Open a feature request** with:
   - Clear description of the feature
   - Use cases and benefits
   - Possible implementation approach

### Contributing Code

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/your-feature-name`
3. **Make your changes** following our coding standards
4. **Test your changes** thoroughly
5. **Commit with clear messages**
6. **Submit a pull request**

## 🛠️ Development Setup

### Prerequisites

- Python 3.7 or higher
- Git
- Text editor or IDE

### Setup Steps

```bash
# Clone your fork
git clone https://github.com/your-username/gantt-chart-generator.git
cd gantt-chart-generator

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
python src/test_extractor.py
```

## 📝 Coding Standards

### Python Code Style

- Follow **PEP 8** style guidelines
- Use **meaningful variable names**
- Add **docstrings** for functions and classes
- Keep **functions focused** and small
- Handle **errors gracefully**

### Example:

```python
def generate_gantt_chart(config: Dict[str, Any], output_file: str) -> bool:
    """
    Generate HTML Gantt chart from configuration.
    
    Args:
        config: Dictionary containing chart configuration
        output_file: Path where HTML file will be saved
        
    Returns:
        bool: True if generation successful, False otherwise
    """
    try:
        # Implementation here
        return True
    except Exception as e:
        logging.error(f"Failed to generate chart: {e}")
        return False
```

### Documentation

- Update **README.md** for significant changes
- Add **examples** for new features
- Update **user guide** when needed
- Include **comments** for complex logic

### Commit Messages

Use clear, descriptive commit messages:

```
feat: add quarterly period type support
fix: resolve template loading issue on Windows
docs: update configuration examples
test: add unit tests for extractor module
```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
python src/test_extractor.py

# Test specific functionality
python src/gantt_extractor.py examples/basic_project.html
```

### Adding Tests

When adding new features:

1. **Add test cases** for new functionality
2. **Test edge cases** and error conditions
3. **Verify backwards compatibility**
4. **Test on different platforms** if possible

## 📁 Project Structure

```
gantt-chart-generator/
├── src/                    # Core Python modules
├── templates/              # HTML templates
├── examples/               # Sample configurations
├── docs/                   # Documentation
├── locale/                 # Language files
├── scripts/                # Utility scripts
└── requirements.txt        # Dependencies
```

## 🌍 Internationalization

### Adding New Languages

1. **Create language file**: `locale/xx.json` (where xx is language code)
2. **Translate all strings** from `locale/en.json`
3. **Test the interface** in the new language
4. **Update documentation** to mention new language support

### Translation Guidelines

- Keep **technical terms** consistent
- Maintain **same structure** as English file
- Consider **cultural differences** in formatting
- Test **UI layout** with longer translations

## 📋 Pull Request Guidelines

### Before Submitting

- [ ] Code follows project style guidelines
- [ ] All tests pass
- [ ] Documentation is updated
- [ ] Commit messages are clear
- [ ] No merge conflicts

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Testing
- [ ] All existing tests pass
- [ ] New tests added for new functionality
- [ ] Tested on multiple platforms

## Screenshots (if applicable)
Add screenshots for UI changes
```

## 🚀 Release Process

### Version Numbering

We use **Semantic Versioning** (SemVer):
- **MAJOR**: Breaking changes
- **MINOR**: New features (backwards compatible)
- **PATCH**: Bug fixes

### Release Checklist

- [ ] All tests pass
- [ ] Documentation updated
- [ ] Version number bumped
- [ ] Release notes prepared
- [ ] Examples verified

## 💡 Ideas for Contributions

### Easy First Contributions

- **Fix typos** in documentation
- **Add example configurations**
- **Improve error messages**
- **Add unit tests**
- **Translate interface**

### Advanced Contributions

- **New chart types** (e.g., resource allocation)
- **Export formats** (PDF, PNG, SVG)
- **API integration** (REST endpoints)
- **Performance optimizations**
- **Advanced styling options**

### New Features Ideas

- **Dependency management** between tasks
- **Resource allocation** visualization
- **Time tracking** integration
- **Collaboration features**
- **Template marketplace**

## 📞 Getting Help

### Communication Channels

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General questions and ideas
- **Pull Requests**: Code review and feedback

### Response Times

- **Bug reports**: We aim to respond within 48 hours
- **Feature requests**: Initial response within a week
- **Pull requests**: Review within 3-5 business days

## 🏆 Recognition

Contributors will be:
- **Listed in README.md** acknowledgments
- **Tagged in release notes** for significant contributions
- **Invited as maintainers** for ongoing contributions

Thank you for contributing to making Gantt Chart Generator better for everyone! 🎉
