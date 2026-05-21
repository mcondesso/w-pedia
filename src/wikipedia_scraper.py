import wikipedia
import random
from src.globals import GameMode, NUMBER_OF_API_TRIES, NUMBER_OF_ROUNDS
from src.country_api import get_random_countries, CountriesError


class WikipediaError(Exception):
    """Base exception class for errors thrown by the wikipedia module"""


class InvalidOutputError(WikipediaError):
    """Thrown when the output from the wikipedia API is invalid"""


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
        "Andy Warhol",
    ],
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
        "Peru",
    ],
    "cities": [
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
        "Monaco",
    ],
}

EVENTS = {
    "military": [
        "World War I",
        "World War II",
        "Cold War",
        "Vietnam War",
        "Korean War",
        "American Civil War",
        "Spanish Civil War",
        "Napoleonic Wars",
        "Crusades",
        "French Revolution",
        "Russian Revolution",
        "American Revolution",
        "Battle of Waterloo",
        "Battle of Hastings",
        "Battle of Stalingrad",
        "Normandy landings",
        "Attack on Pearl Harbor",
        "Cuban Missile Crisis",
        "Fall of Constantinople",
        "Six-Day War",
        "Gulf War",
        "War on Terror",
        "Russian invasion of Ukraine",
        "Falklands War",
        "Trojan War",
    ],
    "historical": [
        "Apollo 11",
        "Titanic",
        "Chernobyl disaster",
        "Fall of the Berlin Wall",
        "French Revolution",
        "Industrial Revolution",
        "Renaissance",
        "Black Death",
        "Discovery of America",
        "First Moon Landing",
        "Signing of the Magna Carta",
        "Boston Tea Party",
        "Watergate scandal",
        "Woodstock Festival",
        "Live Aid",
        "COVID-19 pandemic",
        "Hindenburg disaster",
        "Fukushima disaster",
        "Great Fire of London",
        "Pompeii",
        "Human Genome Project",
        "Sputnik 1",
        "California Gold Rush",
        "Stock Market Crash of 1929",
        "Moon landing conspiracy theories",
    ],
}

# Set user for Wiki API
wikipedia.set_user_agent("W-Pedia/1.0 (https://github.com/mcondesso/w-pedia/)")


def get_random_objects(mode: GameMode, category: str, amount: int = 5):
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
        if category == "countries":
            try:
                return get_random_countries(amount)
            except CountriesError as error:
                raise WikipediaError from error
        else:
            return random.sample(PLACES[category], amount)

    # "What" game mode, iterate EVENTS
    if mode == GameMode.WHAT:
        if category not in EVENTS:
            return []
        return random.sample(EVENTS[category], amount)
    # No game mode:
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
    for _ in range(NUMBER_OF_API_TRIES):
        try:
            summary = wikipedia.summary(
                object_name, sentences=sentences, auto_suggest=False
            )
            return {"answer": object_name, "summary": summary}

        except wikipedia.exceptions.PageError as e:
            pass

        except Exception as e:
            print(f"Error for {object_name}: {e}")


def generate_objects_data(list_elements: list, max_amount=NUMBER_OF_ROUNDS + 1):
    """
    Iterate a list of element to give the summary of each one.
    Args:
        list_elements: list
        max_amount: int

    Returns: list of dictionaries
    """
    results = []
    for element in list_elements:
        element_summary = get_summary(element)
        if element_summary:
            results.append(element_summary)
            if len(results) == max_amount:
                break
    return results


def validate_output(wiki_data: list[dict]):
    if not wiki_data:
        raise InvalidOutputError("Empty data")
    for entry in wiki_data:
        if not entry.get("answer", "") or not entry.get("summary", ""):
            raise InvalidOutputError("Wrong format")


def get_random_wiki_data(mode: GameMode, category: str) -> list[dict] | None:
    """
    Depending on the game mode, it will create a list of random objects, iterate through them
    and create a dictionary with their summary as an answer.
    Args:
        mode: GameMode
        category: str

    Returns: list of dictionaries
    """

    if mode not in {GameMode.WHO, GameMode.WHERE, GameMode.WHAT}:
        print("Error! Game mode not implemented yet.")
        return None
    else:
        list_of_entities = get_random_objects(mode, category)
        wiki_data = generate_objects_data(list_of_entities)
        validate_output(wiki_data)

        return wiki_data


"""
def run():
    test = get_random_wiki_data(mode=GameMode.WHAT, category="military")
    print("-- Testing: --")
    for element in test:
        print(f"{element["answer"]} : \n{element["summary"]}")
        print("-" * 20)

run()
"""
