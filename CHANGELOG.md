# Changelog

All notable changes to the Gantt Chart Generator project will be documented in this file.

## [2.1.1] - 2024-12-30 🎨 STYLE IMPROVEMENTS

### 🎨 Visual Enhancements
- **Improved milestone positioning**: Moved milestone diamonds lower in cells (75% instead of 50%)
- **Enhanced label placement**: Milestone labels now appear to the right of diamonds instead of below
- **Cleaner label styling**: Removed borders and backgrounds for cleaner appearance
- **Color coordination**: Milestone labels now match their diamond colors automatically
  - Major milestones: Dark red (#dc2626)
  - Minor milestones: Dark orange (#d97706) 
  - Critical milestones: Very dark red (#991b1b)

### 🔧 Technical Improvements
- **Consistent styling**: Applied improvements across all templates (simple, advanced, debug)
- **Better space utilization**: Horizontal label positioning uses available space more efficiently
- **Enhanced readability**: Labels are better visually connected to their milestones

## [2.1.0] - 2024-12-30 ✅ FINAL

### ✨ New Features
- **Milestone Label Visibility Control**: Added `milestone_labels_visible` option
  - `true` (default): Milestone labels always visible
  - `false`: Milestone labels show only on hover

### 🐛 Bug Fixes
- **Fixed milestone labels not displaying**: Corrected CSS positioning and container structure
  - Updated `.gantt-cell` with `overflow: visible` and `min-height: 60px`
  - Fixed `.milestone-text` positioning to `top: 55px` with solid white background
  - Added proper z-index layering for label visibility
  - Implemented milestone container structure for better positioning
- **Template compatibility**: All templates (simple, advanced, debug) now work correctly
- **CSS consistency**: Harmonized label styles across all templates
  - Reduces visual clutter for dense charts
  - Supported in all templates (simple, advanced, standard)

### 🔧 Technical Improvements
- **Enhanced configuration schema** with milestone display options
- **CSS hover states** for conditional milestone label display
- **Extractor support** for new milestone_labels_visible option

### 📚 Documentation
- **User guide updated** with milestone visibility examples
- **New test configuration** demonstrating hover-only labels

## [2.0.0] - 2024-12-30

### 🚀 Major Release - Advanced Features & Robustness

#### ✨ New Features
- **Advanced template system** with `advanced_template.html`
- **Complex project support** with enterprise-level examples  
- **Enhanced extractor** compatible with all template types
- **Special elements support** (alerts, indicators, recurring events)
- **Dynamic JavaScript rendering** with improved grid and task positioning
- **Validation guide** with automated testing procedures
- **Professional styling** with animations and modern CSS

#### 🔧 Technical Improvements
- **Modular generator** with extensible architecture
- **Robust Unicode handling** in extractor
- **Enhanced CLI** with `--output`, `--template` options
- **Dynamic placeholders** in templates for better maintainability
- **Comprehensive error handling** and user feedback

#### 📊 Examples & Templates
- **Complex enterprise project** (`complex_enterprise_project.json`)
- **Advanced styling example** (`styling_example.json`) 
- **Three template options** (simple, standard, advanced)
- **Professional project examples** with realistic timelines

#### 🐛 Bug Fixes
- **JavaScript rendering** corrected for proper grid, task, and milestone display
- **Unicode encoding** issues resolved in extraction process
- **CSS positioning** improved for visual consistency
- **Template compatibility** ensured across all formats

#### 📚 Documentation
- **Unified user guide** consolidating all previous documentation
- **Validation guide** with step-by-step testing procedures
- **Comprehensive examples** covering all feature types
- **Updated README** with advanced usage patterns

## [1.0.0] - 2025-07-01

### 🎉 Initial Release - Project Restructure

#### ✨ Added
- **Multi-language support** (English/French)
- **Modular project structure** with organized directories
- **Command-line interface** with arguments support
- **Professional documentation** in English
- **Contributing guidelines** for open-source development
- **Setup script** for easy installation
- **Git configuration** with appropriate .gitignore
- **Example configurations** for quick start

#### 📁 Project Structure Changes
```
OLD Structure:
├── gantt_generator.py
├── gantt_extractor.py
├── gantt-template.html
├── exemple_config.json
├── generer_gantt.bat
└── README.md (French, SatFlows-specific)

NEW Structure:
├── src/                     # Core Python modules
│   ├── gantt_generator.py   # Main generator (multi-language)
│   └── gantt_extractor.py   # Configuration extractor
├── templates/               # HTML templates
│   ├── gantt_template.html  # Original template
│   └── simple_template.html # Simplified template
├── examples/                # Sample configurations
│   ├── basic_project.json   # Generic project example
│   └── styling_example.json # Styling demonstrations
├── locale/                  # Language files
│   ├── en.json             # English translations
│   └── fr.json             # French translations
├── docs/                    # Documentation
│   ├── user_guide.md        # Complete user guide
│   ├── extractor_guide.md   # Extractor documentation
│   └── styling_guide.md     # Template customization
├── scripts/                 # Utility scripts
│   ├── generate_gantt.bat   # Windows launcher (English)
│   └── extract_config.bat   # Windows extractor
├── README.md               # Main documentation (English)
├── README_fr.md            # French documentation
├── CONTRIBUTING.md         # Contribution guidelines
├── requirements.txt        # Python dependencies
├── setup.py               # Installation script
└── .gitignore             # Git ignore rules
```

#### 🌍 Internationalization
- **English** as default language
- **French** language support maintained
- **Modular translation system** using JSON files
- **Language-specific UI** elements and messages

#### 🚀 Command Line Interface
```bash
# Basic usage
python src/gantt_generator.py

# With language selection
python src/gantt_generator.py --lang fr

# Load configuration
python src/gantt_generator.py --config project.json

# Use custom template
python src/gantt_generator.py --template custom.html
```

#### 📚 Documentation Improvements
- **Professional README** in English
- **User guide** with comprehensive examples
- **Contributing guidelines** for developers
- **Installation instructions** for multiple platforms
- **API reference** for advanced usage

#### 🛠️ Development Improvements
- **Clean code structure** with proper imports
- **Error handling** and user feedback
- **Modular design** for easy extension
- **Template system** for customization
- **Configuration validation**

#### 🔧 Installation & Setup
- **requirements.txt** for dependency management
- **setup.py** for standard Python installation
- **Virtual environment** support
- **Cross-platform compatibility**

### 🔄 Migration from SatFlows-specific to Generic

#### Changed
- **Project branding** removed SatFlows references
- **Example configurations** use generic project scenarios
- **Documentation language** changed to English
- **Use cases** broadened for general project management

#### Removed
- **SatFlows-specific** examples and references
- **French-only** interface elements
- **Hardcoded** project assumptions
- **Company-specific** styling and terminology

### 🎯 Target Audience Expansion

#### Before
- Internal SatFlows project planning
- French-speaking team members
- Specific blockchain/fintech use cases

#### After
- **General project management** across industries
- **International audience** with English documentation
- **Software development** teams worldwide
- **Business planning** and strategic initiatives
- **Educational** and academic projects

### 🚀 Future Roadmap

#### Planned Features
- **Interactive web interface** for configuration
- **PDF export** capabilities
- **Advanced styling** options and themes
- **Collaboration features** for team planning
- **API integration** with project management tools
- **Additional chart types** (timeline, resource allocation)

#### Community Contributions
- **Template marketplace** for sharing designs
- **Plugin system** for custom functionality
- **Integration examples** with popular tools
- **Performance optimizations**
- **Mobile-responsive** improvements

---

## Migration Guide

### For Existing Users

1. **Backup your configurations**:
   ```bash
   cp *.json backups/
   ```

2. **Update file paths**:
   - Move configs to `examples/` directory
   - Update script calls to use `src/` prefix

3. **Language selection**:
   ```bash
   # Old: python gantt_generator.py
   # New: python src/gantt_generator.py --lang fr
   ```

4. **Template customization**:
   - Templates moved to `templates/` directory
   - Use `--template` parameter for custom templates

### For New Users

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/gantt-chart-generator.git
   cd gantt-chart-generator
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Try the examples**:
   ```bash
   python src/gantt_generator.py --config examples/basic_project.json
   ```

4. **Read the documentation**:
   - [User Guide](docs/user_guide.md)
   - [Contributing Guide](CONTRIBUTING.md)

---

*This version represents a complete restructure for open-source distribution and international usage while maintaining backward compatibility for existing workflows.*
