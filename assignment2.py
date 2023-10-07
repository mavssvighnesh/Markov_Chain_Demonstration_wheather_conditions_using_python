import numpy as np    #numpy library for random choice 

class WeatherSimulation:
    
    
    def __init__(self, transition_probabilities, holding_times):    #constructor for the class WeatherSimulation 
        self.status = list(transition_probabilities.keys())
        self.current = 'sunny'
        self.transition_probabilities = transition_probabilities
        self.holding_times = holding_times
        self.time_left = holding_times['sunny']

        for state, probabilities in transition_probabilities.items():  #iteration to get sum of the values in transition_probabilites dictionary 
         if not np.isclose(sum(probabilities.values()), 1.0):
             raise RuntimeError(f"The sum of transition probabilities for state {state} is not equal to 1.")    #raises error if sum of transition table is not equal to 1 
    
    
    def get_states(self): #all states will be displayed 
        return self.status
    
    
    def current_state(self):   #it displays the current state 
        return self.current
   
   
    def next_state(self): #method to get the next state 

        if self.time_left > 0:
            self.time_left -= 1


        else:
            probabilities = self.transition_probabilities[self.current]
            self.current = np.random.choice(
            self.status, p=list(probabilities.values()))
            self.time_left = self.holding_times[self.current]
            self.time_left -= 1
    
    
    def set_state(self, new_state):  #method for  transistion for next state and new_state as argument for the method  

        if new_state not in self.status:
            raise ValueError(f"Invalid state name: {new_state}.")  #raise error if the new state is not a value in the dictionary 
        self.current = new_state
        self.time_left = self.holding_times[new_state]
    
   
    def current_state_remaining_hours(self): #returns the value of  time_left in the current state 
        return self.time_left
    
    
    def iterable(self):   #gets the yield of current state and moves to next state 
        while True:
            yield self.current
            self.next_state()

    
    
    def simulate(self, hours):   #method to run the program for a certain hour constraints and gives the output 

            if not isinstance(hours, int) or hours <= 0:
                raise ValueError('Hours should be a positive non-zero integer')
            state_count = {state: 0 for state in self.status}
            for _ in range(hours):

                 self.next_state()
                 state_count[self.current] += 1
                 state_per = [state_count[state] *100 / hours for state in self.status]
            return state_per