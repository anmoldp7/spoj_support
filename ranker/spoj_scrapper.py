import bs4
import requests
import re

class spoj_crawler:
    def __init__(self, handle):
        self.handleExists = True

        try:
            url = "https://www.spoj.com/users/" + handle
            soup = bs4.BeautifulSoup(requests.get(url).text, "html.parser")
        except:
            self.handleExists = False

        self.handle_name = handle
        self.name = "N/A"
        self.locale = "N/A"
        self.joined_on = "N/A"
        self.world_rank = "N/A"
        self.points = 0.0
        self.institution = "N/A"
        self.problems_solved = "N/A"
        self.solutions_submitted = "N/A"

        if self.handleExists:
            # find handle name
            self.handle_name = handle
           
            # find name
            name_marks = soup.find_all("img", { "class" : "avatar small-left-margin" })
            for s in name_marks:
                self.name = s.parent.h3.text
            name = self.name # Remove this
            # find location
            locale_marks = soup.find_all("i", { "class" : "fa fa-map-marker"})
            for s in locale_marks:
                self.locale = s.parent.text[1 : ]
            locale = self.locale # Remove this

            # find date of joining
            joined_on_marks = soup.find_all("i", { "class" : "fa fa-clock-o" })
            for s in joined_on_marks:
                self.joined_on = s.parent.text
            joined_on = self.joined_on # Remove this

            # find world rank and points
            world_rank_marks = soup.find_all("i", { "class" : "fa fa-trophy" })
            for s in world_rank_marks:
                if "#" in s.parent.text:
                    temp = s.parent.text.split("#")[1].split()
                    self.world_rank = temp[0]
                    self.points = temp[1][1 : ]
            world_rank = self.world_rank # Remove this
            points = self.points # Remove this
            
            #find institution
            institution_marks = soup.find_all("i", { "class" : "fa fa-building-o " })
            for s in institution_marks:
                self.institution = s.parent.text[14 : ]
            institution = self.institution # Remove this
            
            #find problems solved and solutions submitted
            stats_marks = soup.find("dl", { "class" : "dl-horizontal profile-info-data profile-info-data-stats"})
            stats_marks = stats_marks.find_all("dd")
            self.problems_solved = stats_marks[0].text
            self.solutions_submitted = stats_marks[1].text
            problems_solved = self.problems_solved # Remove this
            solutions_submitted = self.solutions_submitted # Remove this