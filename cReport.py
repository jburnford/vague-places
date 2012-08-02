import datetime

class cReport():
    points = 0;
    alpha = 1;
    optalpha = 1;
    date = str(datetime.datetime.now());
    countries = [];
    country_val = [];
    live = False;
    WKT = "";
    query = "";

    def set_country_count(self,places):
        """
            For all the countries counts the places extracted
        """
        self.points = len(places);
        for p in places:
            try:
                index = self.countries.index(p.country)
                self.country_val[index] += 1
            except:
                self.countries.append(p.country)
                self.country_val.append(0)

    def print_report(self):
        self.print_title();
        
        self.print_banner("DATASET")
        if(self.live):
            print "DBpedia Live "+str(self.date)
        else:
            print "DBpedia Last release version"

        print "QUERY: "+str(self.query).rjust(20);
        print "Retrieved Points:\t"+str(self.points);
        print;
        print "country".rjust(30),"|".rjust(5),"total_points".rjust(5)
        
        for i,c in enumerate(self.countries):
            print str(c).rjust(30),"|".rjust(5),str(self.country_val[i]).rjust(5)

      
        self.print_banner("Alpha Shape")
        print "---- WKT ---";
        print self.WKT;
        print "Alpha:"+str(self.alpha).rjust(20)
        print "Optimal Alpha: "+str(self.optalpha).rjust(20);
        


    def print_title(self):
        print;
        print "###########################################"
        print "# REPORT GENERATED BY vagueplaces.py"
        print "#  "+str(self.date).center(40)
        print "#"
        print "###########################################"
        print;

    def print_banner(self,text):
        print;
        print "###########################################"
        print "#"
        print "#"+str(text).center(40)
        print "#"
        print "###########################################"
        print;

    def write_report(self,fileh):
        pass;

    def set_alphas(self,alpha,optalpha):
        self.alpha = alpha;
        self.optalpha = optalpha;

    def set_wkt(self,wkt):
        self.WKT = wkt;

    def set_query(self,query):
        self.query = query;
    
    def set_live(self,live):
        self.live = live;
