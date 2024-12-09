# views.py
import random
from django.http import JsonResponse
from .models import ActivityModel

def activity_view(request):
     # Fetch the activity with the name 'fraction 1'
    try:
        activity = ActivityModel.objects.get(name='fraction 1')
    except ActivityModel.DoesNotExist:
        return JsonResponse({"error": "Activity with name 'fraction 1' does not exist."}, status=404)
        # Define the lists of random values
    colors = ["rouge", "bleu", "violet", "jaune"]
    items_with_price_ranges = {
        "voiture": (1000, 5000),  # Cars: higher price range
        "bille": (1, 3),         # Apples: low price range
        "livre": (10, 50),       # Books: moderate price range
        "chaise": (20, 100),     # Chairs: higher than books
    }

    # Randomly select values for the placeholders
    nb_item = random.randint(10, 50)
    nb_item1 = random.randint(3, nb_item - 1)  # Ensure it doesn't exceed `nb_item`
    nb_item2 = nb_item - nb_item1
    name_item = random.choice(list(items_with_price_ranges.keys()))
    
    color_item1 = random.choice(colors)
    color_item2 = random.choice([color for color in colors if color != color_item1])  # Ensure different color

    # Fetch the price range based on the item type
    price_min, price_max = items_with_price_ranges[name_item]

    # Define logical pricing within the range
    price_per_item1 = random.randint(price_min, price_max)  # Price per unit for color_item1
    price_item2 = random.randint(price_min, price_max)      # Price per unit for color_item2

    # Calculate total price
    price_part1 = nb_item1 * price_per_item1
    price_part2 = nb_item2 * price_item2
    price_total = price_part1 + price_part2

    # Use the existing theoretical_text field with .format()
    theoretical_text = activity.theoretical_text.format(
        nb_item=nb_item,
        name_item=name_item,
        price_total=price_total,
        nb_item1=nb_item1,
        color_item1=color_item1,
        color_item2=color_item2,
        price_item2=price_item2
    )
    questions_list = activity.questions_list
    updated_questions = []
    for question in questions_list:
        updated_question = question.format(
        nb_item=nb_item,
        name_item=name_item,
        price_total=price_total,
        nb_item1=nb_item1,
        color_item1=color_item1,
        color_item2=color_item2,
        price_item2=price_item2
        )
        updated_questions.append(updated_question)

    return JsonResponse({
        "theoretical_text": theoretical_text,
        "questions_list": updated_questions,
    }, json_dumps_params={'ensure_ascii': False})
