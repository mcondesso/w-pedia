import wikipedia
import random
from globals import GameMode

PEOPLE = {
    "sports": [
        "Michael Jordan",
        "Lionel Messi",
        "Cristiano Ronaldo",
        "Pelé",
        "Muhammad Ali",
        "Usain Bolt",
        "Michael Phelps",
        "Roger Federer",
        "Rafael Nadal",
        "Novak Djokovic",
        "LeBron James",
        "Kobe Bryant",
        "Tom Brady",
        "Diego Maradona",
        "Johan Cruyff",
        "Zinedine Zidane",
        "Ronaldinho",
        "Tiger Woods",
        "Jack Nicklaus",
        "Serena Williams",
        "Steffi Graf",
        "Martina Navratilova",
        "Simone Biles",
        "Nadia Comaneci",
        "Carl Lewis",
        "Jesse Owens",
        "Wayne Gretzky",
        "Babe Ruth",
        "Wilt Chamberlain",
        "Magic Johnson",
        "Larry Bird",
        "Shaquille O'Neal",
        "Stephen Curry",
        "Tim Duncan",
        "Kareem Abdul-Jabbar",
        "Bill Russell",
        "Hakeem Olajuwon",
        "Kevin Durant",
        "Manny Pacquiao",
        "Mike Tyson",
        "Floyd Mayweather Jr.",
        "Sugar Ray Robinson",
        "Joe Louis",
        "Rocky Marciano",
        "Conor McGregor",
        "Khabib Nurmagomedov",
        "Jon Jones",
        "Georges St-Pierre",
        "Valentino Rossi",
        "Ayrton Senna",
        "Michael Schumacher",
        "Lewis Hamilton",
        "Max Verstappen",
        "Niki Lauda",
        "Fernando Alonso",
        "Alain Prost",
        "Sachin Tendulkar",
        "Virat Kohli",
        "Don Bradman",
        "Brian Lara",
        "Ricky Ponting",
        "Bjørn Borg",
        "Pete Sampras",
        "Andre Agassi",
        "Andy Murray",
        "Monica Seles",
        "Venus Williams",
        "Naomi Osaka",
        "Iga Świątek",
        "Mika Häkkinen",
        "Sebastian Vettel",
        "Edwin Moses",
        "Yelena Isinbayeva",
        "Eliud Kipchoge",
        "Haile Gebrselassie",
        "Paavo Nurmi",
        "Abebe Bikila",
        "Cristiano Ronaldo Nazário",
        "Xavi Hernández",
        "Andrés Iniesta",
        "Franz Beckenbauer",
        "George Best",
        "Lev Yashin",
        "Gerd Müller",
        "Paolo Maldini",
        "Roberto Carlos",
        "Cafu",
        "Alessandro Del Piero",
        "David Beckham",
        "Thierry Henry",
        "Kylian Mbappé",
        "Erling Haaland",
        "Kevin De Bruyne",
        "Alex Morgan",
        "Megan Rapinoe",
        "Bjørn Dæhlie",
        "Ole Einar Bjørndalen",
        "Tony Hawk",
        "Kelly Slater",
        "Michael Johnson"
    ],
    "influential": [
        "Alexander the Great",
        "Julius Caesar",
        "Augustus",
        "Genghis Khan",
        "Napoleon Bonaparte",
        "George Washington",
        "Abraham Lincoln",
        "Winston Churchill",
        "Mahatma Gandhi",
        "Nelson Mandela",
        "Martin Luther King Jr.",
        "Joan of Arc",
        "Cleopatra",
        "Queen Elizabeth I",
        "Charlemagne",
        "Leonardo da Vinci",
        "Michelangelo",
        "William Shakespeare",
        "Johann Wolfgang von Goethe",
        "Miguel de Cervantes",
        "Homer",
        "Dante Alighieri",
        "Isaac Newton",
        "Albert Einstein",
        "Galileo Galilei",
        "Nikola Tesla",
        "Thomas Edison",
        "Marie Curie",
        "Charles Darwin",
        "Stephen Hawking",
        "Alan Turing",
        "Tim Berners-Lee",
        "Aristotle",
        "Plato",
        "Socrates",
        "Sun Tzu",
        "René Descartes",
        "Immanuel Kant",
        "Karl Marx",
        "Sigmund Freud",
        "Adam Smith",
        "Voltaire",
        "John Locke",
        "Niccolò Machiavelli",
        "Johannes Gutenberg",
        "Mozart",
        "Ludwig van Beethoven",
        "Johann Sebastian Bach",
        "Pablo Picasso",
        "Vincent van Gogh",
        "Salvador Dalí",
        "Claude Monet",
        "Rembrandt",
        "Christopher Columbus",
        "Marco Polo",
        "Ferdinand Magellan",
        "Neil Armstrong",
        "Yuri Gagarin",
        "Henry Ford",
        "Steve Jobs",
        "Bill Gates",
        "Elon Musk",
        "Jeff Bezos",
        "Mark Zuckerberg",
        "Larry Page",
        "Sergey Brin",
        "Walt Disney",
        "George Orwell",
        "J.R.R. Tolkien",
        "Fyodor Dostoevsky",
        "Leo Tolstoy",
        "Victor Hugo",
        "Frida Kahlo",
        "Andy Warhol"
    ]
}

PLACES = {
    "countries": [
        "United States",
        "China",
        "Japan",
        "Germany",
        "France",
        "United Kingdom",
        "Italy",
        "Spain",
        "Canada",
        "Australia",
        "Brazil",
        "Mexico",
        "Argentina",
        "Russia",
        "India",
        "South Korea",
        "North Korea",
        "Saudi Arabia",
        "United Arab Emirates",
        "Turkey",
        "Egypt",
        "South Africa",
        "Nigeria",
        "Morocco",
        "Kenya",
        "Greece",
        "Portugal",
        "Netherlands",
        "Belgium",
        "Switzerland",
        "Austria",
        "Sweden",
        "Norway",
        "Denmark",
        "Finland",
        "Poland",
        "Ukraine",
        "Israel",
        "Iran",
        "Thailand",
        "Vietnam",
        "Indonesia",
        "Singapore",
        "Malaysia",
        "Pakistan",
        "New Zealand",
        "Ireland",
        "Cuba",
        "Chile",
        "Peru"
    ],
    "cities": [
        "New York",
        "Los Angeles",
        "Chicago",
        "Miami",
        "Las Vegas",
        "London",
        "Paris",
        "Rome",
        "Madrid",
        "Barcelona",
        "Berlin",
        "Amsterdam",
        "Vienna",
        "Prague",
        "Moscow",
        "Dubai",
        "Tokyo",
        "Kyoto",
        "Seoul",
        "Beijing",
        "Shanghai",
        "Hong Kong",
        "Singapore",
        "Bangkok",
        "Istanbul",
        "Jerusalem",
        "Cairo",
        "Cape Town",
        "Sydney",
        "Melbourne",
        "Rio de Janeiro",
        "Buenos Aires",
        "Mexico City",
        "Toronto",
        "Vancouver",
        "San Francisco",
        "Washington D.C.",
        "Boston",
        "Athens",
        "Venice",
        "Florence",
        "Milan",
        "Lisbon",
        "Dublin",
        "Mumbai",
        "Delhi",
        "Karachi",
        "Bangalore",
        "Honolulu",
        "Monaco"
    ]
}

# Set user for Wiki API
wikipedia.set_user_agent("W-Pedia/1.0 (https://github.com/mcondesso/w-pedia/)")


def get_random_objects(mode: GameMode, category: str, amount: int = 3):
    """
    Creates list of random objects (people or places) depending on game mode and category.
    Args:
        mode: GameMode
        category: str
        amount: int

    Returns: list with random objects
    """
    # "Who" game mode, iterate in PEOPLE
    if mode == GameMode.WHO:
        if category not in PEOPLE:
            return []

        return random.sample(PEOPLE[category], amount)

    # "Where" game mode, iterate PLACES
    if mode == GameMode.WHERE:
        if category not in PLACES:
            return []
        return random.sample(PLACES[category], amount)
    #
    else:
        return []


def get_summary(object_name: str, sentences=3):
    """
    Creates a summary of a person, place or event.
    Args:
        object_name: str
        sentences: int

    Returns: dictionary with name and summary
    """
    try:
        summary = wikipedia.summary(object_name, sentences=sentences, auto_suggest=False)
        return {"answer": object_name, "summary": summary}

    except wikipedia.exceptions.PageError:
        print(f"The page for {object_name} could not be found.")

    except Exception as e:
        print(f"Error for {object_name}: {e}")


def generate_objects_data(list_elements: list):
    """
    Iterate a list of element to give the summary of each one.
    Args:
        list_elements: list

    Returns: list of dictionaries
    """
    results = []
    for element in list_elements:
        element_summary = get_summary(element)
        if element_summary:
            results.append(element_summary)

    return results


def get_random_wiki_data(mode: GameMode, category: str):
    """
    Depending on the game mode, it will create a list of random objects, iterate through them
    and create a dictionary with their summary as an answer.
    Args:
        mode: GameMode
        category: str

    Returns: list of dictionaries
    """

    # "Who" game mode: Gets random places and returns dicts with their summary"
    if mode == GameMode.WHO:
        list_of_people = get_random_objects(GameMode.WHO, category)
        return generate_objects_data(list_of_people)

    # "Where" mode: Search for random places in category "countries" or "cities"
    if mode == GameMode.WHERE:
        list_of_places = get_random_objects(GameMode.WHERE, category)
        return generate_objects_data(list_of_places)

    else:
        print("Error! Game mode not implemented yet.")
        return None


"""
--This lines were for testing--

def run():
    test = get_random_wiki_data(mode=GameMode.WHO, category="influential")
    print("-- Testing: --")
    for element in test:
        print(f"{element["answer"]} : \n{element["summary"]}")
        print("-"*20)


run()
"""""
