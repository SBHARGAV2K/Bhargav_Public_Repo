import pandas as pd


if __name__ == '__main__':
    df = pd.DataFrame(
        {
            'house_id': ['H1', 'H2', 'H3', 'H4', 'H5'], #Unique ID of the house
            'is_furnished': [1,0,1,1,0], #Is the house furnished or not
            'is_on_ground_floor': [0,0,1,0,1], #Is the house located in ground floor
            'has_car_park': [0,0,0,1,1], #Does the house has a car park
            'sales_status_actual': [1,0,1,1,0], #Actual status of sales (1 if sold, 0 otherwise)
            'sales_status_predicted': [0,0,1,1,1], #Predicted sales status (1 if sold, 0 otherwise)
        }
    )
    
    '''
    The following columns are created using logic gates concepts:-
        * C1:- is the house located on the ground floor and furnished (uses AND gate);
        * C2:- is the house located on the ground floor or has a car park, but not both (uses XOR gate);
        * C3:- does actual and predicted sales status match (uses XNOR gate);
    '''
    df.insert(4,'C1',df['is_furnished'] & df['is_on_ground_floor'])
    df.insert(5,'C2',df['has_car_park'] ^ df['is_on_ground_floor'])
    df['C3'] = ~(df['sales_status_actual'] ^ df['sales_status_predicted']) + 2
    print(df)