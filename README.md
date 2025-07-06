# Gantt Chart Generator

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)](https://github.com)

A comprehensive and user-friendly Gantt chart generator that creates professional HTML diagrams from JSON configurations. Perfect for project management, planning, and timeline visualization.

## 🌟 Features

- **Interactive Configuration**: Step-by-step wizard for easy setup
- **Flexible Templates**: Modern, responsive HTML templates
- **Multiple Project Types**: Support for various timeline formats
- **Configuration Extraction**: Reverse-engineer existing charts
- **Multi-language Support**: English and French interfaces
- **Export Ready**: Professional HTML output with TailwindCSS styling

## 🚀 Quick Start

> **Note**: This version (2.0+) includes important fixes for rendering Gantt charts, including correct positioning of multi-period tasks and improved milestone display.

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/gantt-chart-generator.git
cd gantt-chart-generator

# Install dependencies (automatic on first run)
python src/gantt_generator.py
```

### Windows Users

```bat
# Launch the main menu
scripts\generate_gantt.bat

# Or extract from existing HTML
scripts\extract_config.bat
```

### Direct Python Usage

```bash
# Interactive generator
python src/gantt_generator.py

# Extract from HTML file
python src/gantt_extractor.py examples/sample_project.html

# Run tests
python src/test_extractor.py
```

## 📊 Project Structure

```
gantt-chart-generator/
├── 📁 src/                     # Core Python modules
│   ├── gantt_generator.py      # Main generator
│   ├── gantt_extractor.py      # Configuration extractor
│   └── gantt_generator.py      # Main generator module
├── 📁 templates/               # HTML templates
│   ├── gantt-template.html     # Full-featured template
│   └── simple_template.html    # Minimal template
├── 📁 examples/                # Sample configurations
│   ├── basic_project.json      # Simple project example
│   └── styling_example.json    # Advanced styling example
├── 📁 scripts/                 # Utility scripts
│   ├── generate_gantt.bat      # Windows generator launcher
│   └── extract_config.bat      # Windows extractor launcher
├── 📁 docs/                    # Documentation
│   └── user_guide.md           # Complete user guide
├── 📁 locale/                  # Language files
│   ├── en.json                 # English translations
│   └── fr.json                 # French translations
└── requirements.txt            # Python dependencies
```

## 🎯 Use Cases

### 📈 Project Management

- Development roadmaps
- Release planning
- Resource allocation
- Milestone tracking

### 💼 Business Planning

- Strategic initiatives
- Marketing campaigns
- Budget planning
- Team coordination

### 🚀 Software Development

- Sprint planning
- Feature development
- Testing phases
- Deployment schedules

## 📋 Supported Timeline Types

### Row Types

- **Simple**: Basic task bars with custom styling
- **Milestones**: Tasks with milestone markers
- **Special**: Floating elements and indicators

### Period Types

- **Months**: M1, M2, ..., M24 (default)
- **Weeks**: W1, W2, ..., W52
- **Quarters**: Q1, Q2, Q3, Q4
- **Custom**: User-defined labels

### Styling Options

- **Phases**: Multi-colored project phases
- **Tasks**: Primary, secondary, success styles
- **Milestones**: Diamond markers with labels

## 🔄 Typical Workflows

### 1. Create New Project

```
1. Run the generator script
2. Choose "Create new diagram"
3. Follow the interactive wizard
4. Configure periods, rows, and tasks
5. Generate and view HTML output
```

### 2. Modify Existing Project

```
1. Run the extractor on existing HTML
2. Edit the extracted JSON configuration
3. Regenerate the updated diagram
4. Compare and refine as needed
```

### 3. Template Customization

```
1. Copy the base template
2. Modify CSS styles and colors
3. Test with sample configurations
4. Deploy your custom template
```

## 🛠️ Configuration Format

```json
{
  "title": "My Project Timeline",
  "subtitle": "Development roadmap",
  "periods": 12,
  "period_type": "months",
  "period_labels": ["Jan", "Feb", "Mar", "..."],
  "rows": [
    {
      "name": "Development Phase",
      "type": "milestones",
      "tasks": [
        {
          "name": "Core Features",
          "start": 1,
          "duration": 3,
          "style": "phase-1"
        }
      ],
      "milestones": [
        {
          "name": "MVP Release",
          "position": 4,
          "style": "milestone-major"
        }
      ]
    }
  ]
}
```

## 🌐 Multi-language Support

The generator supports multiple languages for the interface:

```bash
# English (default)
python src/gantt_generator.py --lang en

# French
python src/gantt_generator.py --lang fr
```

## 🎨 Customization

### Custom Styles

```css
/* Add to template CSS */
.custom-phase {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
}
```

### Custom Period Types

```json
{
  "period_type": "custom",
  "period_labels": ["Phase 1", "Phase 2", "Testing", "Launch"]
}
```

## 📚 Documentation

- **[Complete User Guide](docs/user_guide.md)**: Comprehensive documentation covering all features, configuration, styling, extraction, CLI usage, troubleshooting, and best practices
- **[Examples](examples/)**: Sample configurations and ready-to-use templates
- **[Contributing Guide](CONTRIBUTING.md)**: How to contribute to the project

## 🧪 Testing

```bash
# Run the test suite
python src/test_extractor.py

# Test with sample files
python src/gantt_extractor.py examples/sample_charts/basic_project.html
```

## 🤝 Contributing

We welcome contributions! Please see our contributing guidelines:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

### Development Setup

```bash
# Clone and setup
git clone https://github.com/your-username/gantt-chart-generator.git
cd gantt-chart-generator

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest src/tests/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with modern web standards (HTML5, CSS3, TailwindCSS)
- Inspired by project management best practices
- Community-driven development and feedback

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/your-username/gantt-chart-generator/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-username/gantt-chart-generator/discussions)
- **Documentation**: [Wiki](https://github.com/your-username/gantt-chart-generator/wiki)

---

*Professional Gantt chart generation made simple. Perfect for project managers, developers, and anyone who needs clear timeline visualization.*

**Available Languages**: **English** | [Français](README_fr.md)
