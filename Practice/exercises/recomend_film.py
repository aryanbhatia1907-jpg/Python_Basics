from film_list import movies        # importing movies from other file
import random

def recommend(mood, genre, language,length):
    # Filter movies matching ALL three criteria
    results = []
    for name, details in movies.items():
        if (details["mood"] == mood and
            details["genre"] == genre and
            details["language"] == language and
            details["duration"] == length):
            results.append((name, details))

    # Sort by rating highest first using lambda
    results = sorted(results, key=lambda x: x[1]["rating"], reverse=True)
    return results

def display_results(results):
    if not results:
        print(f"\n😔 No movies found matching your preferences!")
        # print(f"Try {random.genre} instead of {movies['genre']}!")
        return

    print(f"\n🎬 Found {len(results)} movie(s) for you!\n")
    print("-" * 50)

    for i, (name, details) in enumerate(results, start=1):
        print(f"{i}. {name}")
        print(f"   ⭐ Rating    : {details['rating']}/10")
        print(f"   🎭 Genre     : {details['genre']}")
        print(f"   🌍 Language  : {details['language']}")
        print(f"   ⏱️  Duration  : {details['duration']}")
        print(f"   📖 Plot      : {details['description']}")
        print("-" * 50)

def main():
    print("=" * 50)
    print("   🎬 WHAT SHOULD I WATCH TONIGHT? 🎬")
    print("=" * 50)

    # Mood selection
    print("\n😊 Select your mood:")
    moods = ["excited", "sad", "bored", "romantic"]
    for i, mood in enumerate(moods, 1):
        print(f"   {i}. {mood.capitalize()}")

    # Genre selection
    print("\n🎭 Select genre:")
    genres = ["Horror", "Action", "Comedy", "Romance","Sci-Fi","Thriller", "Drama"]
    for i, genre in enumerate(genres, 1):
        print(f"   {i}. {genre}")

    # Language selection
    print("\n🌍 Select language:")
    languages = ["Hindi", "English"]
    for i, lang in enumerate(languages, 1):
        print(f"   {i}. {lang}")

    print("\n🌍 Select duration:")
    lengths = ["Short", "Long"]
    for i, le in enumerate(lengths, 1):
        print(f"   {i}. {le}")


    try:
        mood_choice    = int(input("\nEnter mood number: "))
        genre_choice   = int(input("Enter genre number: "))
        lang_choice    = int(input("Enter language number: "))
        leng_choice    = int(input("Enter duration: "))

        # Convert number to actual value
        mood     = moods[mood_choice - 1]
        genre    = genres[genre_choice - 1]
        language = languages[lang_choice - 1]
        length = lengths[leng_choice-1]
        

        # Get recommendations
        results = recommend(mood, genre, language, length)
        display_results(results)

    except ValueError:
        print("❌ Please enter a valid number!")
    except IndexError:
        print("❌ Please choose from the given options only!")

if __name__ == "__main__":
    while True:
        main()          # caling main fn
        again = input("\n🔄 Search again? (yes/no): ").lower()
        if again != "yes":
            print("\n🎬 Enjoy your movie! Goodbye! 👋")
            break