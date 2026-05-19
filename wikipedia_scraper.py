
import wikipedia
import random
from game import GameMode


PEOPLE = {"sports":  [
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
    "Albert Einstein",
    "Mahatma Gandhi",
    "Martin Luther King Jr.",
    "Nelson Mandela",
    "Winston Churchill",
    "Franklin D. Roosevelt",
    "John F. Kennedy",
    "Ronald Reagan",
    "Mikhail Gorbachev",
    "Vladimir Putin",
    "Xi Jinping",
    "Barack Obama",
    "Angela Merkel",
    "Margaret Thatcher",
    "Adolf Hitler",
    "Joseph Stalin",
    "Mao Zedong",
    "Vladimir Lenin",
    "Che Guevara",
    "Fidel Castro",
    "Osama bin Laden",
    "Steve Jobs",
    "Bill Gates",
    "Elon Musk",
    "Jeff Bezos",
    "Mark Zuckerberg",
    "Larry Page",
    "Sergey Brin",
    "Tim Berners-Lee",
    "Alan Turing",
    "Nikola Tesla",
    "Stephen Hawking",
    "Marie Curie",
    "Sigmund Freud",
    "Pablo Picasso",
    "Andy Warhol",
    "Walt Disney",
    "Michael Jackson",
    "The Beatles",
    "Elvis Presley",
    "Madonna",
    "Taylor Swift",
    "Cristiano Ronaldo",
    "Lionel Messi",
    "Muhammad Ali",
    "Michael Jordan",
    "Pelé",
    "Marilyn Monroe",
    "Princess Diana",
    "Oprah Winfrey",
    "Coco Chanel",
    "Karl Lagerfeld",
    "Anna Wintour",
    "Martin Scorsese",
    "Steven Spielberg",
    "George Lucas",
    "Stan Lee",
    "Hayao Miyazaki",
    "J.K. Rowling",
    "George Orwell",
    "J.R.R. Tolkien",
    "Yuval Noah Harari",
    "Noam Chomsky",
    "Milton Friedman",
    "John Maynard Keynes",
    "Milton Keynes",
    "Henry Ford",
    "Neil Armstrong",
    "Yuri Gagarin",
    "Greta Thunberg",
    "Malala Yousafzai",
    "Pope John Paul II",
    "Pope Francis",
    "Dalai Lama",
    "Mother Teresa",
    "Aung San Suu Kyi",
    "Volodymyr Zelenskyy",
    "Donald Trump",
    "Joe Biden",
    "Emmanuel Macron",
    "Benjamin Netanyahu",
    "Kim Jong-un",
    "Saddam Hussein",
    "Muammar Gaddafi",
    "Ayatollah Khomeini",
    "Julian Assange",
    "Edward Snowden",
    "Julian Huxley",
    "Richard Dawkins",
    "Carl Sagan",
    "David Attenborough",
    "Jacques Cousteau",
    "Stephen King",
    "Agatha Christie",
    "Ernest Hemingway",
    "Frida Kahlo",
    "Banksy",
    "Usain Bolt",
    "Serena Williams"
]
         }

# Set user for Wiki API
wikipedia.set_user_agent("W-Pedia/1.0 (https://github.com/mcondesso/w-pedia/)")


def get_random_people(category, amount=3):
    """
    Return a random list of people from a category of PEOPLE.
    """
    if category not in PEOPLE:
        return []

    return random.sample(PEOPLE[category], amount)


def get_summary(object_name, sentences=3):
    """
    Return a dictionary with the name and summary of the given object_name.
    """
    try:
        summary = wikipedia.summary(object_name, sentences=sentences, auto_suggest=False)
        return {"name": object_name, "summary": summary}

    except wikipedia.exceptions.PageError:
        print(f"The page for {object_name} could not be found.")

    except Exception as e:
        print(f"Error: {e}")


def generate_people_data(category, amount=3):
    """
    Return a list of dictionaries for each person given the category.
    """
    selected_people = get_random_people(category, amount)
    results = []

    for person in selected_people:
        person_data = get_summary(person)
        if person_data:
            results.append(person_data)

    return results


def get_random_wiki_data(mode: GameMode, category):
    """
    Returns result depending on the game mode.
    """
    #TODO!!! change in the future
    category = "sports"

    if mode == GameMode.WHO:
        return generate_people_data(category)

    else:
        return None


def run():
    final = get_random_wiki_data(mode=GameMode.WHO, category="sports")
    print(final)


run()
