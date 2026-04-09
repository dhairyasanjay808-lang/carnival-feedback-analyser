# Carnival Feedback Analyzer

## Overview
This tool was developed to analyze attendee feedback from the first-ever Christmas Carnival me and my council organized of **GD GOENKA INTERNATIONAL SCHOOL, SURAT**. The event hosted over **2,000 attendees**. This project automates sentiment analysis to provide actionable insights for future large-scale student events.

## Problem Statement
Manually processing feedback from 2,000 people is impractical. I built this to:
- Identify what attendees loved
- Surface recurring pain points
- Guide improvements for future events

## Live Demo
*The application is fully functional locally. To run it, follow the instructions in the "How to Run Locally" section below. A cloud deployment is pending due to Streamlit Community Cloud build queue delays. The source code and documentation are complete and available in this repository.*

## Technical Implementation
- **Frontend:** Streamlit (Python)
- **Data Processing:** Pandas
- **Sentiment Analysis:** TextBlob (NLP)
- **Visualization:** Matplotlib, WordCloud

## How to Run Locally
1. Clone the repository  
   `git clone https://github.com/YOUR_USERNAME/carnival-feedback-analyzer.git`
2. Create a virtual environment  
   `python3 -m venv venv`
3. Activate it (macOS/Linux)  
   `source venv/bin/activate`
4. Install dependencies  
   `pip install -r requirements.txt`
5. Run the app  
   `streamlit run app.py`

## Key Insights (Mock Data)
Top praises: **music**, **organization**  
Top complaints: **queues**, **sound system**

## Portfolio Context

This project was born out of a real-world need. As Head Boy, My council organized a Christmas carnival attended by over 2,000 students. The event generated a substantial amount of qualitative feedback, but manually parsing hundreds of comments to identify what worked and what didn't was impractical.

I built the **Carnival Feedback Analyzer** to automate that process—turning raw attendee comments into clear, actionable insights. It uses **natural language processing** to gauge sentiment and surface recurring themes, making it easier for future event organizers to make data-informed decisions.

## AI-Assisted Development Disclosure
Generative AI (Claude) was used as a coding assistant to:
- Suggest syntax and boilerplate code
- Structure the Streamlit app
- Debug minor errors

All architectural decisions, feature selection, testing, and final code review were performed by me.

---

**Built by Dhairya Dulani**  
