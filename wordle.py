from termcolor import colored
import random

# A large list of possible words to choose from
word_list = ["apple", "table", "chair", "house", "plant", "money", "smile", "water", "train", "light",
    "family", "friend", "market", "school", "garden", "bottle", "candle", "lunch", "winter", "summer",
    "teacher", "student", "morning", "evening", "hospital", "balance", "clothes", "mirror", "battery", "holiday",
    "notebook", "pencil", "paper", "kitchen", "window", "curtain", "pillow", "blanket", "bathroom", "shower",
    "television", "remote", "laptop", "charger", "internet", "keyboard", "mouse", "screen", "headphone", "speaker",
    "grocery", "supermarket", "bakery", "butter", "cheese", "tomato", "potato", "carrot", "spinach", "cabbage",
    "chicken", "mutton", "beef", "cereal", "bread", "noodles", "pasta", "rice", "flour", "sugar",
    "kitchen", "utensils", "fork", "spoon", "knife", "plate", "bowl", "mug", "cup", "glass",
    "clothing", "tshirt", "jeans", "jacket", "sweater", "scarf", "gloves", "socks", "boots", "shoes",
    "slippers", "sandals", "heels", "sneakers", "wallet", "purse", "handbag", "backpack", "umbrella", "raincoat",
    "weather", "sunny", "rainy", "cloudy", "stormy", "snowy", "windy", "humid", "foggy", "breezy",
    "calendar", "appointment", "meeting", "schedule", "deadline", "reminder", "notepad", "journal", "diary", "planner",
    "travel", "airport", "ticket", "passport", "baggage", "suitcase", "backpack", "luggage", "vacation", "tour",
    "transport", "bus", "train", "bicycle", "motorcycle", "scooter", "airplane", "taxi", "subway", "ferry",
    "road", "highway", "street", "bridge", "tunnel", "crosswalk", "sidewalk", "traffic", "signal", "lane",
    "city", "village", "country", "capital", "district", "neighborhood", "avenue", "alley", "square", "plaza",
    "hotel", "restaurant", "cafeteria", "fastfood", "diner", "buffet", "barbecue", "catering", "menu", "order",
    "breakfast", "lunch", "dinner", "snack", "dessert", "beverage", "coffee", "tea", "juice", "soda",
    "sports", "football", "basketball", "cricket", "tennis", "badminton", "volleyball", "swimming", "cycling", "jogging",
    "exercise", "gym", "workout", "training", "yoga", "stretching", "meditation", "running", "hiking", "camping",
    "health", "medicine", "doctor", "nurse", "hospital", "clinic", "pharmacy", "patient", "treatment", "vaccine",
    "body", "head", "hair", "face", "eyes", "ears", "nose", "mouth", "teeth", "tongue",
    "neck", "shoulder", "arm", "elbow", "wrist", "hand", "fingers", "nails", "chest", "stomach",
    "waist", "hip", "leg", "knee", "ankle", "foot", "toes", "skin", "bones", "muscles",
    "school", "college", "university", "teacher", "professor", "student", "classroom", "blackboard", "lesson", "homework",
    "study", "exams", "grades", "subject", "math", "science", "history", "geography", "literature", "language",
    "art", "music", "dance", "drama", "drawing", "painting", "photography", "sculpture", "crafts", "design",
    "technology", "computer", "software", "hardware", "network", "database", "programming", "coding", "internet", "website",
    "communication", "phone", "message", "email", "video", "call", "chat", "social", "media", "newspaper",
    "magazine", "advertisement", "news", "broadcast", "journalist", "editor", "headline", "article", "blog", "podcast",
    "music", "song", "album", "singer", "band", "concert", "melody", "lyrics", "rhythm", "instrument",
    "movie", "cinema", "theater", "actor", "actress", "director", "script", "screenplay", "animation", "series",
    "work", "job", "career", "salary", "promotion", "boss", "employee", "colleague", "meeting", "interview",
    "business", "company", "corporation", "startup", "entrepreneur", "investment", "finance", "stock", "market", "profit",
    "shopping", "store", "supermarket", "mall", "boutique", "discount", "sale", "cashier", "receipt", "checkout",
    "home", "livingroom", "bedroom", "bathroom", "kitchen", "dining", "balcony", "garage", "attic", "basement",
    "garden", "yard", "fence", "driveway", "porch", "roof", "chimney", "doorbell", "doormat", "mailbox",
    "cleaning", "sweeping", "mopping", "vacuuming", "laundry", "washing", "ironing", "dusting", "organizing", "decluttering",
    "finance", "budget", "expense", "income", "savings", "investment", "debt", "loan", "credit", "bank",
    "currency", "exchange", "interest", "mortgage", "insurance", "pension", "salary", "tax", "bills", "economy",
    "science", "biology", "chemistry", "physics", "astronomy", "geology", "botany", "zoology", "genetics", "ecology",
    "nature", "forest", "ocean", "river", "mountain", "desert", "valley", "island", "volcano", "waterfall",
    "weather", "climate", "season", "spring", "summer", "autumn", "winter", "temperature", "humidity", "rainfall",
    "space", "planet", "moon", "star", "galaxy", "universe", "satellite", "telescope", "orbit", "gravity",
    "emotion", "happiness", "sadness", "anger", "fear", "love", "hate", "jealousy", "surprise", "excitement",
    "relationship", "friendship", "family", "marriage", "divorce", "partnership", "trust", "loyalty", "support", "respect"]

# Choose a random word and convert it to uppercase
word = (random.choice(word_list)).upper()
word_letters = list(word)  # Convert word to a list of characters
length_of_word = len(word)  # Store length for validation and attempts

print(f'The word is {length_of_word} letters.')
print(f'You have {length_of_word} attempts')

# Function to handle user's guess and provide feedback
def guessing(Passing_original_letters):
    # Make a copy of the original word's letters so we don't modify it
    temp_original_letters = Passing_original_letters.copy()

    # Take a valid guess from the user
    while True:
        user_guess = input('Enter your guess: ').upper()
        if user_guess.isalpha() and len(user_guess) == length_of_word:
            break
        else:
            print(f'Invalid input! Please enter only English alphabets of {length_of_word} letters.')

    user_guess = list(user_guess)
    print()

    # First pass: mark letters that are correct and in the correct position
    for i in range(length_of_word):
        if user_guess[i] == temp_original_letters[i]:
            user_guess[i] = user_guess[i].lower()
            temp_original_letters[i] = temp_original_letters[i].lower()

    correct_letter_count = 0

    # Second pass: display colored feedback for each letter
    for i in range(length_of_word):
        if user_guess[i] == temp_original_letters[i]:
            print(colored(user_guess[i].upper(), 'green', attrs=['bold']), end='')
            correct_letter_count += 1

            # If all letters are correct, player wins
            if correct_letter_count == length_of_word:
                print('\n')
                print('Congratulations! You got the word.\n')
                return True

            temp_original_letters[i] = 0

        elif user_guess[i] in temp_original_letters:
            print(colored(user_guess[i], 'yellow', attrs=['bold']), end='')
            ind = temp_original_letters.index(user_guess[i])
            temp_original_letters[ind] = 0  # Mark that letter as used

        else:
            print(colored(user_guess[i], 'white', attrs=['bold']), end='')  # Incorrect letter

    print('\n')

# Main game loop
def main():
    for i in range(len(word_letters)):
        print(f"Attempt left: {len(word_letters) - i}\n")
        result = guessing(word_letters)

        if result == True:
            return  # Exit early if the word was guessed

    # If all attempts are used and word not guessed
    print(f"Better luck next time\nThe word was {word}\n")

main()
