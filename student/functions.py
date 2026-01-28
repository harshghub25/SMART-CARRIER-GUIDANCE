from openai import OpenAI
import os

# Set your API key (you can also store in env variable)
client = OpenAI(api_key="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")

def get_ai_career_suggestion(profile):
    """
    Generate career suggestion from student profile using AI
    """
    # Prepare prompt for AI
    prompt = f"""
    Student Profile:
    Education: {profile.degree}
    Graduation Year: {profile.graduation_year}
    Skills: {profile.interest}
    Interest: {profile.interest}

    Suggest the most suitable career path for this student.
    Provide it as a short clear recommendation.
    """

    try:
        response = client.chat.completions.create(
        model="gpt-4o-mini",  # cheap + good
        messages=[
            {"role": "system", "content": "You are a career guidance expert."},
            {"role": "user", "content": prompt}
        ]
    )
        return response.choices[0].message.content
    except Exception as e:
        print("AI API error:", e)
        return "Explore skills → Internship → Specialization"  # fallback
