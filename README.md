
# AI Career Guidance System (Praxis 2.0)

Problem Statement Alignment:

This project aligns with Praxis 2.0 problem statement focused on improving student employability and career guidance using GenAI and Machine Learning.

The system analyzes student resumes to extract skills and provides AI-powered career recommendations and skill gap insights.

## Overview
A Machine Learning based Resume Analyzer that extracts skills from resumes and prepares them for GenAI career guidance.

## Tech Stack
- Python
- Flask
- Scikit-learn
- PDFPlumber

## Architecture
Resume -> Text Extraction -> TF-IDF Skill Extraction -> (Future GenAI Career Advice)

## ML + GenAI
Currently TF-IDF extracts skills. GenAI layer can be added for career recommendations.

## Ethics
No resume data stored.

## Business Feasibility
Useful for colleges, HR, placement cells.

## Run
pip install -r requirements.txt
python app.py
