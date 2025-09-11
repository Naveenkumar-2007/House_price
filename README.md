# Machine Learning Price Estimator

A California housing price prediction system using Artificial Neural Networks (ANN) built with TensorFlow/Keras and served via FastAPI. This project predicts house prices based on various features from the California housing dataset.

## 🎯 Project Overview

This machine learning application uses deep learning techniques to predict housing prices in California. The model is trained on the California housing dataset and deployed as a REST API using FastAPI for real-time predictions.

## 🚀 Features

- **Artificial Neural Network**: Deep learning model built with TensorFlow/Keras
- **Real-time Predictions**: FastAPI-based REST API for instant price predictions
- **Data Preprocessing**: Comprehensive data cleaning and feature engineering
- **Model Evaluation**: Performance metrics and validation
- **Interactive API**: Swagger UI documentation for easy testing

## 🛠️ Tech Stack

- **Machine Learning**: TensorFlow, Keras, Scikit-learn
- **API Framework**: FastAPI
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Development**: Python 3.8+
- **API Documentation**: Swagger UI (automatically generated)

## 📊 Dataset Features

The model uses the following features from the California housing dataset:

- **MedInc**: Median income in block group
- **HouseAge**: Median house age in block group
- **AveRooms**: Average number of rooms per household
- **AveBedrms**: Average number of bedrooms per household
- **Population**: Block group population
- **AveOccup**: Average number of household members
- **Latitude**: Block group latitude
- **Longitude**: Block group longitude

**Target**: Median house value in hundreds of thousands of dollars

## 🔄 Implementation Workflow

1. **Data Loading & Exploration**
   - Load California housing dataset
   - Exploratory data analysis
   - Statistical summary and visualization

2. **Data Preprocessing**
   - Handle missing values
   - Feature scaling/normalization
   - Train-test split

3. **Model Development**
   - Design ANN architecture
   - Compile model with appropriate loss function
   - Train with validation monitoring

4. **Model Evaluation**
   - Performance metrics (MSE, MAE, R²)
   - Validation and testing
   - Model optimization

5. **API Development**
   - FastAPI application setup
   - Endpoint creation for predictions
   - Input validation and error handling

6. **Deployment**
   - API documentation with Swagger
   - Testing and validation

## 💻 How to Use

### Prerequisites

```bash
python >= 3.8
pip install -r requirements.txt
```

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Naveenkumar-2007/Machine-Learning-Price-Estimator.git
   cd Machine-Learning-Price-Estimator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Train the model** (if needed)
   ```bash
   python train_model.py
   ```

2. **Start the FastAPI server**
   ```bash
   uvicorn main:app --reload
   ```

3. **Access the API**
   - API Base URL: `http://localhost:8000`
   - Interactive Documentation: `http://localhost:8000/docs`
   - Alternative Documentation: `http://localhost:8000/redoc`

### Making Predictions

**Via API Endpoint:**
```bash
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{
       "MedInc": 8.3252,
       "HouseAge": 41.0,
       "AveRooms": 6.984,
       "AveBedrms": 1.023,
       "Population": 322.0,
       "AveOccup": 2.555,
       "Latitude": 37.88,
       "Longitude": -122.23
     }'
```

**Via Swagger UI:**
1. Navigate to `http://localhost:8000/docs`
2. Expand the POST `/predict` endpoint
3. Click "Try it out"
4. Enter the required parameters
5. Click "Execute"

## 📈 Model Performance

The trained ANN model achieves competitive performance on the California housing dataset with comprehensive evaluation metrics including Mean Squared Error, Mean Absolute Error, and R-squared scores.

## 📁 Project Structure

```
Machine-Learning-Price-Estimator/
├── main.py              # FastAPI application
├── train_model.py       # Model training script
├── model/              # Trained model files
├── data/               # Dataset files
├── notebooks/          # Jupyter notebooks for analysis
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---



## 🌐 Socials:
<p align="left">
<a href="https://www.linkedin.com/in/naveen-kumar-chapala-69980533b/"><img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white" /></a>
<a href="https://github.com/Naveenkumar-2007"><img src="https://img.shields.io/badge/GitHub-100000?logo=github&logoColor=white" /></a>
</p>

---
