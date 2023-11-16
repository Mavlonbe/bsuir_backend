import importlib
import os

def read_agents():
    agents = []
    directory = './agents/'

    for filename in os.listdir(directory):  
        if filename.endswith('.py'):  
            module_name = filename[:-3]  
            try:
             module = importlib.import_module("agents." + module_name)
             agent_class = getattr(module, 'Agent', None)
             if agent_class is not None:
        
                 agents.append(agent_class)
                
            except Exception as e:
                print(f"Error importing {module_name}: {e}")
                
    return agents