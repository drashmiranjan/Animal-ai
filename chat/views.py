from django.shortcuts import render
from .forms import *
import google.generativeai as genai
from decouple import config

genai.configure(api_key=config("GEMINI_API_KEY"))

def get_ai_response(image_path):
    try:
        with open(image_path, "rb") as img_file:
            image_bytes = img_file.read()

        model = genai.GenerativeModel("gemini-1.5-flash")

        response = model.generate_content(
            [
                {"text": "This is an image of an injured animal. Give first aid advice."},
                {"mime_type": "image/jpeg", "data": image_bytes},
            ]
        )

        return response.text
    except Exception as e:
        return f"AI processing failed: {str(e)}"

# ✅ Main view for uploading image and getting AI help
def ChatForm(request):
    response = None
    img_obj = None

    if request.method == 'POST':
        form = Animalform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            image_path = img_obj.image.path

            # Get response from Gemini
            response = get_ai_response(image_path)

            return render(request, 'ChatForm.html', {
                'form': form,
                'img_obj': img_obj,
                'response': response
            })
    else:
        form = Animalform()

    return render(request, 'ChatForm.html', {'form': form})
