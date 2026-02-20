# Random Scikit-learn Guide Generator 🎲

A Streamlit application that randomly displays guides from the scikit-learn
User Guide, helping you discover and learn about different machine learning
topics.

## Features

- 🎲 Random guide selection from 45+ scikit-learn topics
- 📖 Preview of guide content
- 🔗 Direct links to full documentation
- 🎨 Clean, user-friendly interface
- 🔄 Easy navigation between different guides

## Installation

1. **Clone or download this repository**
2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the Streamlit app:

```bash
streamlit run sklearn_guide_app.py
```

The app will open in your default web browser at `http://localhost:8501`

## How to Use

1. Click the **"🎲 Get Random Guide"** button to display a random scikit-learn guide
2. View the preview of the guide content
3. Click **"📖 Read Full Guide"** to open the complete documentation
4. Click **"🔄 Get Another Random Guide"** to discover a different topic

## Available Topics

The app includes guides from all major scikit-learn categories:

- **Supervised Learning**: Linear Models, SVM, Decision Trees, Neural Networks, etc.
- **Unsupervised Learning**: Clustering, Manifold Learning, Dimensionality Reduction, etc.
- **Model Selection**: Cross-validation, Hyperparameter Tuning, Metrics, etc.
- **Data Processing**: Preprocessing, Feature Extraction, Pipelines, etc.
- **Best Practices**: Common Pitfalls, Model Persistence, etc.

## Requirements

- Python 3.7+
- streamlit >= 1.28.0
- requests >= 2.31.0
- beautifulsoup4 >= 4.12.0

## License

This project is provided as-is for educational purposes. The scikit-learn
documentation content is © scikit-learn developers (BSD License).

## Contributing

Feel free to fork this project and add more features such as:

- Filtering by category
- Search functionality
- Bookmarking favorite guides
- Progress tracking
