import requests
import json

class Multilinguist:
  """This class represents a world traveller who knows
  what languages are spoken in each country around the world
  and can cobble together a sentence in most of them
  (but not very well)
  """

  translatr_base_url = "http://bitmakertranslate.herokuapp.com"
  countries_base_url = "https://restcountries.eu/rest/v2/name"
  #{name}?fullText=true
  #?text=The%20total%20is%2020485&to=ja&from=en

  def __init__(self):
    """Initializes the multilinguist's current_lang to 'en'

    Returns
    -------
    Multilinguist
        A new instance of Multilinguist
    """
    self.current_lang = 'en'

  def language_in(self, country_name):
    """Uses the RestCountries API to look up one of the languages
    spoken in a given country

    Parameters
    ----------
    country_name : str
         The full name of a country.

    Returns
    -------
    bool
        2 letter iso639_1 language code.
    """
    params = {'fullText': 'true'}
    response = requests.get(f"{self.countries_base_url}/{country_name}", params=params)
    json_response = json.loads(response.text)
    return json_response[0]['languages'][0]['iso639_1']

  def travel_to(self, country_name):
    """Sets current_lang to one of the languages spoken
    in a given country

    Parameters
    ----------
    country_name : str
        The full name of a country.

    Returns
    -------
    str
        The new value of current_lang as a 2 letter iso639_1 code.
    """
    local_lang = self.language_in(country_name)
    self.current_lang = local_lang
    return self.current_lang

  def say_in_local_language(self, msg):
    """(Roughly) translates msg into current_lang using the Transltr API

    Parameters
    ----------
    msg : str
        A message to be translated.

    Returns
    -------
    str
        A rough translation of msg.
    """
    params = {'text': msg, 'to': self.current_lang, 'from': 'en'}
    response = requests.get(self.translatr_base_url, params=params)
    json_response = json.loads(response.text)
    return json_response['translationText']


class MathGenius(Multilinguist):


    def report_total(self, list = []):
        sum_total = sum(list)
        return "{} {}".format(self.say_in_local_language('The total is'), sum_total)

class QouteCollector(Multilinguist):


    quotes = [
    "You have to feel a defeat. You cannot say ‘I don’t care, it’s not important’. If I was allowed to say sh*t I would say sh*t but I’m not allowed! It was important and we lost, so that feels not too good. You always have to strike back. We can say all of these things, but you know you can fall down and then you have to stand up. That’s the truth, but it’s completely normal – only silly idiots stay on the floor and wait for the next defeat. Of course we will strike back – 100%. We struck back today in the game."
    ]

    def collector(self, quote):
        self.qoutes.append(quote)

    def generator(self):
        return self.say_in_local_language(random.choice(self.quotes))


# me = MathGenius()
# print(me.report_total([23,45,676,34,5778,4,23,5465])) # The total is 12048
# me.travel_to("India")
# print(me.report_total([6,3,6,68,455,4,467,57,4,534])) # है को कुल 1604
# me.travel_to("Italy")
# print(me.report_total([324,245,6,343647,686545])) # È Il totale 1030767


traveller_1 = Multilinguist()
traveller_1.language_in('Zimbabwe')
traveller_1.travel_to('France')
print(traveller_1.say_in_local_language("Lets play some soccer"))
