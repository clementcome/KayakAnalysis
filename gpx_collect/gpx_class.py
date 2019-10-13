from xml.etree import ElementTree as ET

topografix_tag = '{http://www.topografix.com/GPX/1/1}'
garmin_tag = '{http://www.garmin.com/xmlschemas/TrackPointExtension/v1}'

class GPX():
    def __init__(self, file_path = None, tree = None, global_tag = '{http://www.topografix.com/GPX/1/1}'):
        if file_path:
            self.tree = ET.parse(file_path)
        elif type(tree) == ET.Element:
            self.tree = tree
        else:
            print("You should provide a path to the xml file under file_path OR an xml.etree.ElementTree under tree")
        self.global_tag = global_tag
    
    def search_string(self,*args):
        ans = ""
        for arg in args:
            ans += self.global_tag + arg + "/"
        ans = ans[:-1]
        return ans
    
    def find(self,*args):
        search_string = self.search_string(*args)
        return self.tree.find(search_string)

    def findall(self,*args):
        search_string = self.search_string(*args)
        return self.tree.findall(search_string)
    
    def attrib(self):
        return self.tree.attrib
    
    def tag(self):
        return self.tree.tag