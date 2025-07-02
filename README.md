# 🎓 AI Student Dropout Prediction

This project leverages the AI Development Workflow to predict the risk of student dropout in online learning platforms. It combines data science, machine learning, and software engineering practices to provide a CLI tool and reproducible training pipeline.

> 🔍 Predict which learners are at risk—before they drop out.

---

## 📁 Project Structure

| Folder / File        | Purpose |
|----------------------|---------|
| `data/`              | Sample training dataset in CSV format |
| `src/`               | Training, preprocessing, and evaluation scripts |
| `model/`             | Command-line predictor script (`predict.py`) |
| `notebook/`          | Model development and experimentation notebook |
| `report/`            | Case study, analysis, and deliverables |
| `requirements.txt`   | Python dependencies for project environment |
| `README.md`          | This project guide and usage manual |

---

## 🧠 Model Overview

- **Algorithm**: Random Forest Classifier  
- **Inputs**: Gender, Age, Location, Language, Time Spent, Quiz Score, Login Count  
- **Output**: Dropout Risk Prediction (`Dropped Out` / `Continued`)  
- **Performance Metrics**: *To be added post-evaluation*

---

## 🚀 How to Use the Predictor (CLI)

Run from inside the `model/` directory:



```bash
python predict.py --gender F --age 24 --language English --location Suburban --time_spent 5.5 --quiz_score 80 --login_count 9


## 📊 Data Fields

| Feature       | Description                         |
|---------------|-------------------------------------|
| `gender`      | Student’s gender (M/F)              |
| `age`         | Age in years                        |
| `language`    | Primary language of instruction     |
| `location`    | Region type (Urban/Suburban/Rural)  |
| `time_spent`  | Average weekly hours spent          |
| `quiz_score`  | Average quiz score (0–100)          |
| `login_count` | Weekly login frequency              |

## 📌 Project Status

- ✅ Model Trained  
- ✅ CLI Tool Ready  
- 🚧 Accuracy Metrics & Web UI – In Progress  
- 🚀 `recovery-main` branch is currently ahead of `main`

---------

🪄 Future Ideas
•	[ ] Streamlit web app for real-time prediction
•	[ ] Model evaluation dashboard
•	[ ] Support for external CSV uploads
•	[ ] Add dropout probability (% confidence)
Made with passion, Python 🐍, and persistent debugging 💥

-----------

## 🙋‍♂️ Maintainer

**Leonard Phokane**  
Cloud Engineering · App Development · Ethical AI  

## 🔗 Connect with Me

📫 [LinkedIn – Leonard Phokane](https://www.linkedin.com/in/leonard-phokane)  
🌐 [Enhanced Cloud Portfolio](https://leonardphokane.github.io/enhanced-cloud-portfolio/)  
📊 [AI Student Dropout Prediction](https://leonardphokane.github.io/ai-student-dropout-prediction/)





