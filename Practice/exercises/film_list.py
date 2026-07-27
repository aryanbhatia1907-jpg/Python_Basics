# yeh movies list hai jo `recommend_film` program ko chalayegi 

movies = {

    # ═══════════════════════════════
    # EXCITED + HORROR + HINDI
    # ═══════════════════════════════

    "Tumbbad": {
        "mood": "excited",
        "genre": "Horror",
        "language": "Hindi",
        "duration": "Long",
        "rating": 8.2,
        "description": "Ek mythological story greed ke baare mein colonial India mein!"
    },
    "Stree": {
        "mood": "excited",
        "genre": "Horror",
        "language": "Hindi",
        "duration": "Long",
        "rating": 7.6,
        "description": "Ek choti si town mein ek mysterious aurat ka terror!"
    },
    "Bhool Bhulaiyaa 2": {
        "mood": "excited",
        "genre": "Horror",
        "language": "Hindi",
        "duration": "Long",
        "rating": 6.3,
        "description": "Haunted haveli mein comedy aur horror ka mix!"
    },
    "Roohi": {
        "mood": "excited",
        "genre": "Horror",
        "language": "Hindi",
        "duration": "Long",
        "rating": 5.0,
        "description": "Ek possessed dulhan aur do banda — comedy horror!"
    },
    "Pari": {
        "mood": "excited",
        "genre": "Horror",
        "language": "Hindi",
        "duration": "Long",
        "rating": 6.3,
        "description": "Anushka Sharma ek dark supernatural force se connected hai!"
    },

    # ═══════════════════════════════
    # EXCITED + HORROR + ENGLISH
    # ═══════════════════════════════

    "Hereditary": {
        "mood": "excited",
        "genre": "Horror",
        "language": "English",
        "duration": "Long",
        "rating": 7.3,
        "description": "Family tragedy ke baad dark secrets saamne aate hain!"
    },
    "The Conjuring": {
        "mood": "excited",
        "genre": "Horror",
        "language": "English",
        "duration": "Long",
        "rating": 7.5,
        "description": "Paranormal investigators ka sabse khatarnak case!"
    },
    "Get Out": {
        "mood": "excited",
        "genre": "Horror",
        "language": "English",
        "duration": "Long",
        "rating": 7.7,
        "description": "Ek Black man apni girlfriend ke family se milne jaata hai — shocking results!"
    },
    "A Quiet Place": {
        "mood": "excited",
        "genre": "Horror",
        "language": "English",
        "duration": "Long",
        "rating": 7.5,
        "description": "Ek family survive karti hai monsters se jo sound se attack karte hain!"
    },
    "The Nun": {
        "mood": "excited",
        "genre": "Horror",
        "language": "English",
        "duration": "Long",
        "rating": 5.4,
        "description": "Conjuring universe ki sabse dark origin story!"
    },
    "IT": {
        "mood": "excited",
        "genre": "Horror",
        "language": "English",
        "duration": "Long",
        "rating": 7.3,
        "description": "Pennywise the clown ek chote town ke bachon ko terrorize karta hai!"
    },
    "Midsommar": {
        "mood": "excited",
        "genre": "Horror",
        "language": "English",
        "duration": "Long",
        "rating": 7.1,
        "description": "Sweden ka ek sundar village — lekin andar kuch bahut dark chal raha hai!"
    },
    "Us": {
        "mood": "excited",
        "genre": "Horror",
        "language": "English",
        "duration": "Long",
        "rating": 6.8,
        "description": "Ek family ko unke hi identical twins attack karte hain!"
    },

    # ═══════════════════════════════
    # EXCITED + ACTION + HINDI
    # ═══════════════════════════════

    "KGF Chapter 2": {
        "mood": "excited",
        "genre": "Action",
        "language": "Hindi",
        "duration": "Long",
        "rating": 8.4,
        "description": "Rocky ka empire aur bada hota hai jab dushman aur strong ho jaate hain!"
    },
    "RRR": {
        "mood": "excited",
        "genre": "Action",
        "language": "Hindi",
        "duration": "Long",
        "rating": 7.8,
        "description": "Do freedom fighters aur unka epic journey!"
    },
    "Pathaan": {
        "mood": "excited",
        "genre": "Action",
        "language": "Hindi",
        "duration": "Long",
        "rating": 5.9,
        "description": "Shah Rukh Khan ek spy action thriller mein!"
    },
    "War": {
        "mood": "excited",
        "genre": "Action",
        "language": "Hindi",
        "duration": "Long",
        "rating": 6.5,
        "description": "Ek agent apne hi mentor ko hunt karta hai!"
    },
    "Tiger Zinda Hai": {
        "mood": "excited",
        "genre": "Action",
        "language": "Hindi",
        "duration": "Long",
        "rating": 6.0,
        "description": "Salman Khan ek rescue mission pe Iraq mein!"
    },
    "Brahmastra": {
        "mood": "excited",
        "genre": "Action",
        "language": "Hindi",
        "duration": "Long",
        "rating": 5.5,
        "description": "Ek superhero universe jisme ancient astras ka power hai!"
    },
    "Dhoom 3": {
        "mood": "excited",
        "genre": "Action",
        "language": "Hindi",
        "duration": "Long",
        "rating": 5.3,
        "description": "Aamir Khan ek mastermind thief ke roop mein Chicago mein!"
    },

    # ═══════════════════════════════
    # EXCITED + ACTION + ENGLISH
    # ═══════════════════════════════

    "Avengers Endgame": {
        "mood": "excited",
        "genre": "Action",
        "language": "English",
        "duration": "Long",
        "rating": 8.4,
        "description": "Universe bachane ki ultimate battle!"
    },
    "The Dark Knight": {
        "mood": "excited",
        "genre": "Action",
        "language": "English",
        "duration": "Long",
        "rating": 9.0,
        "description": "Batman vs Joker — best superhero movie ever!"
    },
    "Mad Max Fury Road": {
        "mood": "excited",
        "genre": "Action",
        "language": "English",
        "duration": "Long",
        "rating": 8.1,
        "description": "Post-apocalyptic desert mein non-stop car chase!"
    },
    "John Wick": {
        "mood": "excited",
        "genre": "Action",
        "language": "English",
        "duration": "Long",
        "rating": 7.4,
        "description": "Ek retired hitman unse badla leta hai jinhone uski dog maari!"
    },
    "Mission Impossible Fallout": {
        "mood": "excited",
        "genre": "Action",
        "language": "English",
        "duration": "Long",
        "rating": 7.7,
        "description": "Ethan Hunt ka sabse dangerous mission!"
    },
    "Top Gun Maverick": {
        "mood": "excited",
        "genre": "Action",
        "language": "English",
        "duration": "Long",
        "rating": 8.3,
        "description": "Maverick young pilots ko train karta hai ek impossible mission ke liye!"
    },

    # ═══════════════════════════════
    # BORED + THRILLER + HINDI
    # ═══════════════════════════════

    "Drishyam 2": {
        "mood": "bored",
        "genre": "Thriller",
        "language": "Hindi",
        "duration": "Long",
        "rating": 8.1,
        "description": "Vijay Salgaonkar apne family ka raaz police se chupaata rehta hai!"
    },
    "Andhadhun": {
        "mood": "bored",
        "genre": "Thriller",
        "language": "Hindi",
        "duration": "Long",
        "rating": 8.3,
        "description": "Ek andha pianist accidentally ek murder dekhta hai!"
    },
    "Kahaani": {
        "mood": "bored",
        "genre": "Thriller",
        "language": "Hindi",
        "duration": "Long",
        "rating": 8.1,
        "description": "Ek pregnant woman Kolkata mein apne missing husband ko dhundti hai!"
    },
    "Talaash": {
        "mood": "bored",
        "genre": "Thriller",
        "language": "Hindi",
        "duration": "Long",
        "rating": 7.0,
        "description": "Aamir Khan ek detective jo ek actor ki death investigate karta hai!"
    },
    "Ugly": {
        "mood": "bored",
        "genre": "Thriller",
        "language": "Hindi",
        "duration": "Long",
        "rating": 8.3,
        "description": "Ek bachchi gayab ho jaati hai aur sab ke intentions suspicious lagte hain!"
    },
    "A Wednesday": {
        "mood": "bored",
        "genre": "Thriller",
        "language": "Hindi",
        "duration": "Short",
        "rating": 8.2,
        "description": "Ek common man police ko ek unusual ultimatum deta hai!"
    },

    # ═══════════════════════════════
    # BORED + THRILLER + ENGLISH
    # ═══════════════════════════════

    "Inception": {
        "mood": "bored",
        "genre": "Thriller",
        "language": "English",
        "duration": "Long",
        "rating": 8.8,
        "description": "Ek thief logon ke dreams mein ghuskar secrets churaata hai!"
    },
    "Gone Girl": {
        "mood": "bored",
        "genre": "Thriller",
        "language": "English",
        "duration": "Long",
        "rating": 8.1,
        "description": "Ek aurat gayab ho jaati hai aur uska husband suspect ban jaata hai!"
    },
    "Shutter Island": {
        "mood": "bored",
        "genre": "Thriller",
        "language": "English",
        "duration": "Long",
        "rating": 8.1,
        "description": "Ek detective ek mental asylum mein missing patient dhundta hai!"
    },
    "Parasite": {
        "mood": "bored",
        "genre": "Thriller",
        "language": "English",
        "duration": "Long",
        "rating": 8.5,
        "description": "Ek garib family ek ameer family ke ghar mein slowly ghus jaati hai!"
    },
    "Se7en": {
        "mood": "bored",
        "genre": "Thriller",
        "language": "English",
        "duration": "Long",
        "rating": 8.6,
        "description": "Do detectives ek serial killer ko dhundte hain jo 7 sins pe murders karta hai!"
    },
    "Prisoners": {
        "mood": "bored",
        "genre": "Thriller",
        "language": "English",
        "duration": "Long",
        "rating": 8.1,
        "description": "Ek baap khud apni bachi ko dhundne nikalta hai jab police fail ho jaati hai!"
    },

    # ═══════════════════════════════
    # BORED + DRAMA + HINDI
    # ═══════════════════════════════

    "Article 15": {
        "mood": "bored",
        "genre": "Drama",
        "language": "Hindi",
        "duration": "Long",
        "rating": 8.1,
        "description": "Ek cop rural India mein caste discrimination investigate karta hai!"
    },
    "Gulaal": {
        "mood": "bored",
        "genre": "Drama",
        "language": "Hindi",
        "duration": "Long",
        "rating": 8.1,
        "description": "Rajasthan mein politics aur power ki dark duniya!"
    },
    "Masaan": {
        "mood": "bored",
        "genre": "Drama",
        "language": "Hindi",
        "duration": "Long",
        "rating": 8.2,
        "description": "Varanasi ke ghats pe do alag log apni zindagi se ladte hain!"
    },
    "Gangs of Wasseypur": {
        "mood": "bored",
        "genre": "Drama",
        "language": "Hindi",
        "duration": "Long",
        "rating": 8.2,
        "description": "Generations ki dushmani ek Jharkhand town mein coal mafia ke saath!"
    },
    "Paan Singh Tomar": {
        "mood": "bored",
        "genre": "Drama",
        "language": "Hindi",
        "duration": "Long",
        "rating": 8.2,
        "description": "National champion athlete kaise ek dacoit ban gaya!"
    },

    # ═══════════════════════════════
    # BORED + SCI-FI + ENGLISH
    # ═══════════════════════════════

    "Interstellar": {
        "mood": "bored",
        "genre": "Sci-Fi",
        "language": "English",
        "duration": "Long",
        "rating": 8.7,
        "description": "Astronauts ek wormhole se travel karte hain humanity ko bachane ke liye!"
    },
    "The Matrix": {
        "mood": "bored",
        "genre": "Sci-Fi",
        "language": "English",
        "duration": "Long",
        "rating": 8.7,
        "description": "Ek hacker discover karta hai ki reality actually ek simulation hai!"
    },
    "Arrival": {
        "mood": "bored",
        "genre": "Sci-Fi",
        "language": "English",
        "duration": "Long",
        "rating": 7.9,
        "description": "Ek linguist aliens se communicate karne ki koshish karti hai!"
    },
    "Ex Machina": {
        "mood": "bored",
        "genre": "Sci-Fi",
        "language": "English",
        "duration": "Long",
        "rating": 7.7,
        "description": "Ek programmer AI robot ke saath interact karta hai — dark results!"
    },
    "Blade Runner 2049": {
        "mood": "bored",
        "genre": "Sci-Fi",
        "language": "English",
        "duration": "Long",
        "rating": 8.0,
        "description": "Future mein ek blade runner ek secret dhundta hai jo duniya badal sakta hai!"
    },

    # ═══════════════════════════════
    # SAD + DRAMA + HINDI
    # ═══════════════════════════════

    "Taare Zameen Par": {
        "mood": "sad",
        "genre": "Drama",
        "language": "Hindi",
        "duration": "Long",
        "rating": 8.5,
        "description": "Ek dyslexic bacha aur ek teacher jo uski zindagi badal deta hai!"
    },
    "Dangal": {
        "mood": "sad",
        "genre": "Drama",
        "language": "Hindi",
        "duration": "Long",
        "rating": 8.4,
        "description": "Ek baap apni betiyion ko world champion wrestler banata hai!"
    },
    "Lootera": {
        "mood": "sad",
        "genre": "Drama",
        "language": "Hindi",
        "duration": "Long",
        "rating": 7.6,
        "description": "1950s India mein ek tragic love story!"
    },
    "Udaan": {
        "mood": "sad",
        "genre": "Drama",
        "language": "Hindi",
        "duration": "Long",
        "rating": 8.2,
        "description": "Ek ladka apne strict baap se apne sapnon ke liye ladhta hai!"
    },
    "Kapoor and Sons": {
        "mood": "sad",
        "genre": "Drama",
        "language": "Hindi",
        "duration": "Long",
        "rating": 7.6,
        "description": "Ek dysfunctional family ka emotional reunion!"
    },
    "Dil Dhadakne Do": {
        "mood": "sad",
        "genre": "Drama",
        "language": "Hindi",
        "duration": "Long",
        "rating": 7.3,
        "description": "Ek rich family cruise pe — aur har kisi ke paas secrets hain!"
    },

    # ═══════════════════════════════
    # SAD + DRAMA + ENGLISH
    # ═══════════════════════════════

    "The Pursuit of Happyness": {
        "mood": "sad",
        "genre": "Drama",
        "language": "English",
        "duration": "Long",
        "rating": 8.0,
        "description": "Will Smith ek single dad jo apne bete ke liye sab kuch sacrifice karta hai!"
    },
    "Schindlers List": {
        "mood": "sad",
        "genre": "Drama",
        "language": "English",
        "duration": "Long",
        "rating": 9.0,
        "description": "Nazi Germany mein ek businessman hazaron Jews ko bachata hai!"
    },
    "Forrest Gump": {
        "mood": "sad",
        "genre": "Drama",
        "language": "English",
        "duration": "Long",
        "rating": 8.8,
        "description": "Ek simple man ka extraordinary life journey!"
    },
    "A Beautiful Mind": {
        "mood": "sad",
        "genre": "Drama",
        "language": "English",
        "duration": "Long",
        "rating": 8.2,
        "description": "Math genius John Nash ki schizophrenia se ladai!"
    },
    "The Green Mile": {
        "mood": "sad",
        "genre": "Drama",
        "language": "English",
        "duration": "Long",
        "rating": 8.6,
        "description": "Death row pe ek innocent man ki tragic kahani!"
    },
    "Grave of the Fireflies": {
        "mood": "sad",
        "genre": "Drama",
        "language": "English",
        "duration": "Long",
        "rating": 8.5,
        "description": "WW2 Japan mein do siblings ki survival story — warning: bahut rona padega!"
    },

    # ═══════════════════════════════
    # ROMANTIC + ROMANCE + HINDI
    # ═══════════════════════════════

    "Dilwale Dulhania Le Jayenge": {
        "mood": "romantic",
        "genre": "Romance",
        "language": "Hindi",
        "duration": "Long",
        "rating": 8.0,
        "description": "Classic! Europe mein milte hain, India mein shaadi ki ladhai!"
    },
    "Jab We Met": {
        "mood": "romantic",
        "genre": "Romance",
        "language": "Hindi",
        "duration": "Long",
        "rating": 7.9,
        "description": "Ek sad businessman ek zindadil ladki se milta hai train mein!"
    },
    "Rockstar": {
        "mood": "romantic",
        "genre": "Romance",
        "language": "Hindi",
        "duration": "Long",
        "rating": 7.9,
        "description": "Ek struggling musician aur uski tragic love story!"
    },
    "Tamasha": {
        "mood": "romantic",
        "genre": "Romance",
        "language": "Hindi",
        "duration": "Long",
        "rating": 7.5,
        "description": "Corsica mein milte hain, reality mein ek dusre ko nahi pehchante!"
    },
    "Ae Dil Hai Mushkil": {
        "mood": "romantic",
        "genre": "Romance",
        "language": "Hindi",
        "duration": "Long",
        "rating": 6.6,
        "description": "One sided love ki pain aur healing!"
    },
    "Yeh Jawaani Hai Deewani": {
        "mood": "romantic",
        "genre": "Romance",
        "language": "Hindi",
        "duration": "Long",
        "rating": 7.1,
        "description": "Zindagi jeene ka alag andaz — adventure vs love!"
    },

    # ═══════════════════════════════
    # ROMANTIC + ROMANCE + ENGLISH
    # ═══════════════════════════════

    "The Notebook": {
        "mood": "romantic",
        "genre": "Romance",
        "language": "English",
        "duration": "Long",
        "rating": 7.8,
        "description": "1940s America mein ek eternal love story!"
    },
    "La La Land": {
        "mood": "romantic",
        "genre": "Romance",
        "language": "English",
        "duration": "Long",
        "rating": 8.0,
        "description": "LA mein ek actress aur musician ki bittersweet love story!"
    },
    "About Time": {
        "mood": "romantic",
        "genre": "Romance",
        "language": "English",
        "duration": "Long",
        "rating": 7.8,
        "description": "Ek man time travel karke apni love life theek karta hai!"
    },
    "Before Sunrise": {
        "mood": "romantic",
        "genre": "Romance",
        "language": "English",
        "duration": "Long",
        "rating": 8.1,
        "description": "Vienna mein ek raat do strangers ki conversation — magical!"
    },
    "Eternal Sunshine of the Spotless Mind": {
        "mood": "romantic",
        "genre": "Romance",
        "language": "English",
        "duration": "Long",
        "rating": 8.3,
        "description": "Ek couple apni memories erase karwata hai — kya ye sahi tha?"
    },

    # ═══════════════════════════════
    # EXCITED + COMEDY + HINDI
    # ═══════════════════════════════

    "3 Idiots": {
        "mood": "excited",
        "genre": "Comedy",
        "language": "Hindi",
        "duration": "Long",
        "rating": 8.4,
        "description": "Teen dost engineering college mein — ek classic!"
    },
    "Hera Pheri": {
        "mood": "excited",
        "genre": "Comedy",
        "language": "Hindi",
        "duration": "Long",
        "rating": 8.2,
        "description": "Raju Shyam aur Babu Bhaiya ka iconic comedy caper!"
    },
    "Golmaal": {
        "mood": "excited",
        "genre": "Comedy",
        "language": "Hindi",
        "duration": "Long",
        "rating": 7.3,
        "description": "Char dost ek blind couple ko fool karte hain — mayhem ensues!"
    },
    "Andaz Apna Apna": {
        "mood": "excited",
        "genre": "Comedy",
        "language": "Hindi",
        "duration": "Long",
        "rating": 8.0,
        "description": "Aamir aur Salman dono ek ameer ladki se shaadi karna chahte hain!"
    },
    "Dhamaal": {
        "mood": "excited",
        "genre": "Comedy",
        "language": "Hindi",
        "duration": "Long",
        "rating": 7.3,
        "description": "Char dost ek hidden treasure dhundte hain — total chaos!"
    },

    # ═══════════════════════════════
    # EXCITED + COMEDY + ENGLISH
    # ═══════════════════════════════

    "The Grand Budapest Hotel": {
        "mood": "excited",
        "genre": "Comedy",
        "language": "English",
        "duration": "Long",
        "rating": 8.1,
        "description": "Europe ke best hotel ka legendary concierge aur uski adventures!"
    },
    "Game Night": {
        "mood": "excited",
        "genre": "Comedy",
        "language": "English",
        "duration": "Long",
        "rating": 7.0,
        "description": "Ek game night real crime mein badal jaati hai!"
    },
    "Knives Out": {
        "mood": "excited",
        "genre": "Comedy",
        "language": "English",
        "duration": "Long",
        "rating": 7.9,
        "description": "Ek murder mystery jahan sab suspect hain!"
    },
    "The Nice Guys": {
        "mood": "excited",
        "genre": "Comedy",
        "language": "English",
        "duration": "Long",
        "rating": 7.4,
        "description": "1970s LA mein ek unlikely detective duo!"
    },

    # ═══════════════════════════════
    # BORED + SCI-FI + HINDI
    # ═══════════════════════════════

    "Ra One": {
        "mood": "bored",
        "genre": "Sci-Fi",
        "language": "Hindi",
        "duration": "Long",
        "rating": 4.9,
        "description": "Ek game character real world mein aa jaata hai!"
    },
    "Krrish 3": {
        "mood": "bored",
        "genre": "Sci-Fi",
        "language": "Hindi",
        "duration": "Long",
        "rating": 5.3,
        "description": "India ka superhero Krrish mutants se ladhta hai!"
    },
    "2.0": {
        "mood": "bored",
        "genre": "Sci-Fi",
        "language": "Hindi",
        "duration": "Long",
        "rating": 6.0,
        "description": "Rajinikanth ek scientist jo ek supernatural force se ladhta hai!"
    },

    # ═══════════════════════════════
    # SHORT DURATION — MIXED
    # ═══════════════════════════════

    "Drishyam": {
        "mood": "bored",
        "genre": "Thriller",
        "language": "Hindi",
        "duration": "Short",
        "rating": 8.2,
        "description": "Ajay Devgn apne family ko bachata hai ek cover-up mein!"
    },
    "Badlapur": {
        "mood": "sad",
        "genre": "Thriller",
        "language": "Hindi",
        "duration": "Short",
        "rating": 7.9,
        "description": "Ek aadmi 15 saal baad badla leta hai apni family ke murder ka!"
    },
    "Talvar": {
        "mood": "bored",
        "genre": "Thriller",
        "language": "Hindi",
        "duration": "Short",
        "rating": 8.2,
        "description": "Aarushi murder case ki real story — kaun tha asli qatil?"
    },
    "Get Hard": {
        "mood": "excited",
        "genre": "Comedy",
        "language": "English",
        "duration": "Short",
        "rating": 6.0,
        "description": "Will Ferrell ek convicted man ko jail ke liye prepare karta hai!"
    },
    "Superbad": {
        "mood": "excited",
        "genre": "Comedy",
        "language": "English",
        "duration": "Short",
        "rating": 7.6,
        "description": "High school ke last din — do dost ek party ke liye sab kuch karte hain!"
    },
    "The Breakfast Club": {
        "mood": "sad",
        "genre": "Drama",
        "language": "English",
        "duration": "Short",
        "rating": 7.9,
        "description": "Five very different students ek Saturday detention mein bond karte hain!"
    },
    "Whiplash": {
        "mood": "bored",
        "genre": "Drama",
        "language": "English",
        "duration": "Short",
        "rating": 8.5,
        "description": "Ek drummer aur uska brutal music teacher — excellence ka obsession!"
    },
    "Good Will Hunting": {
        "mood": "sad",
        "genre": "Drama",
        "language": "English",
        "duration": "Short",
        "rating": 8.3,
        "description": "Ek genius janitor jo apni problems se bhag raha hai!"
    },

}


film_types={ " -- ":
    # Quick Count Check
    # - Excited + Horror + Hindi: 5 movies
    # - Excited + Horror + English: 7 movies
    # - Excited + Action + Hindi: 7 movies
    # - Excited + Action + English: 6 movies
    # - Bored + Thriller + Hindi: 6 movies
    # - Bored + Thriller + English: 6 movies
    # - Bored + Drama + Hindi: 5 movies
    # - Bored + Sci-Fi + English: 5 movies
    # - Sad + Drama + Hindi: 6 movies
    # - Sad + Drama + English: 6 movies
    # - Romantic + Romance + Hindi: 6 movies
    # - Romantic + Romance + English: 5 movies
    # - Excited + Comedy + Hindi: 5 movies
    # - Excited + Comedy + English: 4 movies
    # - Bored + Sci-Fi + Hindi: 3 movies
    # - Short Duration Mixed: 8 movies
    # - **Total: 100 movies!**
    4}
