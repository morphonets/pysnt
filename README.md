<p align="center"><img src="./docs/_static/snt_logo.svg" alt="SNT" width="150"></p>
<h1 align="center">PySNT</h1>
<h2 align="center">Python wrapper for SNT, the ImageJ framework  for Neuroanatomy</h2>
<div align="center">
  <!-- License -->
  <a href="https://github.com/morphonets/SNT/blob/master/LICENSE.txt">
    <img alt="GitHub license" src="https://img.shields.io/github/license/morphonets/SNT">
  </a>
  <!-- Forum -->
  <a href="https://forum.image.sc/tags/snt">
    <img alt="Forum.sc topics" src="https://img.shields.io/badge/dynamic/json.svg?label=forum&url=https%3A%2F%2Fforum.image.sc%2Ftag%2Fsnt.json&query=%24.topic_list.tags.0.topic_count&suffix=%20topics">
  </a>
  <!-- Issues -->
  <a href="https://github.com/morphonets/pysnt/issues">
    <img alt="Open issues" src="https://img.shields.io/github/issues/morphonets/pysnt">
  </a>
  <a href="https://github.com/morphonets/pysnt/issues">
    <img alt="Closed issues" src="https://img.shields.io/github/issues-closed/morphonets/pysnt">
  </a>
</div>
<div align="center">
  <h3>
    <a href="https://pysnt.readthedocs.io/en/latest/install.html">
      Installation
    </a>
    <span style="margin:.5em">|</span>
    <a href="https://pysnt.readthedocs.io/en/latest/index.html">
       Documentation
    </a>
    <span style="margin:.5em">|</span>
    <a href="https://forum.image.sc/tag/SNT">
      Support
    </a>
  </h3>
</div>

<h3 align="center">⚠️ This project remains experimental. Feedback welcome! ⚠️ </h3>

## Technical Features
- **Complete Java bridge**: Access all SNT Java classes from Python
- **Consistent API**: 1:1 correspondence with SNT's java API
- **Type hints**: Type annotation support with .pyi files
- **IDE support**: Auto-completion in IDEs
- **Dynamic loading**: Lazy loading of Java classes for better performance
- **Development Tools**: Utilities to res

## Limitations
- Headless operations only
- May require unreleased versions of SNT
- Mostly untested

## Getting Started for Developers

### Environment Setup
```bash
# 1. Clone the repository
git clone https://github.com/morphonets/pysnt.git
cd pysnt

# 2. Set up conda/mamba (if not already configured)
mamba config append channels conda-forge
mamba config set channel_priority strict

# 3. Create and activate the development environment
mamba env create -f environment-dev.yml
mamba activate pysnt-dev

# 4. Install PySNT in development mode
pip install -e .[dev]

# 5. Verify the setup
python -c "import pysnt; print('PySNT imported successfully!')"

# 6. Have a look at ./dev/README.md for common workflows
```

### IDE Configuration

#### PyCharm
1. Open this folder as a project in PyCharm
2. Go to File → Settings → Project → Python Interpreter
3. Select the 'pysnt' conda environment

#### VS Code
1. Open this folder in VS Code
2. Install recommended extensions when prompted
3. Select the 'pysnt' Python interpreter when prompted

#### Spyder
1. Make sure Spyder is installed in the 'pysnt' environment:
   ```bash
    conda activate pysnt
    conda install spyder
    ```
2. Launch Spyder from the activated environment
3. Open this folder as a project: File → Open Project

### Project Structure

```
pysnt/
├── src/pysnt/        # Main package source
├── tests/            # Test suite
├── scripts/          # Development scripts
├── docs/             # Documentation source
├── dev/              # Development utilities and templates
└── environment.yml   # Environment specification
```

### Need Help?

- 📖 **Documentation**: [pysnt.readthedocs.io](https://pysnt.readthedocs.io)
- 💬 **Forum**: [forum.image.sc/tag/snt](https://forum.image.sc/tag/snt)
- 🐛 **Issues**: [GitHub Issues](https://github.com/morphonets/pysnt/issues)