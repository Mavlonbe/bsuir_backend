from py2neo import Graph

from typing import List

from api.serializers import EventSerializer

class Agent(object):
    client = Graph("bolt://localhost:7687", auth=("neo4j", "cnbem5ug"))
    
    def search_recipes(self, ingredients: EventSerializer) -> dict:
        recipes = self.client.run(
            '''
            MATCH (r:Recipe)-[:CONTAINS_NER]->(n:NER)
            WHERE n.name IN $ner_list
            AND NOT EXISTS {
                MATCH (r)-[:CONTAINS_NER]->(excluded:NER)
                WHERE excluded.name IN ["pork", "gelatin", "crab", "lobster", "oyster", "mussels", "squid", "octopus", "shark", "eel", "frog", "turtle"]
                }
            WITH r, COUNT(n) AS nerCount
            RETURN r
            ORDER BY nerCount DESC
            LIMIT 3
            ''', {'ner_list': ingredients.data['Message']}
            )
        
        return recipes.to_data_frame().to_dict()
    
    @classmethod
    def trigger(cls, event: EventSerializer) -> (dict, None):
        if event.data['EventType'] == "Search_Recipe_By_Ingredients_Halal":
            return cls.search_recipes(cls, event)
        
        return None
        
        
    
    