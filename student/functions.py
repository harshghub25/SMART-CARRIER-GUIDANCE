import google.generativeai as genai

genai.configure(api_key="AIzaSyARd_OmWv8F6knd42AWR9Qw6MrPKIXjkuw")
model = genai.GenerativeModel("gemini-2.5-flash")

def get_ai_career_suggestion(profile):
    """
    Generate career suggestion from student profile using AI
    """
    prompt = f"""
    You are a career guidance expert.

    Student Profile:
    Education: {profile.degree}
    Graduation Year: {profile.graduation_year}
    Skills: {profile.interest}
    Interest: {profile.interest}

    Suggest the most suitable career path for this student.
    Provide it as a short clear recommendation.
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print("AI API error:", e)
        return "Explore skills → Internship → Specialization"